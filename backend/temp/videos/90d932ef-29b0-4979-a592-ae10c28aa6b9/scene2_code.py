from manim import *

class Scene2(Scene):
    def construct(self):
        # Title
        title = Text("MAC Address Filtering", font_size=32, color=BLUE).to_edge(UP)
        self.add(title)

        # Switch - Central Hub
        switch_box = Rectangle(width=2.5, height=1.5, color=TEAL, fill_opacity=0.2)
        switch_label = Text("Switch", font_size=24).move_to(switch_box.get_center())
        switch_group = VGroup(switch_box, switch_label).move_to(ORIGIN)

        # Nodes (Computers)
        node_a = Circle(radius=0.4, color=WHITE).shift(LEFT * 4 + UP * 1.5)
        node_b = Circle(radius=0.4, color=WHITE).shift(RIGHT * 4 + UP * 1.5)
        node_c = Circle(radius=0.4, color=WHITE).shift(LEFT * 4 + DOWN * 1.5)
        node_d = Circle(radius=0.4, color=WHITE).shift(RIGHT * 4 + DOWN * 1.5)

        label_a = Text("A", font_size=20).move_to(node_a.get_center())
        label_b = Text("B", font_size=20).move_to(node_b.get_center())
        label_c = Text("C", font_size=20).move_to(node_c.get_center())
        label_d = Text("D", font_size=20).move_to(node_d.get_center())

        nodes = VGroup(node_a, node_b, node_c, node_d, label_a, label_b, label_c, label_d)

        # Connections
        line_a = Line(node_a.get_right(), switch_box.get_left())
        line_b = Line(node_b.get_left(), switch_box.get_right())
        line_c = Line(node_c.get_right(), switch_box.get_left())
        line_d = Line(node_d.get_left(), switch_box.get_right())
        lines = VGroup(line_a, line_b, line_c, line_d)

        # MAC Table
        table_rect = Rectangle(width=2.5, height=2, color=WHITE).to_edge(RIGHT).shift(DOWN * 1)
        table_title = Text("MAC Table", font_size=18).next_to(table_rect, UP)
        table_content = VGroup(
            Text("Port 1: MAC A", font_size=16),
            Text("Port 2: MAC B", font_size=16),
            Text("Port 3: MAC C", font_size=16),
            Text("Port 4: MAC D", font_size=16)
        ).arrange(DOWN, aligned_edge=LEFT).move_to(table_rect.get_center())
        mac_table = VGroup(table_rect, table_title, table_content)

        # Display Initial State
        self.play(Create(switch_group), Create(nodes), Create(lines))
        self.play(Create(mac_table))
        self.wait(1)

        # Data Frame Animation
        # Packet from A to B
        packet = Rectangle(width=1.0, height=0.5, color=YELLOW, fill_opacity=0.8)
        packet_text = Text("To: MAC B", font_size=14, color=BLACK).move_to(packet.get_center())
        data_frame = VGroup(packet, packet_text).move_to(node_a.get_center())

        # Step 1: A to Switch
        self.play(data_frame.animate.move_to(switch_box.get_center()), run_time=1.5)
        
        # Step 2: Switch checks Table
        highlight = Rectangle(width=2.3, height=0.3, color=YELLOW, fill_opacity=0.3).move_to(table_content[1].get_center())
        self.play(Create(highlight))
        self.play(Indicate(switch_box, color=GOLD))
        self.wait(0.5)

        # Step 3: Switch forwards only to B
        self.play(
            data_frame.animate.move_to(node_b.get_center()),
            Uncreate(highlight),
            run_time=1.5
        )

        # Explanation Text
        explanation = Text("Dedicated bandwidth, no collisions", font_size=24, color=GREEN).to_edge(DOWN)
        self.play(Write(explanation))
        
        # Show that lines C and D were idle
        cross_c = Line(line_c.get_start(), line_c.get_end(), color=RED).scale(0.2)
        cross_d = Line(line_d.get_start(), line_d.get_end(), color=RED).scale(0.2)
        idle_text = Text("IDLE", font_size=16, color=WHITE).next_to(line_c, UP, buff=0.1)
        
        self.play(FadeIn(idle_text))
        self.wait(2)

        # Cleanup
        self.play(
            FadeOut(data_frame),
            FadeOut(explanation),
            FadeOut(switch_group),
            FadeOut(nodes),
            FadeOut(lines),
            FadeOut(mac_table),
            FadeOut(title),
            FadeOut(idle_text)
        )