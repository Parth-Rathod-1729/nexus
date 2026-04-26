from manim import *

class Scene3(Scene):
    def construct(self):
        # Title and Concept
        title = Text("Galloping Strategy", color=GOLD).to_edge(UP)
        explanation = Text("Exponential search for faster merging", font_size=20).next_to(title, DOWN)
        
        # Run A: Several sorted elements
        vals_a = [10, 15, 20, 25, 30, 35, 40, 45]
        run_a = VGroup(*[
            VGroup(
                Square(side_length=0.7, fill_color=BLUE, fill_opacity=0.7),
                Text(str(v), font_size=22)
            ) for v in vals_a
        ]).arrange(RIGHT, buff=0.1).shift(UP * 0.2)
        
        label_a = Text("Run A", font_size=24, color=BLUE).next_to(run_a, LEFT)

        # Run B: One large element to compare
        val_b = 100
        run_b_box = VGroup(
            Square(side_length=0.7, fill_color=GREEN, fill_opacity=0.7),
            Text(str(val_b), font_size=22)
        ).next_to(run_a, DOWN, buff=1.5).align_to(run_a, LEFT)
        
        label_b = Text("Run B element", font_size=24, color=GREEN).next_to(run_b_box, LEFT)

        self.play(Write(title), Write(explanation))
        self.play(Create(run_a), Create(run_b_box), Write(label_a), Write(label_b))

        # Comparison Pointer
        pointer = Arrow(start=DOWN, end=UP, color=YELLOW, buff=0.1).scale(0.6)
        pointer.next_to(run_a[0], DOWN)
        
        self.play(Create(pointer))

        # Galloping Sequence: Jumps at 2^k - 1 (Indices 0, 1, 3, 7)
        # Step 1: index 1
        self.play(
            pointer.animate.next_to(run_a[1], DOWN), 
            run_a[1][0].animate.set_fill(TEAL, fill_opacity=0.9),
            run_a[0][0].animate.set_fill(BLUE, fill_opacity=0.3),
            run_b_box[0].animate.set_stroke(YELLOW, width=4)
        )
        self.wait(0.5)
        
        # Step 2: index 3 (Exponential jump)
        gallop_label = Text("Gallop Step: 2", color=YELLOW, font_size=24).next_to(run_b_box, RIGHT, buff=1)
        self.play(
            pointer.animate.next_to(run_a[3], DOWN), 
            run_a[3][0].animate.set_fill(TEAL, fill_opacity=0.9),
            run_a[1][0].animate.set_fill(BLUE, fill_opacity=0.3),
            Write(gallop_label)
        )
        self.wait(0.5)
        
        # Step 3: index 7 (Exponential jump)
        self.play(
            pointer.animate.next_to(run_a[7], DOWN), 
            run_a[7][0].animate.set_fill(TEAL, fill_opacity=0.9),
            run_a[3][0].animate.set_fill(BLUE, fill_opacity=0.3),
            gallop_label.animate.become(Text("Gallop Step: 4", color=YELLOW, font_size=24).next_to(run_b_box, RIGHT, buff=1))
        )
        self.wait(0.8)

        # Skip Visualizer
        skip_rect = Rectangle(width=run_a.get_width(), height=0.9, color=YELLOW).move_to(run_a.get_center())
        skip_text = Text("Whole block identified", font_size=24, color=YELLOW).next_to(run_a, UP)
        
        self.play(Create(skip_rect), Write(skip_text))
        self.wait(1)

        # Final Merging action
        merged_group = VGroup(*[run_a, run_b_box])
        target_zone = Rectangle(width=8, height=1.2, stroke_dash_array=[5, 5]).shift(DOWN * 2.5)
        
        self.play(
            FadeOut(pointer),
            FadeOut(gallop_label),
            FadeOut(skip_rect),
            FadeOut(skip_text),
            run_a.animate.scale(0.8).move_to(DOWN * 2.5 + LEFT * 1),
            run_b_box.animate.scale(0.8).next_to(run_a, RIGHT, buff=0.1).shift(DOWN * 0.05),
            explanation.animate.become(Text("Massive performance boost for real-world data", font_size=24, color=WHITE).next_to(title, DOWN))
        )
        
        self.wait(2)
        self.play(FadeOut(VGroup(title, explanation, run_a, run_b_box, label_a, label_b)))