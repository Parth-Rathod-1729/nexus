from manim import *

class Scene1(Scene):
    def construct(self):
        # 1. Title and Layout
        title = Text("Physical Layer: Repeaters and Hubs", color=WHITE).scale(0.8).to_edge(UP)
        divider = Line(UP * 2.5, DOWN * 3, color=WHITE)
        
        # 2. Repeater Construction (Left Side)
        repeater_label = Text("Repeater (2 Ports)", font_size=24).move_to(LEFT * 3.5 + UP * 2)
        repeater_box = Rectangle(width=1.2, height=0.8, color=BLUE, fill_opacity=0.3).move_to(LEFT * 3.5)
        repeater_text = Text("Regen", font_size=18).move_to(repeater_box.get_center())
        
        in_wire = Line(LEFT * 6, LEFT * 4.1)
        out_wire = Line(LEFT * 2.9, LEFT * 1)
        
        repeater_group = VGroup(repeater_box, repeater_text, in_wire, out_wire)
        
        # 3. Hub Construction (Right Side)
        hub_label = Text("Hub (Multi-port)", font_size=24).move_to(RIGHT * 3.5 + UP * 2)
        hub_box = Square(side_length=1.2, color=TEAL, fill_opacity=0.3).move_to(RIGHT * 3.5)
        hub_text = Text("Broadcast", font_size=18).move_to(hub_box.get_center())
        
        # Hub Ports
        p_in = Line(RIGHT * 1, RIGHT * 2.9)
        p_out1 = Line(RIGHT * 4.1, RIGHT * 6)
        p_out2 = Line(RIGHT * 3.5 + UP * 0.6, RIGHT * 3.5 + UP * 1.5)
        p_out3 = Line(RIGHT * 3.5 + DOWN * 0.6, RIGHT * 3.5 + DOWN * 1.5)
        
        hub_group = VGroup(hub_box, hub_text, p_in, p_out1, p_out2, p_out3)

        # 4. Display Static Elements
        self.play(Write(title))
        self.play(Create(divider))
        self.play(
            Create(repeater_group),
            Write(repeater_label),
            Create(hub_group),
            Write(hub_label)
        )
        self.wait(1)

        # 5. Repeater Animation: Signal Regeneration
        weak_signal = Dot(color=RED).scale(0.5).move_to(in_wire.get_start())
        strong_signal = Dot(color=GREEN).scale(1.5).move_to(repeater_box.get_center())
        
        regeneration_label = Text("Regenerates", font_size=20, color=GOLD).next_to(repeater_box, DOWN)

        self.play(weak_signal.animate.move_to(repeater_box.get_center()), run_time=1.5)
        self.play(FadeOut(weak_signal), FadeIn(strong_signal), Write(regeneration_label))
        self.play(strong_signal.animate.move_to(out_wire.get_end()), run_time=1.5)
        self.wait(1)

        # 6. Hub Animation: Broadcasting
        input_dot = Dot(color=YELLOW).move_to(p_in.get_start())
        
        broadcast_label = Text("Copies to all ports", font_size=20, color=GOLD).next_to(hub_box, DOWN)
        
        self.play(input_dot.animate.move_to(hub_box.get_center()), run_time=1)
        self.play(Write(broadcast_label))
        
        # Split dots for broadcasting
        d1 = Dot(color=YELLOW).move_to(hub_box.get_center())
        d2 = Dot(color=YELLOW).move_to(hub_box.get_center())
        d3 = Dot(color=YELLOW).move_to(hub_box.get_center())
        
        self.remove(input_dot)
        self.play(
            d1.animate.move_to(p_out1.get_end()),
            d2.animate.move_to(p_out2.get_end()),
            d3.animate.move_to(p_out3.get_end()),
            run_time=1.5
        )
        
        self.wait(2)