from manim import *

class Scene3(Scene):
    def construct(self):
        # Title
        title = Text("The Rational Agent", color=GOLD).to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Room Squares (Dirty = RED, Clean = TEAL)
        s1 = Square(side_length=1.2, color=WHITE, fill_color=RED, fill_opacity=0.4).shift(LEFT * 3 + DOWN * 1)
        s2 = Square(side_length=1.2, color=WHITE, fill_color=RED, fill_opacity=0.4).next_to(s1, RIGHT, buff=0.2)
        s3 = Square(side_length=1.2, color=WHITE, fill_color=RED, fill_opacity=0.4).next_to(s2, RIGHT, buff=0.2)
        room = VGroup(s1, s2, s3)

        # Performance Meter
        meter_label = Text("Performance", font_size=24).to_edge(LEFT, buff=1).shift(UP * 1.5)
        meter_bg = Rectangle(width=3, height=0.4, color=WHITE).next_to(meter_label, DOWN, buff=0.2)
        meter_fill = Rectangle(width=0.01, height=0.3, color=GREEN, fill_opacity=1).move_to(meter_bg.get_left(), aligned_edge=LEFT).shift(RIGHT * 0.05)
        score_val = MathTex("0", color=WHITE).next_to(meter_bg, RIGHT)
        
        # Agent
        agent = Circle(radius=0.4, color=BLUE, fill_opacity=1).move_to(s1.get_center())
        
        self.play(Create(room), Create(agent))
        self.play(Create(meter_bg), Write(meter_label), Write(score_val))

        # Pillars of Rationality
        pillars_title = Text("Rationality Pillars:", font_size=28, color=YELLOW).to_edge(RIGHT, buff=0.5).shift(UP * 2)
        p1 = Text("1. Performance Measure", font_size=22).next_to(pillars_title, DOWN, aligned_edge=LEFT, buff=0.4)
        p2 = Text("2. Prior Knowledge", font_size=22).next_to(p1, DOWN, aligned_edge=LEFT, buff=0.3)
        p3 = Text("3. Available Actions", font_size=22).next_to(p2, DOWN, aligned_edge=LEFT, buff=0.3)
        p4 = Text("4. Percept Sequence", font_size=22).next_to(p3, DOWN, aligned_edge=LEFT, buff=0.3)
        
        # Action Sequence
        # Cleaning first square
        self.play(Write(p1))
        self.play(s1.animate.set_fill(TEAL, fill_opacity=0.8))
        self.play(
            meter_fill.animate.stretch_to_fit_width(1.0, about_edge=LEFT),
            Transform(score_val, MathTex("50", color=WHITE).next_to(meter_bg, RIGHT))
        )

        # Moving and cleaning second square
        self.play(Write(p2), agent.animate.move_to(s2.get_center()))
        self.play(s2.animate.set_fill(TEAL, fill_opacity=0.8))
        self.play(
            meter_fill.animate.stretch_to_fit_width(2.0, about_edge=LEFT),
            Transform(score_val, MathTex("100", color=WHITE).next_to(meter_bg, RIGHT))
        )

        # Final move and cleaning
        self.play(Write(p3), Write(p4), agent.animate.move_to(s3.get_center()))
        self.play(s3.animate.set_fill(TEAL, fill_opacity=0.8))
        self.play(
            meter_fill.animate.stretch_to_fit_width(2.9, about_edge=LEFT),
            Transform(score_val, MathTex("150", color=WHITE).next_to(meter_bg, RIGHT))
        )

        self.wait(2)