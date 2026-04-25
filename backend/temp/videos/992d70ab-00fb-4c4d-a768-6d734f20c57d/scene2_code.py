from manim import *

class Scene2(Scene):
    def construct(self):
        # Title and Central Switch
        title = Text("MAC Address Filtering", color=WHITE).scale(0.8).to_edge(UP)
        switch_rect = Rectangle(width=3.5, height=2.2, color=BLUE, fill_opacity=0.2).move_to(ORIGIN)
        switch_text = Text("Switch", color=BLUE).scale(0.7).next_to(switch_rect, UP, buff=0.1)
        
        # MAC Table Construction
        table_bg = Rectangle(width=2.8, height=2.2, color=GOLD, fill_opacity=0.1).to_edge(LEFT, buff=0.5)
        table_title = Text("MAC Table", color=GOLD).scale(0.5).next_to(table_bg, UP, buff=0.1)
        row1 = Text("AA:11 -> Port 1", color=WHITE).scale(0.4)
        row2 = Text("BB:22 -> Port 2", color=WHITE).scale(0.4)
        row3 = Text("CC:33 -> Port 3", color=WHITE).scale(0.4)
        table_rows = VGroup(row1, row2, row3).arrange(DOWN, buff=0.3).move_to(table_bg.get_center())
        mac_table = VGroup(table_bg, table_title, table_rows)

        # Port Connections (Right side)
        p1_circle = Circle(radius=0.3, color=WHITE, fill_opacity=0.1).move_to(RIGHT*4 + UP*1.5)
        p2_circle = Circle(radius=0.3, color=WHITE, fill_opacity=0.1).move_to(RIGHT*4 + ORIGIN)
        p3_circle = Circle(radius=0.3, color=WHITE, fill_opacity=0.1).move_to(RIGHT*4 + DOWN*1.5)
        
        label1 = Text("Port 1 (A)", color=WHITE).scale(0.4).next_to(p1_circle, RIGHT)
        label2 = Text("Port 2 (B)", color=WHITE).scale(0.4).next_to(p2_circle, RIGHT)
        label3 = Text("Port 3 (C)", color=WHITE).scale(0.4).next_to(p3_circle, RIGHT)

        line1 = Line(switch_rect.get_right(), p1_circle.get_left(), color=WHITE)
        line2 = Line(switch_rect.get_right(), p2_circle.get_left(), color=WHITE)
        line3 = Line(switch_rect.get_right(), p3_circle.get_left(), color=WHITE)

        all_ports = VGroup(p1_circle, p2_circle, p3_circle, label1, label2, label3, line1, line2, line3)

        # Setup Scene
        self.play(Write(title))
        self.play(Create(switch_rect), Write(switch_text))
        self.play(Create(mac_table), Create(all_ports))
        self.wait(1)

        # Incoming Data Packet
        packet = Square(side_length=0.4, color=RED, fill_opacity=1).move_to(DOWN*3.5)
        packet_label = Text("Dest: BB:22", color=RED).scale(0.3).next_to(packet, DOWN)
        packet_group = VGroup(packet, packet_label)

        # Animation: Packet arrives at switch
        self.play(packet_group.animate.move_to(switch_rect.get_center()), run_time=1.5)
        
        # Animation: Table Lookup
        highlight_box = Rectangle(width=2.6, height=0.4, color=YELLOW, fill_opacity=0.3).move_to(row2.get_center())
        self.play(Create(highlight_box))
        self.play(row2.animate.set_color(YELLOW))
        self.wait(1)

        # Animation: Direct Routing
        self.play(
            packet_group.animate.move_to(p2_circle.get_center()),
            FadeOut(highlight_box),
            run_time=1.5
        )
        
        # Confirmation text
        efficiency_text = Text("Data sent only to Port 2", color=GREEN).scale(0.6).to_edge(DOWN, buff=1)
        self.play(Write(efficiency_text))
        self.play(p2_circle.animate.set_fill(GREEN, fill_opacity=0.5))
        
        self.wait(2)

        # Clean up
        self.play(
            FadeOut(packet_group),
            FadeOut(switch_rect),
            FadeOut(switch_text),
            FadeOut(mac_table),
            FadeOut(all_ports),
            FadeOut(efficiency_text),
            FadeOut(title)
        )