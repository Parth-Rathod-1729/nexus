from manim import *

class Scene3(Scene):
    def construct(self):
        # --- UI Elements ---
        title = Text("Rationality & Performance", color=GOLD, font_size=36).to_edge(UP)
        explanation = Text("Agent maximizes performance measure", font_size=24).next_to(title, DOWN)
        
        # Squares A and B
        square_a = Square(side_length=2, color=WHITE).shift(LEFT * 3 + DOWN * 0.5)
        square_b = Square(side_length=2, color=WHITE).shift(RIGHT * 3 + DOWN * 0.5)
        label_a = Text("A", font_size=28).next_to(square_a, DOWN)
        label_b = Text("B", font_size=28).next_to(square_b, DOWN)
        
        # Dirt representation
        dirt_a = Dot(square_a.get_center() + UP * 0.3, color=TEAL, radius=0.2)
        dirt_b = Dot(square_b.get_center() + UP * 0.3, color=TEAL, radius=0.2)
        
        # Scoreboard
        score_rect = Rectangle(height=1.2, width=3.5, color=WHITE).to_corner(UP + RIGHT)
        score_title = Text("Performance:", font_size=20).move_to(score_rect.get_center() + UP * 0.3)
        score_val = Text("0", color=YELLOW, font_size=36).move_to(score_rect.get_center() + DOWN * 0.2)
        score_group = VGroup(score_rect, score_title, score_val)

        # Agent (Vacuum)
        agent = Circle(radius=0.5, color=BLUE, fill_opacity=0.8).move_to(square_a.get_center())
        agent_label = Text("Agent", font_size=20).move_to(agent.get_center())
        agent_vgroup = VGroup(agent, agent_label)

        # --- Animations ---
        self.add(title, explanation)
        self.play(
            Create(square_a), 
            Create(square_b), 
            Write(label_a), 
            Write(label_b),
            Create(score_group)
        )
        self.play(FadeIn(dirt_a), FadeIn(dirt_b))
        self.play(FadeIn(agent_vgroup))
        self.wait(1)

        # Action 1: Clean A
        new_score_1 = Text("1", color=YELLOW, font_size=36).move_to(score_val.get_center())
        self.play(
            FadeOut(dirt_a),
            Transform(score_val, new_score_1),
            agent_vgroup.animate.scale(1.1).set_color(GREEN),
            run_time=1
        )
        self.play(agent_vgroup.animate.scale(1/1.1).set_color(BLUE))

        # Action 2: Move to B
        self.play(agent_vgroup.animate.move_to(square_b.get_center()), run_time=1.5)

        # Action 3: Clean B
        new_score_2 = Text("2", color=YELLOW, font_size=36).move_to(score_val.get_center())
        self.play(
            FadeOut(dirt_b),
            Transform(score_val, new_score_2),
            agent_vgroup.animate.scale(1.1).set_color(GREEN),
            run_time=1
        )
        self.play(agent_vgroup.animate.scale(1/1.1).set_color(BLUE))

        # Conclusion text
        conclusion = Text("Rational Action = High Score", color=GOLD, font_size=32).move_to(DOWN * 3)
        self.play(Write(conclusion))
        self.wait(2)