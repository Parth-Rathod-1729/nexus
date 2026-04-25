from manim import *

class Scene2(Scene):
    def construct(self):
        # Title
        title = Text("MAC Address Filtering & Unicasting", font_size=32, color=WHITE).to_edge(UP)
        self.add(title)

        # Central Switch
        switch_body = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.3)
        switch_label = Text("Network Switch", font_size=24).move_to(switch_body.get_center())
        switch = VGroup(switch_body, switch_label).move_to(ORIGIN)

        # Address Directory Table
        table_box = Rectangle(width=3, height=2.5, color=TEAL, fill_opacity=0.1).to_edge(RIGHT, buff=0.5)
        table_title = Text("Address Directory", font_size=20, color=TEAL).next_to(table_box, UP, buff=0.1)
        row1 = Text("MAC A: Port 1", font_size=18).move_to(table_box.get_top() + DOWN * 0.5)
        row2 = Text("MAC B: Port 2", font_size=18, color=YELLOW).next_to(row1, DOWN, buff=0.3)
        row3 = Text("MAC C: Port 3", font_size=18).next_to(row2, DOWN, buff=0.3)
        mac_table = VGroup(table_box, table_title, row1, row2, row3)

        # Nodes (Devices)
        node_a = Circle(radius=0.4, color=WHITE, fill_opacity=0.5).move_to(LEFT * 5 + UP * 1.5)
        label_a = Text("A", font_size=20).move_to(node_a.get_center())
        node_b = Circle(radius=0.4, color=WHITE, fill_opacity=0.5).move_to(RIGHT * 3 + DOWN * 2)
        label_b = Text("B", font_size=20).move_to(node_b.get_center())
        node_c = Circle(radius=0.4, color=WHITE, fill_opacity=0.5).move_to(LEFT * 5 + DOWN * 1.5)
        label_c = Text("C", font_size=20).move_to(node_c.get_center())
        
        nodes = VGroup(node_a, label_a, node_b, label_b, node_c, label_c)

        # Connections
        line_a = Line(node_a.get_right(), switch_body.get_left(), color=WHITE)
        line_b = Line(node_b.get_top(), switch_body.get_bottom(), color=WHITE)
        line_c = Line(node_c.get_right(), switch_body.get_left() + DOWN * 0.5, color=WHITE)
        lines = VGroup(line_a, line_b, line_c)

        # Scene Intro
        self.play(Create(switch), Create(nodes), Create(lines))
        self.play(Write(mac_table))
        self.wait(1)

        # Data Frame
        frame_rect = Rectangle(width=0.8, height=0.5, color=GOLD, fill_opacity=1.0)
        frame_text = Text("To: B", font_size=16, color=BLACK).move_to(frame_rect.get_center())
        data_frame = VGroup(frame_rect, frame_text).move_to(node_a.get_center())

        # Step 1: Send to Switch
        self.play(data_frame.animate.move_to(switch_body.get_center()), run_time=2)
        
        # Step 2: Switch looks up table
        self.play(row2.animate.scale(1.2).set_color(GOLD))
        self.wait(0.5)

        # Step 3: Forwarding to specific port only
        # Highlight destination line
        self.play(line_b.animate.set_stroke(YELLOW, width=6))
        self.play(data_frame.animate.move_to(node_b.get_center()), run_time=2)
        
        # Step 4: Final explanation text
        efficiency_text = Text("Unicasting: Data sent only to destination.", font_size=20, color=GREEN).to_edge(DOWN)
        self.play(Write(efficiency_text))
        self.wait(2)

        # Cleanup
        self.play(FadeOut(data_frame), FadeOut(nodes), FadeOut(switch), FadeOut(mac_table), FadeOut(lines), FadeOut(efficiency_text), FadeOut(title))