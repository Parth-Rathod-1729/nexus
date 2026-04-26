from manim import *

class Scene1(Scene):
    def construct(self):
        # Title and Explanation
        title = Text("Identifying Natural Runs", color=WHITE).scale(0.8)
        title.to_edge(UP, buff=0.5)
        
        # Array Data
        values = [10, 20, 30, 5, 15, 42, 2, 8, 12]
        squares = VGroup()
        numbers = VGroup()
        
        for i, val in enumerate(values):
            sq = Square(side_length=0.8, color=WHITE)
            sq.move_to(LEFT * 4 + RIGHT * i * 1.0)
            num = Text(str(val)).scale(0.7).move_to(sq.get_center())
            squares.add(sq)
            numbers.add(num)
        
        array_grp = VGroup(squares, numbers).center()
        
        # Identification of Runs
        # Run 1: indices 0, 1, 2
        run1_rect = Rectangle(width=2.8, height=1.0, color=GREEN, fill_opacity=0.2)
        run1_rect.move_to(squares[1].get_center())
        run1_label = Text("Natural Run", color=GREEN).scale(0.4).next_to(run1_rect, DOWN)
        
        # Run 2: indices 3, 4
        run2_rect = Rectangle(width=1.8, height=1.0, color=RED, fill_opacity=0.2)
        run2_rect.move_to(VGroup(squares[3], squares[4]).get_center())
        run2_label = Text("Short Run", color=RED).scale(0.4).next_to(run2_rect, DOWN)
        
        # Run 3: indices 6, 7, 8
        run3_rect = Rectangle(width=2.8, height=1.0, color=TEAL, fill_opacity=0.2)
        run3_rect.move_to(squares[7].get_center())
        run3_label = Text("Natural Run", color=TEAL).scale(0.4).next_to(run3_rect, DOWN)

        # Animations
        self.add(title)
        self.play(Create(squares), Write(numbers), run_time=2)
        self.wait(1)
        
        self.play(
            Create(run1_rect), Write(run1_label),
            Create(run3_rect), Write(run3_label),
            run_time=2
        )
        self.wait(1)
        
        self.play(Create(run2_rect), Write(run2_label), run_time=1.5)
        self.wait(1)
        
        # Expansion Animation
        expansion_text = Text("Expand to Min-Run Length", color=YELLOW).scale(0.5)
        expansion_text.to_edge(DOWN, buff=1.0)
        
        new_run2_rect = Rectangle(width=2.8, height=1.0, color=BLUE, fill_opacity=0.3)
        new_run2_rect.move_to(squares[4].get_center())
        fixed_run_label = Text("Fixed Run", color=BLUE).scale(0.4).next_to(new_run2_rect, DOWN)
        
        self.play(
            ReplacementTransform(run2_rect, new_run2_rect),
            ReplacementTransform(run2_label, fixed_run_label),
            Write(expansion_text),
            run_time=2
        )
        
        arrow = Arrow(start=expansion_text.get_top(), end=new_run2_rect.get_bottom(), color=YELLOW)
        self.play(Create(arrow), run_time=1)
        self.wait(2)

        # Cleanup
        self.play(
            FadeOut(arrow),
            FadeOut(expansion_text),
            FadeOut(run1_label),
            FadeOut(fixed_run_label),
            FadeOut(run3_label),
            run_time=1
        )
        self.wait(1)

        # Final state check
        self.play(
            new_run2_rect.animate.set_stroke(width=5),
            run1_rect.animate.set_stroke(width=5),
            run3_rect.animate.set_stroke(width=5),
            run_time=1
        )
        self.wait(2)