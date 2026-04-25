from manim import *

class Scene2(Scene):
    def construct(self):
        # 1. Background Switch and Devices
        switch_box = Rectangle(width=4, height=2.5, color=BLUE, fill_opacity=0.2)
        switch_label = Text("Switch", font_size=28).move_to(switch_box.get_top() + DOWN * 0.4)
        switch = VGroup(switch_box, switch_label)

        # 2. Devices (A, B, C, D)
        node_a = VGroup(Circle(radius=0.4, color=TEAL, fill_opacity=0.6), Text("A", font_size=20)).shift(LEFT * 5 + UP * 1.5)
        node_b = VGroup(Circle(radius=0.4, color=TEAL, fill_opacity=0.6), Text("B", font_size=20)).shift(LEFT * 5 + DOWN * 1.5)
        node_c = VGroup(Circle(radius=0.4, color=GREEN, fill_opacity=0.6), Text("C", font_size=20)).shift(RIGHT * 5 + UP * 1.5)
        node_d = VGroup(Circle(radius=0.4, color=TEAL, fill_opacity=0.6), Text("D", font_size=20)).shift(RIGHT * 5 + DOWN * 1.5)

        # Connections
        line_a = Line(node_a.get_right(), switch_box.get_left() + UP * 0.5, color=WHITE)
        line_b = Line(node_b.get_right(), switch_box.get_left() + DOWN * 0.5, color=WHITE)
        line_c = Line(node_c.get_left(), switch_box.get_right() + UP * 0.5, color=WHITE)
        line_d = Line(node_d.get_left(), switch_box.get_right() + DOWN * 0.5, color=WHITE)
        connections = VGroup(line_a, line_b, line_c, line_d)

        # 3. MAC Address Table
        table_rect = Rectangle(width=3, height=1.2, color=GOLD, fill_opacity=0.1).to_edge(UP, buff=0.2)
        table_title = Text("MAC Address Table", font_size=18).next_to(table_rect, UP, buff=0.1)
        entry_a = Text("A -> Port 1", font_size=16).move_to(table_rect.get_center() + UP * 0.2)
        entry_c = Text("C -> Port 3", font_size=16).move_to(table_rect.get_center() + DOWN * 0.2)
        mac_table = VGroup(table_rect, table_title, entry_a, entry_c)

        # 4. Data Frame
        frame_box = Square(side_length=0.4, color=RED, fill_opacity=0.9)
        frame_text = Text("Dest: C", font_size=12).move_to(frame_box)
        frame = VGroup(frame_box, frame_text).move_to(node_a.get_center())

        # --- Animations ---
        self.play(Create(switch), Create(node_a), Create(node_b), Create(node_c), Create(node_d))
        self.play(Create(connections))
        self.play(Create(mac_table))
        self.wait(1)

        # Frame moves from A to Switch
        self.play(frame.animate.move_to(switch_box.get_center()), run_time=1.5)
        
        # Switch looks up Destination C in the table
        highlight = Rectangle(width=2.8, height=0.3, color=YELLOW).move_to(entry_c)
        self.play(Create(highlight))
        self.play(entry_c.animate.set_color(YELLOW))
        self.wait(1)

        # Frame moves exclusively to C
        self.play(
            frame.animate.move_to(node_c.get_center()),
            FadeOut(highlight),
            run_time=1.5
        )

        # Final explanation visual
        efficiency_text = Text("Direct Forwarding: No Collisions", font_size=24, color=YELLOW).to_edge(DOWN)
        self.play(Write(efficiency_text))
        self.wait(2)

        # End of Scene
        self.play(FadeOut(VGroup(switch, node_a, node_b, node_c, node_d, connections, mac_table, frame, efficiency_text)))

# End of code.