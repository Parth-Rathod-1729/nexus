from manim import *

class Scene1(Scene):
    def construct(self):
        # Title
        title = Text("Layer 1: Repeaters and Hubs", color=WHITE).scale(0.8).to_edge(UP)
        self.add(title)

        # REPEATER SECTION (Left Side)
        repeater_label = Text("Repeater", font_size=24, color=BLUE).move_to([-3.5, 1.5, 0])
        repeater_box = Rectangle(width=1.6, height=1.0, color=BLUE, fill_opacity=0.2).move_to([-3.5, 0, 0])
        
        # Weak Signal (Jagged lines)
        w1 = Line([-5.5, 0, 0], [-5.3, 0.2, 0], color=RED)
        w2 = Line([-5.3, 0.2, 0], [-5.1, -0.2, 0], color=RED)
        w3 = Line([-5.1, -0.2, 0], [-4.9, 0.1, 0], color=RED)
        w4 = Line([-4.9, 0.1, 0], [-4.7, 0, 0], color=RED)
        weak_signal = VGroup(w1, w2, w3, w4)
        weak_text = Text("Weak Signal", font_size=18, color=RED).next_to(weak_signal, DOWN)

        # Strong Signal (Clean pulse)
        s1 = Line([-2.3, 0, 0], [-2.3, 0.5, 0], color=GREEN)
        s2 = Line([-2.3, 0.5, 0], [-1.8, 0.5, 0], color=GREEN)
        s3 = Line([-1.8, 0.5, 0], [-1.8, 0, 0], color=GREEN)
        s4 = Line([-1.8, 0, 0], [-1.3, 0, 0], color=GREEN)
        strong_signal = VGroup(s1, s2, s3, s4)
        strong_text = Text("Strong Signal", font_size=18, color=GREEN).next_to(strong_signal, DOWN)

        # HUB SECTION (Right Side)
        hub_label = Text("Hub", font_size=24, color=TEAL).move_to([3.5, 1.5, 0])
        hub_box = Square(side_length=1.2, color=TEAL, fill_opacity=0.2).move_to([3.5, 0, 0])
        
        # Connected Devices (Dots)
        d1 = Dot(point=[3.5, 2.2, 0], color=WHITE)  # Top
        d2 = Dot(point=[5.0, 0, 0], color=WHITE)    # Right
        d3 = Dot(point=[3.5, -2.2, 0], color=WHITE) # Bottom
        d4 = Dot(point=[2.0, 0, 0], color=WHITE)    # Left
        devices = VGroup(d1, d2, d3, d4)
        
        # Connection Lines
        l1 = Line(hub_box.get_top(), d1.get_center(), stroke_width=2)
        l2 = Line(hub_box.get_right(), d2.get_center(), stroke_width=2)
        l3 = Line(hub_box.get_bottom(), d3.get_center(), stroke_width=2)
        l4 = Line(hub_box.get_left(), d4.get_center(), stroke_width=2)
        connections = VGroup(l1, l2, l3, l4)

        # Animation Sequence
        self.play(Write(repeater_label), Create(repeater_box))
        self.play(Create(weak_signal), Write(weak_text))
        self.play(weak_signal.animate.move_to([-3.5, 0, 0]), run_time=1.5)
        self.play(FadeOut(weak_signal), FadeIn(strong_signal), Write(strong_text))
        self.play(strong_signal.animate.shift(RIGHT * 1.5), run_time=1.5)
        
        self.wait(0.5)
        
        self.play(Write(hub_label), Create(hub_box), Create(devices), Create(connections))
        
        # Packet enters hub
        p_in = Dot(point=[3.5, 2.2, 0], color=YELLOW)
        self.play(p_in.animate.move_to([3.5, 0, 0]), run_time=1)
        
        # Broadcast copies
        p1 = Dot(point=[3.5, 0, 0], color=YELLOW)
        p2 = Dot(point=[3.5, 0, 0], color=YELLOW)
        p3 = Dot(point=[3.5, 0, 0], color=YELLOW)
        p4 = Dot(point=[3.5, 0, 0], color=YELLOW)
        
        self.play(
            p1.animate.move_to(d1.get_center()),
            p2.animate.move_to(d2.get_center()),
            p3.animate.move_to(d3.get_center()),
            p4.animate.move_to(d4.get_center()),
            hub_box.animate.set_fill(YELLOW, opacity=0.4),
            run_time=1.5
        )
        self.play(hub_box.animate.set_fill(TEAL, opacity=0.2))
        
        self.wait(2)