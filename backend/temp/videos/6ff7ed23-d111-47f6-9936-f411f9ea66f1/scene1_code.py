from manim import *

class Scene1(Scene):
    def construct(self):
        # 1. Background Setup: Divider and Titles
        divider = Line(UP * 3.5, DOWN * 3.5, color=WHITE)
        left_title = Text("Repeater: Signal Regeneration", font_size=28, color=WHITE).to_edge(UP).shift(LEFT * 3.5)
        right_title = Text("Hub: Multi-port Broadcast", font_size=28, color=WHITE).to_edge(UP).shift(RIGHT * 3.5)
        
        self.add(divider, left_title, right_title)

        # 2. Repeater Section (Left)
        repeater_box = Rectangle(width=2, height=1.2, color=BLUE, fill_opacity=0.2).move_to(LEFT * 3.5)
        repeater_text = Text("REPEATER", font_size=20, color=BLUE).move_to(repeater_box.get_center())
        repeater_group = VGroup(repeater_box, repeater_text)

        # Weak Signal Bits (before)
        weak_bits = VGroup()
        for i in range(3):
            # Shrinking heights to simulate attenuation
            h = 0.4 - (i * 0.1)
            bit = Line(ORIGIN, UP * h, color=RED, stroke_width=2).move_to(LEFT * (6.0 - i * 0.6) + DOWN * 0.2)
            weak_bits.add(bit)
        
        # Strong Signal Bits (after)
        strong_bits = VGroup()
        for i in range(3):
            bit = Line(ORIGIN, UP * 0.8, color=GREEN, stroke_width=6).move_to(LEFT * (2.0 - i * 0.6) + DOWN * 0.2)
            strong_bits.add(bit)

        # 3. Hub Section (Right)
        hub_box = Rectangle(width=1.8, height=1.2, color=GOLD, fill_opacity=0.2).move_to(RIGHT * 3.5)
        hub_text = Text("HUB", font_size=20, color=GOLD).move_to(hub_box.get_center())
        hub_group = VGroup(hub_box, hub_text)

        # Connected Stations (Circles)
        c1 = Circle(radius=0.3, color=TEAL, fill_opacity=0.5).move_to(RIGHT * 1.5 + UP * 2)
        c2 = Circle(radius=0.3, color=TEAL, fill_opacity=0.5).move_to(RIGHT * 5.5 + UP * 2)
        c3 = Circle(radius=0.3, color=TEAL, fill_opacity=0.5).move_to(RIGHT * 1.5 + DOWN * 2)
        c4 = Circle(radius=0.3, color=TEAL, fill_opacity=0.5).move_to(RIGHT * 5.5 + DOWN * 2)
        stations = VGroup(c1, c2, c3, c4)

        # Connection Lines
        l1 = Line(hub_box.get_center(), c1.get_center(), color=WHITE, stroke_width=2)
        l2 = Line(hub_box.get_center(), c2.get_center(), color=WHITE, stroke_width=2)
        l3 = Line(hub_box.get_center(), c3.get_center(), color=WHITE, stroke_width=2)
        l4 = Line(hub_box.get_center(), c4.get_center(), color=WHITE, stroke_width=2)
        links = VGroup(l1, l2, l3, l4)

        # 4. Animation Sequence
        
        # Show Repeater and Hub
        self.play(Create(repeater_group), Create(hub_group))
        self.play(Create(stations), Create(links))
        self.wait(1)

        # Left: Signal Regeneration
        self.play(Create(weak_bits, run_time=2))
        arrow_in = Arrow(LEFT * 5, LEFT * 4.5, color=RED)
        self.play(FadeIn(arrow_in))
        
        self.play(
            weak_bits.animate.move_to(repeater_box.get_center()).set_opacity(0),
            run_time=1
        )
        
        self.play(Create(strong_bits, run_time=1))
        arrow_out = Arrow(LEFT * 2.5, LEFT * 1.5, color=GREEN)
        self.play(FadeIn(arrow_out))
        self.wait(1)

        # Right: Hub Broadcast
        # Incoming packet
        packet_in = Dot(color=YELLOW).move_to(RIGHT * 3.5 + DOWN * 3.5)
        self.play(packet_in.animate.move_to(hub_box.get_center()))
        
        # Outgoing broadcast packets
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

        # Cleanup
        self.play(FadeOut(weak_bits, strong_bits, arrow_in, arrow_out, p1, p2, p3, p4, packet_in))
        self.wait(1)