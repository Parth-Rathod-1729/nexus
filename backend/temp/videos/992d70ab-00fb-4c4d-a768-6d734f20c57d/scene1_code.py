from manim import *

class Scene1(Scene):
    def construct(self):
        # Title
        title = Text("Physical Layer: Repeaters and Hubs", color=BLUE, font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # --- REPEATER SECTION ---
        repeater_label = Text("Repeater: Signal Regeneration", color=YELLOW, font_size=28)
        repeater_label.next_to(title, DOWN, buff=0.5)
        
        repeater_box = Rectangle(width=3, height=1.5, color=GOLD, fill_opacity=0.2)
        repeater_text = Text("Repeater", font_size=24).move_to(repeater_box.get_center())
        repeater_group = VGroup(repeater_box, repeater_text).move_to(ORIGIN)

        # Signals
        weak_signal = VGroup(
            Line(LEFT * 5, LEFT * 4, color=RED, stroke_width=2),
            Line(LEFT * 4, LEFT * 3.5, color=RED, stroke_width=1),
            Line(LEFT * 3.5, LEFT * 2, color=RED, stroke_width=0.5)
        )
        weak_label = Text("Weak Signal", color=RED, font_size=20).next_to(weak_signal, UP)
        
        strong_signal_arrow = Arrow(start=RIGHT * 1.5, end=RIGHT * 5, color=GREEN, stroke_width=8)
        strong_label = Text("Regenerated Signal", color=GREEN, font_size=20).next_to(strong_signal_arrow, UP)

        self.play(Create(repeater_group), Write(repeater_label))
        self.play(Create(weak_signal), Write(weak_label))
        self.wait(1)
        
        self.play(
            weak_signal.animate.move_to(repeater_box.get_center()).set_opacity(0),
            FadeOut(weak_label),
            run_time=1.5
        )
        self.play(GrowArrow(strong_signal_arrow), Write(strong_label))
        self.wait(2)

        # Clear Repeater Section
        self.play(
            FadeOut(repeater_group), 
            FadeOut(repeater_label), 
            FadeOut(strong_signal_arrow), 
            FadeOut(strong_label)
        )

        # --- HUB SECTION ---
        hub_label = Text("Hub: Multi-port Broadcast", color=TEAL, font_size=28)
        hub_label.next_to(title, DOWN, buff=0.5)

        hub_box = Square(side_length=1.5, color=TEAL, fill_opacity=0.3)
        hub_text = Text("Hub", font_size=24).move_to(hub_box.get_center())
        hub_group = VGroup(hub_box, hub_text).move_to(ORIGIN)

        # Devices
        d1 = Circle(radius=0.3, color=WHITE).move_to(UP * 2.5 + LEFT * 2)
        d2 = Circle(radius=0.3, color=WHITE).move_to(UP * 2.5 + RIGHT * 2)
        d3 = Circle(radius=0.3, color=WHITE).move_to(DOWN * 2 + LEFT * 2)
        d4 = Circle(radius=0.3, color=WHITE).move_to(DOWN * 2 + RIGHT * 2)
        devices = VGroup(d1, d2, d3, d4)
        
        # Connections
        c1 = Line(hub_box.get_corner(UL), d1.get_center(), color=GRAY)
        c2 = Line(hub_box.get_corner(UR), d2.get_center(), color=GRAY)
        c3 = Line(hub_box.get_corner(DL), d3.get_center(), color=GRAY)
        c4 = Line(hub_box.get_corner(DR), d4.get_center(), color=GRAY)
        connections = VGroup(c1, c2, c3, c4)

        self.play(Create(hub_group), Write(hub_label))
        self.play(Create(devices), Create(connections))
        self.wait(1)

        # Packet movement
        input_packet = Dot(color=YELLOW).move_to(LEFT * 5)
        self.play(input_packet.animate.move_to(hub_box.get_center()))
        
        # Broadcasting
        p1 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p2 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p3 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p4 = Dot(color=YELLOW).move_to(hub_box.get_center())
        
        broadcast_packets = VGroup(p1, p2, p3, p4)

        self.play(
            p1.animate.move_to(d1.get_center()),
            p2.animate.move_to(d2.get_center()),
            p3.animate.move_to(d3.get_center()),
            p4.animate.move_to(d4.get_center()),
            input_packet.animate.set_opacity(0),
            run_time=2
        )
        
        broadcast_text = Text("Broadcast to all ports", color=YELLOW, font_size=20).next_to(hub_box, DOWN, buff=0.8)
        self.play(Write(broadcast_text))
        self.wait(2)

        # Final Cleanup
        self.play(FadeOut(VGroup(hub_group, hub_label, devices, connections, broadcast_packets, broadcast_text, title)))
        self.wait(1)

# End of code