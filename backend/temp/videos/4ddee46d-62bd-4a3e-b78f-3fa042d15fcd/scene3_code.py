from manim import *

class Scene3(Scene):
    def construct(self):
        # Title and Labels
        title = Text("Galloping Merge Strategy", color=GOLD).to_edge(UP)
        run_a_label = Text("Run A", font_size=24, color=WHITE).move_to([-3.5, 2, 0])
        run_b_label = Text("Run B", font_size=24, color=WHITE).move_to([3.5, 2, 0])
        merge_label = Text("Merged Result", font_size=24, color=WHITE).move_to([0, -1, 0])

        # Create Run A Squares
        run_a = VGroup(*[
            Square(side_length=0.6, fill_opacity=0.7, color=BLUE) for _ in range(5)
        ]).arrange(RIGHT, buff=0.1).next_to(run_a_label, DOWN)

        # Create Run B Squares
        run_b = VGroup(*[
            Square(side_length=0.6, fill_opacity=0.7, color=GREEN) for _ in range(5)
        ]).arrange(RIGHT, buff=0.1).next_to(run_b_label, DOWN)

        # Create Result Slots (Rectangles)
        res_slots = VGroup(*[
            Rectangle(width=0.6, height=0.6, stroke_color=WHITE, fill_opacity=0.1) for _ in range(10)
        ]).arrange(RIGHT, buff=0.1).next_to(merge_label, DOWN)

        # Initial Setup
        self.play(Write(title))
        self.play(
            Create(run_a), Write(run_a_label),
            Create(run_b), Write(run_b_label)
        )
        self.play(Create(res_slots), Write(merge_label))
        self.wait(0.5)

        # Galloping Arrow Animation
        gallop_arrow = Arrow(start=UP, end=DOWN, color=YELLOW, buff=0.1).scale(0.6)
        gallop_arrow.next_to(run_b[0], UP)
        
        self.play(Create(gallop_arrow))
        
        # Step 1: Jump to index 1 (2nd element)
        self.play(
            gallop_arrow.animate.next_to(run_b[1], UP),
            run_b[0].animate.set_fill(YELLOW, fill_opacity=0.8),
            run_b[1].animate.set_fill(YELLOW, fill_opacity=0.8),
            run_a[0].animate.set_color(GOLD),
            run_a[1].animate.set_color(GOLD),
            run_a[2].animate.set_color(GOLD),
            run_a[3].animate.set_color(GOLD),
            run_a[4].animate.set_color(GOLD),
            run_a.animate.set_fill(TEAL, fill_opacity=0.8),
            run_b.animate.set_fill(TEAL, fill_opacity=0.8),
            run_b[0].animate.set_fill(YELLOW, fill_opacity=0.8),
            run_b[1].animate.set_fill(YELLOW, fill_opacity=0.8),
            run_b[2].animate.set_fill(TEAL, fill_opacity=0.8),
            run_b[3].animate.set_fill(TEAL, fill_opacity=0.8),
            run_b[4].animate.set_fill(TEAL, fill_opacity=0.8),
            run_a.animate.set_fill(BLUE, fill_opacity=0.7),
            run_b.animate.set_fill(GREEN, fill_opacity=0.7),
            run_b[1].animate.set_fill(YELLOW, fill_opacity=0.9),
            run_b[0].animate.set_fill(YELLOW, fill_opacity=0.9),
            run_a.animate.set_color(BLUE)
        )

        # Step 2: Jump to index 3 (4th element) - Illustrates exponential skip
        self.play(
            gallop_arrow.animate.next_to(run_b[3], UP),
            run_b[2].animate.set_fill(YELLOW, fill_opacity=0.9),
            run_b[3].animate.set_fill(YELLOW, fill_opacity=0.9),
            run_a.animate.scale(1.1),
            run_a.animate.scale(0.909)
        )
        self.wait(0.5)

        # Step 3: Efficiently Merge chunks
        merge_group_a = run_a.copy()
        merge_group_b = run_b.copy()

        self.play(FadeOut(gallop_arrow))
        
        self.play(
            merge_group_a.animate.move_to(res_slots[0:5].get_center()),
            merge_group_b.animate.move_to(res_slots[5:10].get_center()),
            run_a.animate.set_fill(BLUE, fill_opacity=0.2),
            run_b.animate.set_fill(GREEN, fill_opacity=0.2),
            run_a.animate.set_stroke(opacity=0.3),
            run_b.animate.set_stroke(opacity=0.3),
            run_a_label.animate.set_stroke(opacity=0.3),
            run_b_label.animate.set_stroke(opacity=0.3)
        )
        
        # Highlight completion
        success_box = Rectangle(width=7.5, height=1.2, color=GOLD).move_to(res_slots.get_center())
        self.play(Create(success_box))
        self.wait(1.5)

        # Cleanup
        self.play(FadeOut(VGroup(title, run_a, run_b, run_a_label, run_b_label, merge_label, res_slots, merge_group_a, merge_group_b, success_box)))