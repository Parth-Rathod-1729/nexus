from manim import *

class Scene1(Scene):
    def construct(self):
        # Header
        title = Text("Physical Layer: Repeaters & Hubs", color=BLUE).scale(0.7)
        title.to_edge(UP)
        divider = Line(UP * 2, DOWN * 3, color=WHITE)
        self.add(title, divider)

        # Left Side - Repeater
        repeater_title = Text("Repeater", color=TEAL).scale(0.6).shift(LEFT * 3.5 + UP * 1.5)
        repeater_box = Square(side_length=1.2, color=TEAL, fill_opacity=0.2).shift(LEFT * 3.5)
        repeater_text = Text("Regenerate", color=WHITE).scale(0.3).move_to(repeater_box.get_center())
        
        # Weak Signal (Jagged lines)
        weak_signal = VGroup(
            Line(LEFT * 6, LEFT * 5.8), Line(LEFT * 5.8, LEFT * 5.6 + UP * 0.2),
            Line(LEFT * 5.6 + UP * 0.2, LEFT * 5.4 + DOWN * 0.2), Line(LEFT * 5.4 + DOWN * 0.2, LEFT * 5.2)
        ).set_color(RED).shift(DOWN * 0.5)
        
        # Strong Signal (Clean Arrow)
        strong_signal = Arrow(LEFT * 2.8, LEFT * 0.5, color=GREEN, buff=0)

        repeater_group = VGroup(repeater_title, repeater_box, repeater_text)
        self.play(Write(repeater_group))
        self.play(weak_signal.animate.move_to(repeater_box.get_center()), run_time=1.5)
        self.play(repeater_box.animate.set_fill(TEAL, opacity=0.8), weak_signal.animate.set_opacity(0))
        self.play(Create(strong_signal), repeater_box.animate.set_fill(TEAL, opacity=0.2))
        self.wait(1)

        # Right Side - Hub
        hub_title = Text("Hub", color=GOLD).scale(0.6).shift(RIGHT * 3.5 + UP * 1.5)
        hub_box = Square(side_length=1.2, color=GOLD, fill_opacity=0.2).shift(RIGHT * 3.5)
        hub_text = Text("Broadcast", color=WHITE).scale(0.3).move_to(hub_box.get_center())

        # Devices connected to Hub
        d1 = Dot(color=WHITE).shift(RIGHT * 5.5 + UP * 1)
        d2 = Dot(color=WHITE).shift(RIGHT * 6 + DOWN * 0)
        d3 = Dot(color=WHITE).shift(RIGHT * 5.5 + DOWN * 1)
        devices = VGroup(d1, d2, d3)
        
        lines = VGroup(
            Line(hub_box.get_right(), d1.get_left()),
            Line(hub_box.get_right(), d2.get_left()),
            Line(hub_box.get_right(), d3.get_left())
        ).set_color(WHITE).set_opacity(0.3)

        hub_group = VGroup(hub_title, hub_box, hub_text, devices, lines)
        self.play(Write(hub_group))

        # Data packet flow
        input_packet = Circle(radius=0.1, color=YELLOW, fill_opacity=1).next_to(hub_box, LEFT, buff=0.5)
        self.play(input_packet.animate.move_to(hub_box.get_center()), run_time=1)
        
        # Broadcast effect
        p1 = Circle(radius=0.1, color=YELLOW, fill_opacity=1).move_to(hub_box.get_center())
        p2 = Circle(radius=0.1, color=YELLOW, fill_opacity=1).move_to(hub_box.get_center())
        p3 = Circle(radius=0.1, color=YELLOW, fill_opacity=1).move_to(hub_box.get_center())
        
        self.play(
            p1.animate.move_to(d1.get_center()),
            p2.animate.move_to(d2.get_center()),
            p3.animate.move_to(d3.get_center()),
            input_packet.animate.set_opacity(0),
            run_time=1.5
        )
        self.wait(2)