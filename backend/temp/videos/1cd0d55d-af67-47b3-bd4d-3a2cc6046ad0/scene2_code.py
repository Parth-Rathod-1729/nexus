from manim import *

class Scene2(Scene):
    def construct(self):
        # 1. Setup Title
        title = Text("Layer 2: Bridges and Switches", color=BLUE, font_size=32).to_edge(UP)
        explanation = Text("MAC Address Filtering", color=WHITE, font_size=20).next_to(title, DOWN)
        
        # 2. Create Network Components
        switch = Rectangle(width=2.5, height=1.2, color=TEAL, fill_opacity=0.3).move_to(ORIGIN)
        switch_label = Text("Switch", font_size=24).move_to(switch.get_center())
        
        pc_a = Square(side_length=0.8, color=WHITE).shift(LEFT * 4.5)
        pc_b = Square(side_length=0.8, color=WHITE).shift(RIGHT * 4.5 + UP * 1.5)
        pc_c = Square(side_length=0.8, color=WHITE).shift(RIGHT * 4.5 + DOWN * 1.5)
        
        label_a = Text("PC A (MAC: AA)", font_size=16).next_to(pc_a, UP)
        label_b = Text("PC B (MAC: BB)", font_size=16).next_to(pc_b, UP)
        label_c = Text("PC C (MAC: CC)", font_size=16).next_to(pc_c, DOWN)
        
        line_a = Line(pc_a.get_right(), switch.get_left(), color=WHITE)
        line_b = Line(switch.get_right(), pc_b.get_left(), color=WHITE)
        line_c = Line(switch.get_right(), pc_c.get_left(), color=WHITE)
        
        network = VGroup(switch, switch_label, pc_a, pc_b, pc_c, label_a, label_b, label_c, line_a, line_b, line_c)
        
        # 3. Create MAC Address Table
        table_rect = Rectangle(width=3.5, height=2.0, color=GOLD, fill_opacity=0.1).to_corner(DL, buff=0.5)
        table_header = Text("Switch MAC Table", font_size=18, color=GOLD).next_to(table_rect, UP, buff=0.1)
        row1 = Text("Port 1: AA", font_size=16).move_to(table_rect.get_center() + UP * 0.4)
        row2 = Text("Port 2: BB", font_size=16).move_to(table_rect.get_center())
        row3 = Text("Port 3: CC", font_size=16).move_to(table_rect.get_center() + DOWN * 0.4)
        
        mac_table = VGroup(table_rect, table_header, row1, row2, row3)
        
        # 4. Animations
        self.play(Write(title), Write(explanation))
        self.play(Create(network))
        self.play(Create(mac_table))
        self.wait(1)
        
        # 5. Data Transfer Animation
        # Data Packet
        packet = Circle(radius=0.15, color=YELLOW, fill_opacity=1)
        packet_label = Text("To: BB", font_size=14, color=BLACK).move_to(packet.get_center())
        data_frame = VGroup(packet, packet_label).move_to(pc_a.get_center())
        
        # PC A to Switch
        self.play(data_frame.animate.move_to(switch.get_center()), run_time=2)
        
        # Switch logic: Highlight table row
        highlight = Rectangle(width=3.3, height=0.35, color=YELLOW, fill_opacity=0.3).move_to(row2.get_center())
        self.play(Create(highlight))
        self.wait(1)
        
        # Switch to PC B (Intelligent forwarding)
        self.play(
            data_frame.animate.move_to(pc_b.get_center()),
            line_b.animate.set_color(YELLOW),
            run_time=2
        )
        
        # Confirming PC C received nothing
        no_entry = Text("Filtered", font_size=14, color=RED).next_to(line_c, DOWN, buff=0.1)
        self.play(Write(no_entry))
        self.wait(2)
        
        # Cleanup and finish
        self.play(
            FadeOut(data_frame),
            FadeOut(highlight),
            FadeOut(no_entry),
            line_b.animate.set_color(WHITE)
        )
        self.wait(1)
        self.play(FadeOut(network), FadeOut(mac_table), FadeOut(title), FadeOut(explanation))
        self.wait(1)