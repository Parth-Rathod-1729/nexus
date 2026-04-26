from manim import *

class Scene2(Scene):
    def construct(self):
        # Title
        title = Text("Filtering with Bridges and Switches", color=BLUE).scale(0.8)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Bridge Section
        bridge_rect = Rectangle(width=3, height=1.5, color=BLUE, fill_opacity=0.3)
        bridge_label = Text("Bridge", color=WHITE).scale(0.6).move_to(bridge_rect.get_center())
        bridge_group = VGroup(bridge_rect, bridge_label).move_to(ORIGIN)
        
        packet_rect = Rectangle(width=2, height=0.8, color=YELLOW, fill_opacity=0.5)
        packet_text = Text("Dest: MAC A", color=BLACK).scale(0.4).move_to(packet_rect.get_center())
        packet = VGroup(packet_rect, packet_text).shift(LEFT * 5)
        
        table_rect = Rectangle(width=2.5, height=1.5, color=GOLD, fill_opacity=0.2)
        table_title = Text("Lookup Table", color=GOLD).scale(0.4).next_to(table_rect.get_top(), DOWN)
        table_entry = Text("MAC A -> Seg 2", color=WHITE).scale(0.4).next_to(table_title, DOWN)
        table = VGroup(table_rect, table_title, table_entry).next_to(bridge_group, UP, buff=0.5)

        self.play(Create(bridge_group))
        self.play(packet.animate.next_to(bridge_group, LEFT))
        self.play(Create(table))
        self.wait(1)
        self.play(packet.animate.shift(RIGHT * 6), FadeOut(table))
        self.play(FadeOut(bridge_group), FadeOut(packet))

        # Switch Section
        switch_body = Rectangle(width=4, height=2.5, color=TEAL, fill_opacity=0.2)
        switch_label = Text("Switch", color=TEAL).scale(0.7).next_to(switch_body.get_top(), DOWN)
        
        # Ports
        port_in = Square(side_length=0.5, color=WHITE).next_to(switch_body.get_left(), RIGHT, buff=0)
        port_out1 = Square(side_length=0.5, color=WHITE).move_to(switch_body.get_right() + UP * 0.7 + LEFT * 0.25)
        port_out2 = Square(side_length=0.5, color=WHITE).move_to(switch_body.get_right() + DOWN * 0.7 + LEFT * 0.25)
        
        port_label1 = Text("Port 1", color=WHITE).scale(0.3).next_to(port_out1, LEFT, buff=0.1)
        port_label2 = Text("Port 2", color=WHITE).scale(0.3).next_to(port_out2, LEFT, buff=0.1)
        
        switch_group = VGroup(switch_body, switch_label, port_in, port_out1, port_out2, port_label1, port_label2).move_to(ORIGIN)
        
        # Buffer
        buffer_circle = Circle(radius=0.4, color=RED, fill_opacity=0.4).move_to(switch_body.get_center())
        buffer_text = Text("Buffer", color=WHITE).scale(0.3).move_to(buffer_circle.get_center())
        buffer_group = VGroup(buffer_circle, buffer_text)

        self.play(Create(switch_group))
        self.wait(1)

        # Packet movement in Switch
        packet_small = Rectangle(width=1, height=0.5, color=YELLOW, fill_opacity=0.6).shift(LEFT * 5)
        self.play(packet_small.animate.move_to(port_in.get_center()))
        self.play(Create(buffer_group))
        self.play(packet_small.animate.move_to(buffer_circle.get_center()))
        self.wait(1)
        
        # Send to specific port
        arrow = Arrow(buffer_circle.get_right(), port_out2.get_left(), color=YELLOW)
        self.play(Create(arrow))
        self.play(packet_small.animate.move_to(port_out2.get_center()))
        self.play(packet_small.animate.shift(RIGHT * 3))
        
        # Cleanup
        self.play(
            FadeOut(switch_group),
            FadeOut(buffer_group),
            FadeOut(arrow),
            FadeOut(packet_small),
            FadeOut(title)
        )
        self.wait(1)