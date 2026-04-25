from manim import *

class Scene2(Scene):
    def construct(self):
        # Title and Concept Labels
        title = Text("Intelligent Data Forwarding: The Switch", font_size=36, color=BLUE).to_edge(UP)
        explanation = Text("MAC Address Filtering & Dedicated Paths", font_size=24, color=GOLD).next_to(title, DOWN)
        
        # Central Switch Representation
        switch_body = Rectangle(width=5, height=3, color=WHITE, fill_opacity=0.1)
        switch_label = Text("Network Switch", font_size=24).next_to(switch_body, UP, buff=0.1)
        
        # Internal MAC Table
        mac_table_box = Rectangle(width=2.5, height=1.5, color=TEAL, fill_opacity=0.2).move_to(switch_body.get_center())
        mac_title = Text("Address Table", font_size=16, color=TEAL).next_to(mac_table_box, UP, buff=0.05)
        mac_entry = Text("Port 3 -> PC C", font_size=20, color=WHITE).move_to(mac_table_box.get_center())
        mac_table = VGroup(mac_table_box, mac_title, mac_entry)
        
        # Connected Nodes (PCs)
        pc_a = Square(side_length=0.8, color=WHITE, fill_opacity=0.3).shift(LEFT * 5 + UP * 1.5)
        pc_b = Square(side_length=0.8, color=WHITE, fill_opacity=0.3).shift(LEFT * 5 + DOWN * 1.5)
        pc_c = Square(side_length=0.8, color=GREEN, fill_opacity=0.3).shift(RIGHT * 5)
        
        label_a = Text("PC A", font_size=20).next_to(pc_a, LEFT)
        label_b = Text("PC B", font_size=20).next_to(pc_b, LEFT)
        label_c = Text("PC C", font_size=20).next_to(pc_c, RIGHT)
        
        # Lines representing cables
        line_a = Line(pc_a.get_right(), switch_body.get_left() + UP * 0.8, color=GRAY)
        line_b = Line(pc_b.get_right(), switch_body.get_left() + DOWN * 0.8, color=GRAY)
        line_c = Line(switch_body.get_right(), pc_c.get_left(), color=GRAY)
        
        # Ports
        port1 = Circle(radius=0.1, color=WHITE, fill_opacity=1).move_to(line_a.get_end())
        port2 = Circle(radius=0.1, color=WHITE, fill_opacity=1).move_to(line_b.get_end())
        port3 = Circle(radius=0.1, color=GREEN, fill_opacity=1).move_to(line_c.get_start())
        ports = VGroup(port1, port2, port3)

        # Build Scene
        main_group = VGroup(switch_body, switch_label, mac_table, pc_a, pc_b, pc_c, label_a, label_b, label_c, line_a, line_b, line_c, ports)
        self.play(Write(title))
        self.play(Create(main_group))
        self.play(Write(explanation))
        self.wait(1)

        # Data Frame Animation
        frame = Dot(color=RED, radius=0.15)
        frame.move_to(pc_a.get_center())
        frame_tag = Text("Target: PC C", font_size=18, color=RED).next_to(frame, UP)
        
        # 1. Frame moves to Switch
        self.play(
            frame.animate.move_to(port1.get_center()),
            frame_tag.animate.next_to(port1, UP),
            run_time=1.5
        )
        
        # 2. Table Lookup (Highlighting logic)
        lookup_rect = Rectangle(width=2.6, height=1.6, color=YELLOW).move_to(mac_table_box)
        self.play(Create(lookup_rect))
        self.play(mac_entry.animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(FadeOut(lookup_rect))
        
        # 3. Direct Forwarding (Avoiding PC B)
        status_text = Text("Directing only to Port 3...", font_size=22, color=YELLOW).to_edge(DOWN)
        self.play(Write(status_text))
        
        # Move frame to destination, bypassing other ports
        self.play(
            frame.animate.move_to(port3.get_center()),
            frame_tag.animate.next_to(port3, UP),
            run_time=1
        )
        self.play(
            frame.animate.move_to(pc_c.get_center()),
            frame_tag.animate.next_to(pc_c, UP),
            run_time=1
        )
        
        # Success state
        success_label = Text("No Collision - Data Delivered", font_size=24, color=GREEN).to_edge(DOWN)
        self.play(Transform(status_text, success_label))
        self.play(pc_c.animate.set_fill(GREEN, fill_opacity=0.8))
        
        self.wait(2)