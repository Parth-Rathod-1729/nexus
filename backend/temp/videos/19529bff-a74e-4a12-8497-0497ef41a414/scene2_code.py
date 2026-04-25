from manim import *

class Scene2(Scene):
    def construct(self):
        # Title
        title = Text("Intelligent Switching: Data Link Layer", font_size=32, color=BLUE)
        title.to_edge(UP, buff=0.5)

        # Central Switch
        switch_box = Rectangle(width=3, height=1.5, color=WHITE, fill_opacity=0.2)
        switch_label = Text("Switch", font_size=24).move_to(switch_box.get_center())
        switch_group = VGroup(switch_box, switch_label).move_to(ORIGIN)

        # Devices
        dev_a = Circle(radius=0.4, color=GREEN, fill_opacity=0.3)
        dev_a_label = Text("MAC: A", font_size=18).next_to(dev_a, UP, buff=0.1)
        node_a = VGroup(dev_a, dev_a_label).move_to(LEFT * 4 + UP * 1.5)

        dev_b = Circle(radius=0.4, color=GREEN, fill_opacity=0.3)
        dev_b_label = Text("MAC: B", font_size=18).next_to(dev_b, DOWN, buff=0.1)
        node_b = VGroup(dev_b, dev_b_label).move_to(LEFT * 4 + DOWN * 1.5)

        dev_c = Circle(radius=0.4, color=TEAL, fill_opacity=0.3)
        dev_c_label = Text("MAC: C", font_size=18).next_to(dev_c, UP, buff=0.1)
        node_c = VGroup(dev_c, dev_c_label).move_to(RIGHT * 4 + UP * 1.5)

        dev_d = Circle(radius=0.4, color=TEAL, fill_opacity=0.3)
        dev_d_label = Text("MAC: D", font_size=18).next_to(dev_d, DOWN, buff=0.1)
        node_d = VGroup(dev_d, dev_d_label).move_to(RIGHT * 4 + DOWN * 1.5)

        # Connections
        line_a = Line(node_a.get_center(), switch_group.get_left(), color=GRAY)
        line_b = Line(node_b.get_center(), switch_group.get_left(), color=GRAY)
        line_c = Line(node_c.get_center(), switch_group.get_right(), color=GRAY)
        line_d = Line(node_d.get_center(), switch_group.get_right(), color=GRAY)
        lines = VGroup(line_a, line_b, line_c, line_d)

        # MAC Lookup Table
        table_rect = Rectangle(width=2.5, height=2.2, color=YELLOW, fill_opacity=0.1)
        table_rect.to_edge(RIGHT, buff=0.2).shift(DOWN * 0.5)
        table_title = Text("MAC Table", font_size=20, color=YELLOW).next_to(table_rect, UP, buff=0.1)
        entry_a = Text("A -> Port 1", font_size=16).move_to(table_rect.get_center() + UP * 0.6)
        entry_b = Text("B -> Port 2", font_size=16).next_to(entry_a, DOWN, buff=0.2)
        entry_c = Text("C -> Port 3", font_size=16).next_to(entry_b, DOWN, buff=0.2)
        entry_d = Text("D -> Port 4", font_size=16).next_to(entry_c, DOWN, buff=0.2)
        mac_table = VGroup(table_rect, table_title, entry_a, entry_b, entry_c, entry_d)

        # Animation Sequence
        self.play(Write(title))
        self.play(Create(switch_group), Create(lines))
        self.play(Create(VGroup(node_a, node_b, node_c, node_d)))
        self.play(Create(mac_table))
        self.wait(1)

        # Packet Transmission Simulation
        packet = Dot(color=RED, radius=0.12)
        packet.move_to(node_a.get_center())
        
        # 1. Packet from A to Switch
        self.play(packet.animate.move_to(switch_group.get_center()), run_time=1.5)
        
        # 2. Switch Look-up: Highlight Entry C
        highlight_box = Rectangle(width=2.3, height=0.3, color=GOLD).move_to(entry_c.get_center())
        self.play(Create(highlight_box))
        self.wait(0.5)
        
        # 3. Dedicated Transmission: Only to C
        # Show that other lines are NOT used (visualized by line colors staying gray)
        self.play(line_c.animate.set_color(GOLD), run_time=0.5)
        self.play(packet.animate.move_to(node_c.get_center()), run_time=1.5)
        
        # Explanation Text
        explanation = Text("Collision Domain Segmented", font_size=24, color=GOLD)
        explanation.next_to(switch_group, DOWN, buff=1)
        self.play(Write(explanation))
        
        # Final State
        self.play(FadeOut(packet), line_c.animate.set_color(GRAY), FadeOut(highlight_box))
        self.wait(2)

        # Cleanup
        self.play(
            FadeOut(title),
            FadeOut(switch_group),
            FadeOut(lines),
            FadeOut(node_a), FadeOut(node_b), FadeOut(node_c), FadeOut(node_d),
            FadeOut(mac_table),
            FadeOut(explanation)
        )