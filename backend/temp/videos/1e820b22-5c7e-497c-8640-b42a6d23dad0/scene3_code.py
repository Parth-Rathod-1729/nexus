from manim import *

class Scene3(Scene):
    def construct(self):
        # 1. Setup the Environment
        room_a = Rectangle(width=5, height=3.5, color=WHITE).move_to(LEFT * 3)
        room_b = Rectangle(width=5, height=3.5, color=WHITE).move_to(RIGHT * 3)
        label_a = Text("Room A", font_size=28, color=WHITE).next_to(room_a, UP)
        label_b = Text("Room B", font_size=28, color=WHITE).next_to(room_b, UP)
        rooms = VGroup(room_a, room_b, label_a, label_b)

        # 2. Performance Measure UI
        score_label = Text("Performance Score:", font_size=32).to_edge(UP).shift(LEFT * 0.5)
        score_val = MathTex("0", color=YELLOW, font_size=48).next_to(score_label, RIGHT)
        score_group = VGroup(score_label, score_val)

        # 3. Rational Agent (Vacuum)
        body = Square(side_length=0.8, color=BLUE, fill_opacity=0.8)
        head = Circle(radius=0.15, color=WHITE, fill_opacity=0.6).move_to(body.get_center())
        vacuum = VGroup(body, head).move_to(room_a.get_center())

        # 4. Dirt Particles
        d1 = Dot(point=room_a.get_center() + LEFT*0.8 + UP*0.5, color=GOLD, radius=0.12)
        d2 = Dot(point=room_a.get_center() + RIGHT*0.9 + DOWN*0.4, color=GOLD, radius=0.12)
        d3 = Dot(point=room_a.get_center() + LEFT*0.3 + DOWN*0.7, color=GOLD, radius=0.12)
        dirt = VGroup(d1, d2, d3)

        # 5. Animation Sequence
        self.play(Create(rooms), Write(score_group))
        self.play(FadeIn(vacuum), FadeIn(dirt))
        self.wait(1)

        # Action: Detect and Clean d1
        self.play(vacuum.animate.move_to(d1.get_center()), run_time=0.8)
        self.play(FadeOut(d1))
        
        # Update Score 1
        new_score_1 = MathTex("10", color=GREEN, font_size=48).move_to(score_val)
        self.play(Transform(score_val, new_score_1))

        # Action: Detect and Clean d2
        self.play(vacuum.animate.move_to(d2.get_center()), run_time=0.8)
        self.play(FadeOut(d2))

        # Update Score 2
        new_score_2 = MathTex("20", color=GREEN, font_size=48).move_to(score_val)
        self.play(Transform(score_val, new_score_2))

        # Action: Detect and Clean d3
        self.play(vacuum.animate.move_to(d3.get_center()), run_time=0.8)
        self.play(FadeOut(d3))

        # Final Score for Room A
        final_score = MathTex("30", color=GREEN, font_size=48).move_to(score_val)
        self.play(Transform(score_val, final_score))

        # Move to next room as part of rational strategy
        self.play(vacuum.animate.move_to(room_b.get_center()), run_time=1.2)
        
        # Rationality Text
        rational_txt = Text("Maximizing Performance", font_size=30, color=TEAL).next_to(rooms, DOWN)
        self.play(Write(rational_txt))
        
        self.wait(2)