from manim import *

class Scene2(Scene):
    def construct(self):
        # Title and labels
        title = Text("Intelligent Forwarding: Bridges and Switches", font_size=30, color=TEAL).to_edge(UP)
        explanation = Text("Filtering data using MAC addresses", font_size=18, color=WHITE).next_to(title, DOWN)
        
        # Central Switch
        switch_box = Rectangle(width=3, height=1.5, color=BLUE, fill_opacity=0.3)
        switch_label = Text("Switch", font_size=24).move_to(switch_box.get_center())
        switch_group = VGroup(switch_box, switch_label).shift(DOWN * 0.5)

        # MAC Address Table (Directory)
        table_rect = Rectangle(width=2.5, height=2, color=GOLD, fill_opacity=0.1).to_edge(RIGHT, buff=1).shift(UP * 0.5)
        table_title = Text("MAC Table", font_size=18).next_to(table_rect, UP, buff=0.1)
        row1 = Text("A -> P1", font_size=18, color=WHITE).move_to(table_rect.get_top() + DOWN * 0.4)
        row2 = Text("B -> P2", font_size=18, color=WHITE).move_to(table_rect.get_center())
        row3 = Text("C -> P3", font_size=18, color=WHITE).move_to(table_rect.get_bottom() + UP * 0.4)
        mac_table = VGroup(table_rect, table_title, row1, row2, row3)

        # Connected Devices (Ports)
        node_a = Circle(radius=0.3, color=WHITE).next_to(switch_box, LEFT, buff=1.5)
        node_b = Circle(radius=0.3, color=WHITE).next_to(switch_box, RIGHT, buff=1.5)
        node_c = Circle(radius=0.3, color=WHITE).next_to(switch_box, DOWN, buff=1)
        
        label_a = Text("A", font_size=20).next_to(node_a, LEFT)
        label_b = Text("B", font_size=20).next_to(node_b, RIGHT)
        label_c = Text("C", font_size=20).next_to(node_c, DOWN)

        line_a = Line(node_a.get_right(), switch_box.get_left(), color=WHITE)
        line_b = Line(switch_box.get_right(), node_b.get_left(), color=WHITE)
        line_c = Line(switch_box.get_bottom(), node_c.get_top(), color=WHITE)

        # Initial layout presentation
        self.play(Write(title), Write(explanation))
        self.play(Create(switch_group), Create(mac_table))
        self.play(
            Create(node_a), Write(label_a), Create(line_a),
            Create(node_b), Write(label_b), Create(line_b),
            Create(node_c), Write(label_c), Create(line_c)
        )
        self.wait(1)

        # Data Frame entering from Node A
        frame_rect = Rectangle(width=0.5, height=0.3, color=GREEN, fill_opacity=1)
        frame_text = Text("Data", font_size=12).move_to(frame_rect.get_center())
        frame = VGroup(frame_rect, frame_text).move_to(node_a.get_center())

        # Step 1: Frame to Switch
        self.play(frame.animate.move_to(switch_box.get_center()), run_time=1.5)
        
        # Step 2: Highlight Destination B in MAC Table
        highlight = Rectangle(width=2.3, height=0.4, color=YELLOW, fill_opacity=0.2).move_to(row2.get_center())
        self.play(Create(highlight))
        self.wait(1)

        # Step 3: Forward Frame to B, ignoring C
        dest_arrow = Arrow(switch_box.get_center(), node_b.get_center(), color=YELLOW, buff=0.1)
        self.play(Create(dest_arrow))
        self.play(frame.animate.move_to(node_b.get_center()), run_time=1.5)
        
        # Idle state for C
        idle_text = Text("Idle", font_size=16, color=RED).next_to(node_c, RIGHT)
        self.play(Write(idle_text))
        
        self.wait(2)