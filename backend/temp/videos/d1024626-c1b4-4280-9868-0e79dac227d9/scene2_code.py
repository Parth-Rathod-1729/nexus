from manim import *

class Scene2(Scene):
    def construct(self):
        # Title and labels
        title = Text("Layer 2 Intelligence: Switches", font_size=32, color=BLUE).to_edge(UP)
        explanation = Text("MAC-Based Filtering and Dedicated Bandwidth", font_size=22).next_to(title, DOWN)
        
        # Central Switch representation
        switch_body = Rectangle(width=3, height=1.5, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        switch_label = Text("SWITCH", font_size=24, weight=BOLD).move_to(switch_body.get_center())
        switch_group = VGroup(switch_body, switch_label)
        
        # MAC Address Table
        table_rect = Rectangle(width=2.5, height=1.2, color=GOLD).to_edge(RIGHT, buff=1)
        table_header = Text("MAC Table", font_size=18, color=GOLD).next_to(table_rect, UP, buff=0.1)
        table_entry1 = Text("Port 1: MAC_A", font_size=14).move_to(table_rect.get_center() + UP * 0.2)
        table_entry2 = Text("Port 3: MAC_C", font_size=14).move_to(table_rect.get_center() + DOWN * 0.2)
        table_group = VGroup(table_rect, table_header, table_entry1, table_entry2)

        # Connected Devices
        pc_a = VGroup(Circle(radius=0.4, color=WHITE), Text("A", font_size=20)).shift(LEFT * 5 + UP * 1.5)
        pc_b = VGroup(Circle(radius=0.4, color=WHITE), Text("B", font_size=20)).shift(LEFT * 5 + DOWN * 1.5)
        pc_c = VGroup(Circle(radius=0.4, color=WHITE), Text("C", font_size=20)).shift(RIGHT * 5)
        
        # Physical connections
        link_a = Line(pc_a.get_right(), switch_body.get_left(), color=WHITE)
        link_b = Line(pc_b.get_right(), switch_body.get_left(), color=WHITE)
        link_c = Line(pc_c.get_left(), switch_body.get_right(), color=WHITE)
        links = VGroup(link_a, link_b, link_c)

        # Initial display
        self.play(Write(title), Write(explanation))
        self.play(Create(switch_group), Create(links), Create(pc_a), Create(pc_b), Create(pc_c))
        self.play(Create(table_group))
        self.wait(1)

        # Data Frame animation
        packet = Square(side_length=0.3, fill_color=YELLOW, fill_opacity=1, color=YELLOW)
        packet_label = Text("Frame", font_size=12, color=BLACK).move_to(packet)
        frame = VGroup(packet, packet_label).move_to(pc_a.get_center())

        # Step 1: PC A sends to PC C
        dest_text = Text("To: MAC_C", font_size=16, color=YELLOW).next_to(pc_a, UP)
        self.play(Write(dest_text))
        self.play(frame.animate.move_to(switch_body.get_center()), run_time=1.5)
        
        # Step 2: Switch look-up
        highlight = Rectangle(width=2.4, height=0.3, color=RED).move_to(table_entry2.get_center())
        self.play(Create(highlight))
        self.wait(0.5)

        # Step 3: Direct delivery to C (ignoring B)
        self.play(
            frame.animate.move_to(pc_c.get_center()),
            FadeOut(dest_text),
            Uncreate(highlight),
            run_time=1.5
        )

        # Explanation logic
        efficiency_text = Text("Direct delivery = No collisions", font_size=24, color=TEAL).to_edge(DOWN, buff=1)
        self.play(Write(efficiency_text))
        self.wait(2)

        # Final cleanup
        self.play(
            FadeOut(switch_group),
            FadeOut(table_group),
            FadeOut(links),
            FadeOut(pc_a),
            FadeOut(pc_b),
            FadeOut(pc_c),
            FadeOut(frame),
            FadeOut(efficiency_text),
            FadeOut(title),
            FadeOut(explanation)
        )