from manim import *

class Scene3(Scene):
    def construct(self):
        # Scene title and setup
        title = Text("The Galloping Strategy", color=GOLD)
        title.to_edge(UP)
        
        explanation = Text("Exponential search skips multiple elements", font_size=24, color=WHITE)
        explanation.next_to(title, DOWN)
        
        # Create Left Block (Sorted Run 1)
        l_nums = [10, 20, 30, 40, 50]
        l_run = VGroup()
        for val in l_nums:
            sq = Square(side_length=0.8, color=BLUE, fill_opacity=0.4)
            txt = MathTex(str(val))
            item = VGroup(sq, txt)
            l_run.add(item)
        l_run.arrange(RIGHT, buff=0.2)
        l_run.move_to([-1.5, 0, 0])
        
        # Create Right Block (Sorted Run 2)
        r_nums = [35, 60, 70]
        r_run = VGroup()
        for val in r_nums:
            sq = Square(side_length=0.8, color=TEAL, fill_opacity=0.4)
            txt = MathTex(str(val))
            item = VGroup(sq, txt)
            r_run.add(item)
        r_run.arrange(RIGHT, buff=0.2)
        r_run.next_to(l_run, RIGHT, buff=2.0)
        
        # Draw initial state
        self.play(Write(title), Write(explanation))
        self.play(Create(l_run), Create(r_run))
        self.wait(1)
        
        # Define the galloper (the first element of the right run)
        galloper = r_run[0]
        
        # Calculate target position between 30 (index 2) and 40 (index 3)
        target_x = (l_run[2].get_x() + l_run[3].get_x()) / 2
        
        # Visual leap indicator
        leap_arrow = Arrow(
            start=galloper.get_top(),
            end=[target_x, 1.5, 0],
            color=YELLOW,
            buff=0.1
        )
        
        # Show the leap strategy
        self.play(Create(leap_arrow))
        
        # Group the elements that need to shift right to make space
        shift_group = VGroup(*l_run[3:], *r_run[1:])
        
        # The Leap Animation (Galloping)
        self.play(
            galloper.animate.move_to([target_x, 1.5, 0]),
            shift_group.animate.shift(RIGHT * 1.0),
            run_time=1.5
        )
        
        # Finalize the position
        self.play(
            galloper.animate.move_to([target_x, 0, 0]),
            leap_arrow.animate.set_stroke(opacity=0),
            run_time=1
        )
        
        # Highlight efficiency
        efficiency_text = Text("Reduces total comparisons", color=GREEN, font_size=28)
        efficiency_text.to_edge(DOWN, buff=1.0)
        
        self.play(Write(efficiency_text))
        
        # Visual check: highlight the gap filled
        highlight_rect = Rectangle(
            width=1.0, 
            height=1.0, 
            color=YELLOW, 
            stroke_width=4
        ).move_to(galloper.get_center())
        
        self.play(Create(highlight_rect))
        self.play(highlight_rect.animate.set_stroke(opacity=0), run_time=1)
        
        self.wait(2)