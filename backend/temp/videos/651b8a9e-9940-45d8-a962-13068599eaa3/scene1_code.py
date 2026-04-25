from manim import *

class Scene1(Scene):
    def construct(self):
        # Header
        title = Text("Signal Regeneration: Repeaters and Hubs", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.add(title)

        # --- Repeater Section (Left) ---
        repeater_title = Text("Repeater", font_size=28, color=BLUE).move_to([-3.5, 2, 0])
        repeater_box = Square(side_length=1.5, color=BLUE).move_to([-3.5, 0, 0])
        repeater_label = Text("Repeater", font_size=20).move_to(repeater_box.get_center())
        
        # Weak Signal (Jagged segments)
        w1 = Line([-6, 0.2, 0], [-5.7, -0.2, 0], color=RED, stroke_width=2)
        w2 = Line([-5.7, -0.2, 0], [-5.4, 0.2, 0], color=RED, stroke_width=2)
        w3 = Line([-5.4, 0.2, 0], [-5.1, -0.2, 0], color=RED, stroke_width=2)
        w4 = Line([-5.1, -0.2, 0], [-4.8, 0, 0], color=RED, stroke_width=2)
        weak_signal = VGroup(w1, w2, w3, w4)
        weak_text = Text("Weak Signal", font_size=16, color=RED).next_to(weak_signal, DOWN)

        # Strong Signal
        strong_arrow = Arrow(start=[-2.75, 0, 0], end=[-0.5, 0, 0], color=GREEN, buff=0)
        strong_text = Text("Regenerated", font_size=16, color=GREEN).next_to(strong_arrow, DOWN)

        self.play(Write(repeater_title), Create(repeater_box), Write(repeater_label))
        self.play(Create(weak_signal), Write(weak_text))
        self.wait(1)
        self.play(Create(strong_arrow), Write(strong_text))
        self.wait(1)

        # --- Hub Section (Right) ---
        hub_title = Text("Hub", font_size=28, color=GOLD).move_to([3.5, 2, 0])
        hub_box = Rectangle(width=1.8, height=1.0, color=GOLD, fill_opacity=0.2).move_to([3.5, 0, 0])
        hub_label = Text("Hub", font_size=20).move_to(hub_box.get_center())

        # Stations (4 Circles)
        c1 = Circle(radius=0.3, color=WHITE).move_to([2.0, -2, 0])
        c2 = Circle(radius=0.3, color=WHITE).move_to([3.0, -2, 0])
        c3 = Circle(radius=0.3, color=WHITE).move_to([4.0, -2, 0])
        c4 = Circle(radius=0.3, color=WHITE).move_to([5.0, -2, 0])
        stations = VGroup(c1, c2, c3, c4)

        # Connection Lines
        l1 = Line(hub_box.get_bottom(), c1.get_top())
        l2 = Line(hub_box.get_bottom(), c2.get_top())
        l3 = Line(hub_box.get_bottom(), c3.get_top())
        l4 = Line(hub_box.get_bottom(), c4.get_top())
        links = VGroup(l1, l2, l3, l4)

        # Incoming data
        in_arrow = Arrow(start=[3.5, 1.2, 0], end=[3.5, 0.5, 0], color=TEAL)
        packet_in = Dot(color=YELLOW).move_to([3.5, 1.2, 0])

        self.play(Write(hub_title), Create(hub_box), Write(hub_label))
        self.play(Create(stations), Create(links))
        
        # Broadcast Animation
        self.play(packet_in.animate.move_to(hub_box.get_center()), Create(in_arrow))
        
        # Create 4 packets for broadcast
        p1 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p2 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p3 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p4 = Dot(color=YELLOW).move_to(hub_box.get_center())
        
        self.play(
            p1.animate.move_to(c1.get_center()),
            p2.animate.move_to(c2.get_center()),
            p3.animate.move_to(c3.get_center()),
            p4.animate.move_to(c4.get_center()),
            run_time=2
        )
        self.wait(2)

        # Cleanup labels and secondary items
        self.play(FadeOut(weak_text), FadeOut(strong_text), FadeOut(in_arrow))
        self.wait(1)

        # Summary text
        summary = Text("Repeaters regenerate, Hubs broadcast.", font_size=24, color=YELLOW).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)