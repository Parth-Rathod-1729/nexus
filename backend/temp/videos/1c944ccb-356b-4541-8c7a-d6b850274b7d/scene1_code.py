from manim import *

class Scene1(Scene):
    def construct(self):
        # 1. Title and setup
        title = Text("Identifying Runs and the Stack", font_size=36, color=WHITE).to_edge(UP, buff=0.5)
        
        # 2. Stack Container (Vertical)
        stack_box = Rectangle(height=4.5, width=1.5, color=WHITE).to_edge(LEFT, buff=1.5)
        stack_label = Text("Run Stack", font_size=24).next_to(stack_box, UP)
        
        # 3. Horizontal Array
        array_rects = VGroup(*[Rectangle(width=0.5, height=0.5, color=WHITE) for _ in range(9)])
        array_rects.arrange(RIGHT, buff=0.1).move_to(RIGHT * 2.5 + UP * 0.5)
        array_label = Text("Input Data", font_size=24).next_to(array_rects, UP)

        self.play(Write(title))
        self.play(Create(stack_box), Write(stack_label), Create(array_rects), Write(array_label))
        self.wait(1)

        # Define Runs
        # Run 1: Indices 0-2 (length 3) - BLUE
        # Run 2: Indices 3-4 (length 2) - GREEN
        # Run 3: Indices 5-8 (length 4) - TEAL

        # Run 1 Animation
        run1_highlight = array_rects[0:3]
        run1_stack_obj = Rectangle(width=1.3, height=0.8, fill_color=BLUE, fill_opacity=0.8, color=BLUE)
        run1_stack_obj.move_to(run1_highlight.get_center())
        
        self.play(run1_highlight.animate.set_fill(BLUE, fill_opacity=0.5))
        self.play(run1_stack_obj.animate.move_to(stack_box.get_bottom() + UP * 0.5))
        
        # Run 2 Animation
        run2_highlight = array_rects[3:5]
        run2_stack_obj = Rectangle(width=1.3, height=0.6, fill_color=GREEN, fill_opacity=0.8, color=GREEN)
        run2_stack_obj.move_to(run2_highlight.get_center())
        
        self.play(run2_highlight.animate.set_fill(GREEN, fill_opacity=0.5))
        self.play(run2_stack_obj.animate.move_to(run1_stack_obj.get_top() + UP * 0.4))
        
        # Run 3 Animation
        run3_highlight = array_rects[5:9]
        run3_stack_obj = Rectangle(width=1.3, height=1.0, fill_color=TEAL, fill_opacity=0.8, color=TEAL)
        run3_stack_obj.move_to(run3_highlight.get_center())
        
        self.play(run3_highlight.animate.set_fill(TEAL, fill_opacity=0.5))
        self.play(run3_stack_obj.animate.move_to(run2_stack_obj.get_top() + UP * 0.6))

        # Add Arrows to show movement direction
        arrow = Arrow(start=RIGHT * 1, end=LEFT * 0.5, color=YELLOW)
        arrow.next_to(stack_box, RIGHT, buff=0.5)
        push_text = Text("Push Run", font_size=20, color=YELLOW).next_to(arrow, UP)
        
        self.play(Create(arrow), Write(push_text))
        self.wait(2)

        # Final Cleanup for scene ending
        self.play(FadeOut(arrow), FadeOut(push_text), FadeOut(title))
        self.wait(1)