from manim import *

class Scene2(Scene):
    def construct(self):
        # Title
        title = Text("Percept Sequence & Agent Function", color=WHITE).scale(0.8).to_edge(UP)
        self.play(Write(title))

        # Percept Sequence Components (Left side)
        sequence_rect = Rectangle(width=4.5, height=1.5, color=BLUE)
        sequence_rect.shift(LEFT * 4 + DOWN * 0.5)
        sequence_label = Text("Percept Sequence", font_size=24, color=BLUE).next_to(sequence_rect, UP)
        
        p1 = Square(side_length=0.6, color=YELLOW, fill_opacity=0.5).move_to(sequence_rect.get_left() + RIGHT * 0.7)
        p2 = Square(side_length=0.6, color=YELLOW, fill_opacity=0.5).next_to(p1, RIGHT, buff=0.2)
        p3 = Square(side_length=0.6, color=YELLOW, fill_opacity=0.5).next_to(p2, RIGHT, buff=0.2)
        p_dots = Text("...", font_size=30).next_to(p3, RIGHT, buff=0.2)
        
        sequence_group = VGroup(sequence_rect, sequence_label, p1, p2, p3, p_dots)

        # Agent Function (Center)
        agent_circle = Circle(radius=0.8, color=TEAL, fill_opacity=0.2)
        agent_circle.shift(DOWN * 0.5)
        func_math = MathTex("f(P^*)", color=TEAL).move_to(agent_circle.get_center())
        func_label = Text("Agent Function", font_size=24, color=TEAL).next_to(agent_circle, UP)
        
        agent_group = VGroup(agent_circle, func_math, func_label)

        # Resulting Action (Right side)
        action_rect = Rectangle(width=2.5, height=1.5, color=GREEN)
        action_rect.shift(RIGHT * 4.5 + DOWN * 0.5)
        action_label = Text("Action", font_size=24, color=GREEN).next_to(action_rect, UP)
        action_text = Text("Move / Pick", font_size=20, color=WHITE).move_to(action_rect.get_center())
        
        action_group = VGroup(action_rect, action_label, action_text)

        # Arrows
        arrow1 = Arrow(sequence_rect.get_right(), agent_circle.get_left(), color=WHITE, buff=0.1)
        arrow2 = Arrow(agent_circle.get_right(), action_rect.get_left(), color=WHITE, buff=0.1)

        # Animations
        self.play(Create(sequence_rect), Write(sequence_label))
        self.play(FadeIn(p1, shift=RIGHT), FadeIn(p2, shift=RIGHT), FadeIn(p3, shift=RIGHT), Write(p_dots))
        self.wait(1)

        self.play(Create(agent_circle), Write(func_label), Write(func_math))
        self.play(Create(arrow1))
        self.wait(1)

        self.play(Create(action_rect), Write(action_label))
        self.play(Create(arrow2))
        self.play(Write(action_text))
        
        # Highlight mapping
        mapping_math = MathTex("f: P^* \\rightarrow A", color=GOLD).to_edge(DOWN, buff=0.5)
        self.play(Write(mapping_math))
        self.play(mapping_math.animate.scale(1.2), run_time=1)
        self.play(mapping_math.animate.scale(1.0), run_time=1)

        self.wait(2)

        # Clean up
        self.play(
            FadeOut(sequence_group),
            FadeOut(agent_group),
            FadeOut(action_group),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(mapping_math),
            FadeOut(title)
        )