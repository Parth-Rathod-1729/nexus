from manim import *

class Scene1(Scene):
    def construct(self):
        # Title
        title = Text("Repeater & Hub: Signal Boosters", font_size=36, color=WHITE).to_edge(UP)
        self.play(Write(title))

        # --- REPEATER SECTION ---
        repeater_box = Rectangle(height=1.5, width=2.5, color=BLUE, fill_opacity=0.2)
        repeater_label = Text("Repeater", font_size=24).move_to(repeater_box.get_center())
        repeater_group = VGroup(repeater_box, repeater_label).shift(UP * 0.5)

        weak_signal_line = Line(LEFT * 5, LEFT * 1.25, color=RED, stroke_width=2).shift(UP * 0.5)
        weak_text = Text("Weak Signal", font_size=18, color=RED).next_to(weak_signal_line, UP)
        
        strong_signal_line = Line(RIGHT * 1.25, RIGHT * 5, color=GREEN, stroke_width=8).shift(UP * 0.5)
        strong_text = Text("Regenerated Signal", font_size=18, color=GREEN).next_to(strong_signal_line, UP)

        self.play(Create(repeater_group))
        self.play(Create(weak_signal_line), Write(weak_text))
        self.wait(1)
        self.play(Create(strong_signal_line), Write(strong_text))
        self.wait(2)

        # Clear Repeater Section
        self.play(FadeOut(repeater_group), FadeOut(weak_signal_line), FadeOut(weak_text), 
                  FadeOut(strong_signal_line), FadeOut(strong_text))

        # --- HUB SECTION ---
        hub_box = Square(side_length=1.5, color=GOLD, fill_opacity=0.3).shift(DOWN * 0.5)
        hub_label = Text("Hub", font_size=24).move_to(hub_box.get_center())
        hub_group = VGroup(hub_box, hub_label)

        # Connectors/Ports
        p1 = Square(side_length=0.6, color=TEAL).shift(UP * 1.5 + LEFT * 3)
        p2 = Square(side_length=0.6, color=TEAL).shift(UP * 1.5 + RIGHT * 3)
        p3 = Square(side_length=0.6, color=TEAL).shift(DOWN * 2 + LEFT * 3)
        p4 = Square(side_length=0.6, color=TEAL).shift(DOWN * 2 + RIGHT * 3)
        
        l1 = Line(hub_box.get_corner(UL), p1.get_center(), color=WHITE)
        l2 = Line(hub_box.get_corner(UR), p2.get_center(), color=WHITE)
        l3 = Line(hub_box.get_corner(DL), p3.get_center(), color=WHITE)
        l4 = Line(hub_box.get_corner(DR), p4.get_center(), color=WHITE)

        devices = VGroup(p1, p2, p3, p4, l1, l2, l3, l4)

        self.play(Create(hub_group), Create(devices))

        # Incoming Data Packet
        packet_in = Dot(color=YELLOW).move_to(p1.get_center())
        self.play(packet_in.animate.move_to(hub_box.get_center()), run_time=1.5)

        # Broadcast Data Packets
        out1 = Dot(color=YELLOW).move_to(hub_box.get_center())
        out2 = Dot(color=YELLOW).move_to(hub_box.get_center())
        out3 = Dot(color=YELLOW).move_to(hub_box.get_center())

        broadcast_text = Text("Broadcasting to all ports", font_size=20, color=GOLD).to_edge(DOWN)
        self.play(Write(broadcast_text))

        self.play(
            out1.animate.move_to(p2.get_center()),
            out2.animate.move_to(p3.get_center()),
            out3.animate.move_to(p4.get_center()),
            packet_in.animate.set_fill(opacity=0),
            run_time=2
        )

        self.wait(2)