from manim import *

class Scene1(Scene):
    def construct(self):
        # Header
        title = Text("Physical Layer: Repeaters & Hubs", color=WHITE).scale(0.8).to_edge(UP)
        self.play(Write(title))
        
        # Split Screen Divider
        divider = Line(UP * 2, DOWN * 3, color=WHITE)
        self.play(Create(divider))

        # --- REPEATER SECTION (LEFT) ---
        rep_label = Text("Repeater", color=BLUE).scale(0.6).move_to(LEFT * 3.5 + UP * 1.5)
        rep_box = Rectangle(width=1.5, height=1, color=BLUE, fill_opacity=0.2).shift(LEFT * 3.5)
        rep_text = Text("Signal\nRegenerator", font_size=20).move_to(rep_box.get_center())
        
        # Weak Signal
        w1 = Line(LEFT * 6 + UP * 0.1, LEFT * 5.7 + UP * 0.3, color=RED)
        w2 = Line(LEFT * 5.7 + UP * 0.3, LEFT * 5.4 + DOWN * 0.2, color=RED)
        w3 = Line(LEFT * 5.4 + DOWN * 0.2, LEFT * 5.1 + UP * 0.1, color=RED)
        weak_signal = VGroup(w1, w2, w3)
        
        # Strong Signal
        s1 = Line(LEFT * 1.9 + UP * 0.1, LEFT * 1.5 + UP * 0.6, color=GREEN)
        s2 = Line(LEFT * 1.5 + UP * 0.6, LEFT * 1.1 + DOWN * 0.5, color=GREEN)
        s3 = Line(LEFT * 1.1 + DOWN * 0.5, LEFT * 0.7 + UP * 0.1, color=GREEN)
        strong_signal = VGroup(s1, s2, s3)

        self.play(Create(rep_box), Write(rep_label), Write(rep_text))
        self.play(Create(weak_signal))
        self.play(weak_signal.animate.move_to(rep_box.get_center()), run_time=1.5)
        self.play(FadeOut(weak_signal))
        self.play(Create(strong_signal))
        self.play(strong_signal.animate.shift(RIGHT * 0.5), run_time=1.5)

        # --- HUB SECTION (RIGHT) ---
        hub_label = Text("Hub", color=TEAL).scale(0.6).move_to(RIGHT * 3.5 + UP * 1.5)
        hub_box = Square(side_length=1.2, color=TEAL, fill_opacity=0.2).shift(RIGHT * 3.5)
        hub_text = Text("Broadcaster", font_size=20).move_to(hub_box.get_center())
        
        # Connected Devices (Dots)
        pc1 = Dot(RIGHT * 2.5 + DOWN * 2, color=WHITE)
        pc2 = Dot(RIGHT * 3.2 + DOWN * 2, color=WHITE)
        pc3 = Dot(RIGHT * 3.9 + DOWN * 2, color=WHITE)
        pc4 = Dot(RIGHT * 4.6 + DOWN * 2, color=WHITE)
        pcs = VGroup(pc1, pc2, pc3, pc4)
        
        # Connection Lines
        l1 = Line(hub_box.get_bottom(), pc1.get_top(), stroke_width=2)
        l2 = Line(hub_box.get_bottom(), pc2.get_top(), stroke_width=2)
        l3 = Line(hub_box.get_bottom(), pc3.get_top(), stroke_width=2)
        l4 = Line(hub_box.get_bottom(), pc4.get_top(), stroke_width=2)
        conns = VGroup(l1, l2, l3, l4)

        self.play(Create(hub_box), Write(hub_label), Write(hub_text))
        self.play(Create(pcs), Create(conns))
        
        # Data Packet Animation
        packet_in = Dot(color=GOLD).move_to(RIGHT * 5.5 + hub_box.get_center()[1])
        self.play(packet_in.animate.move_to(hub_box.get_center()))
        
        # Broadcasting copies
        p1 = Dot(color=GOLD).move_to(hub_box.get_center())
        p2 = Dot(color=GOLD).move_to(hub_box.get_center())
        p3 = Dot(color=GOLD).move_to(hub_box.get_center())
        p4 = Dot(color=GOLD).move_to(hub_box.get_center())
        
        self.play(FadeOut(packet_in))
        self.play(
            p1.animate.move_to(pc1.get_center()),
            p2.animate.move_to(pc2.get_center()),
            p3.animate.move_to(pc3.get_center()),
            p4.animate.move_to(pc4.get_center()),
            run_time=2
        )
        
        # Conclusion Text
        footer = Text("Hubs lack recipient filtering", font_size=24, color=YELLOW).to_edge(DOWN)
        self.play(Write(footer))
        self.wait(2)

        # Cleanup
        self.play(FadeOut(rep_box), FadeOut(hub_box), FadeOut(footer), FadeOut(title), FadeOut(divider), FadeOut(strong_signal), FadeOut(p1), FadeOut(p2), FadeOut(p3), FadeOut(p4), FadeOut(pcs), FadeOut(conns), FadeOut(rep_text), FadeOut(hub_text), FadeOut(rep_label), FadeOut(hub_label))