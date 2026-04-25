import math
from manim import *

class Scene1(Scene):
    def construct(self):
        # Title
        title = Text("Repeaters and Hubs", font_size=40, color=WHITE).to_edge(UP, buff=0.5)
        divider = Line(start=[0, 2, 0], end=[0, -3, 0], color=WHITE)
        
        # --- Repeater Section (Left) ---
        rep_title = Text("Repeater", font_size=28, color=TEAL).move_to([-3.5, 2, 0])
        rep_box = Rectangle(width=2, height=1.2, color=TEAL, fill_opacity=0.3).move_to([-3.5, 0, 0])
        rep_text = Text("REPEATER", font_size=20).move_to(rep_box.get_center())
        rep_group = VGroup(rep_box, rep_text)
        
        weak_label = Text("Weak Signal", font_size=18, color=RED).next_to(rep_box, LEFT, buff=1).shift(UP*0.5)
        strong_label = Text("Regenerated", font_size=18, color=GREEN).next_to(rep_box, RIGHT, buff=0.5).shift(UP*0.5)
        
        weak_dot = Dot(point=[-6, 0, 0], radius=0.06, color=RED)
        strong_dot = Dot(point=[-3.5, 0, 0], radius=0.15, color=GREEN)
        
        # --- Hub Section (Right) ---
        hub_title = Text("Hub", font_size=28, color=GOLD).move_to([3.5, 2, 0])
        hub_circle = Circle(radius=0.6, color=GOLD, fill_opacity=0.4).move_to([3.5, 0, 0])
        hub_text = Text("HUB", font_size=20).move_to(hub_circle.get_center())
        hub_group = VGroup(hub_circle, hub_text)
        
        # Computers around the Hub
        pc1 = Square(side_length=0.5, color=WHITE, fill_opacity=0.2).move_to([3.5, 1.5, 0])
        pc2 = Square(side_length=0.5, color=WHITE, fill_opacity=0.2).move_to([5.3, 0, 0])
        pc3 = Square(side_length=0.5, color=WHITE, fill_opacity=0.2).move_to([3.5, -1.5, 0])
        pc4 = Square(side_length=0.5, color=WHITE, fill_opacity=0.2).move_to([1.7, 0, 0])
        pc_group = VGroup(pc1, pc2, pc3, pc4)
        
        # Connection lines
        l1 = Line(hub_circle.get_top(), pc1.get_bottom())
        l2 = Line(hub_circle.get_right(), pc2.get_left())
        l3 = Line(hub_circle.get_bottom(), pc3.get_top())
        l4 = Line(hub_circle.get_left(), pc4.get_right())
        lines_group = VGroup(l1, l2, l3, l4)

        # Narration subtitle
        sub = Text("Repeaters regenerate signals; Hubs broadcast to all ports.", font_size=20).to_edge(DOWN, buff=0.5)

        # --- Animations ---
        
        # Setup
        self.play(Write(title))
        self.play(Create(divider), Write(rep_title), Write(hub_title))
        self.play(Create(rep_group), Create(hub_group), Create(pc_group), Create(lines_group))
        self.play(Write(sub))
        self.wait(1)

        # Repeater Action
        self.play(FadeIn(weak_label), weak_dot.animate.move_to(rep_box.get_center()), run_time=1.5)
        self.play(Flash(rep_box, color=WHITE))
        self.remove(weak_dot)
        self.play(FadeIn(strong_label), FadeIn(strong_dot))
        self.play(strong_dot.animate.shift(RIGHT*2.5), run_time=1.5)
        self.wait(0.5)

        # Hub Action
        input_packet = Dot(pc3.get_center(), color=BLUE, radius=0.1)
        self.play(input_packet.animate.move_to(hub_circle.get_center()), run_time=1)
        self.play(Flash(hub_circle, color=GOLD))
        
        # Broadcast copies
        out1 = Dot(hub_circle.get_center(), color=BLUE, radius=0.1)
        out2 = Dot(hub_circle.get_center(), color=BLUE, radius=0.1)
        out3 = Dot(hub_circle.get_center(), color=BLUE, radius=0.1)
        out4 = Dot(hub_circle.get_center(), color=BLUE, radius=0.1)
        
        self.play(
            out1.animate.move_to(pc1.get_center()),
            out2.animate.move_to(pc2.get_center()),
            out3.animate.move_to(pc3.get_center()),
            out4.animate.move_to(pc4.get_center()),
            run_time=1.5
        )
        
        self.wait(2)

        # Clean exit
        self.play(
            FadeOut(title), FadeOut(divider), FadeOut(rep_group), FadeOut(hub_group),
            FadeOut(pc_group), FadeOut(lines_group), FadeOut(strong_dot), FadeOut(out1),
            FadeOut(out2), FadeOut(out3), FadeOut(out4), FadeOut(weak_label), 
            FadeOut(strong_label), FadeOut(sub), FadeOut(rep_title), FadeOut(hub_title),
            FadeOut(input_packet)
        )