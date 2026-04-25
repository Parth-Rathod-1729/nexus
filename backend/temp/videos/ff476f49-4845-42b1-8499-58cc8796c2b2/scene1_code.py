from manim import *

class Scene1(Scene):
    def construct(self):
        # 0. Title and Concept
        title = Text("Understanding AI Agents", font_size=48, color=GOLD)
        concept = Text("Definition and Core Components of an AI Agent", font_size=30, color=BLUE)
        concept.next_to(title, DOWN, buff=0.8)

        self.play(Write(title))
        self.play(Write(concept))
        self.wait(1.5)

        # Shrink and move title/concept to make space for the main diagram
        self.play(
            title.animate.to_edge(UP).scale(0.7),
            concept.animate.next_to(title, DOWN, buff=0.3).scale(0.8),
            run_time=1.5
        )
        self.wait(0.5)

        # 1. Central AI AGENT
        agent_label = Text("AI AGENT", font_size=40, color=WHITE)
        agent_box = Square(side_length=2.5, color=TEAL, fill_opacity=0.7)
        agent_box.move_to(ORIGIN)
        agent_label.move_to(agent_box.get_center()) # Center label inside the box
        
        agent_group = VGroup(agent_box, agent_label)

        self.play(Create(agent_box), Write(agent_label))
        self.wait(1)

        # 2. Key Components of AI Agents (Internal Properties)
        brain_text = Text("Brain (Model)", font_size=24, color=BLUE)
        perception_comp_text = Text("Perception System", font_size=24, color=BLUE)
        action_comp_text = Text("Action/Tools Module", font_size=24, color=BLUE)
        memory_text = Text("Memory", font_size=24, color=BLUE)

        # Arrange these components around the agent_group
        brain_text.move_to(agent_group.get_center() + LEFT * 3.5 + UP * 2)
        perception_comp_text.move_to(agent_group.get_center() + RIGHT * 3.5 + UP * 2)
        action_comp_text.move_to(agent_group.get_center() + RIGHT * 3.5 + DOWN * 2)
        memory_text.move_to(agent_group.get_center() + LEFT * 3.5 + DOWN * 2)

        # Arrows pointing from components to the agent's general area (corners)
        arrow_brain = Arrow(start=brain_text.get_right(), end=agent_group.get_corner(UL), buff=0.1, color=WHITE, stroke_width=3)
        arrow_perception_comp = Arrow(start=perception_comp_text.get_left(), end=agent_group.get_corner(UR), buff=0.1, color=WHITE, stroke_width=3)
        arrow_action_comp = Arrow(start=action_comp_text.get_left(), end=agent_group.get_corner(DR), buff=0.1, color=WHITE, stroke_width=3)
        arrow_memory = Arrow(start=memory_text.get_right(), end=agent_group.get_corner(DL), buff=0.1, color=WHITE, stroke_width=3)
        
        component_group = VGroup(
            brain_text, perception_comp_text, action_comp_text, memory_text,
            arrow_brain, arrow_perception_comp, arrow_action_comp, arrow_memory
        )

        self.play(
            LaggedStart(
                Write(brain_text), Create(arrow_brain),
                Write(perception_comp_text), Create(arrow_perception_comp),
                Write(action_comp_text), Create(arrow_action_comp),
                Write(memory_text), Create(arrow_memory),
                lag_ratio=0.5 # Staggered animation for clarity
            )
        )
        self.wait(1.5)

        # 3. Agent's Process Flow (Perceive -> Decide -> Act -> Goal)
        perceive_text = Text("Perceive Environment", font_size=28, color=GREEN)
        decide_text = Text("Make Decisions", font_size=28, color=GREEN)
        actions_text = Text("Take Actions", font_size=28, color=GREEN)
        goal_text = Text("Achieve Goal", font_size=28, color=GREEN)

        # Position these process steps around the agent, outside the components
        perceive_text.next_to(agent_group, LEFT, buff=3.0)
        decide_text.next_to(agent_group, UP, buff=2.5)
        actions_text.next_to(agent_group, RIGHT, buff=3.0)
        goal_text.next_to(agent_group, DOWN, buff=2.5)

        # Arrows for the circular flow
        arrow1 = Arrow(start=agent_group.get_edge_center(LEFT), end=perceive_text.get_right(), buff=0.1, color=YELLOW, stroke_width=4)
        arrow2 = Arrow(start=perceive_text.get_edge_center(UP), end=decide_text.get_edge_center(LEFT), buff=0.1, color=YELLOW, stroke_width=4)
        arrow3 = Arrow(start=decide_text.get_edge_center(RIGHT), end=actions_text.get_edge_center(UP), buff=0.1, color=YELLOW, stroke_width=4)
        arrow4 = Arrow(start=actions_text.get_edge_center(DOWN), end=goal_text.get_edge_center(RIGHT), buff=0.1, color=YELLOW, stroke_width=4)
        
        process_flow_group = VGroup(
            perceive_text, decide_text, actions_text, goal_text,
            arrow1, arrow2, arrow3, arrow4
        )

        self.play(
            LaggedStart(
                Write(perceive_text), Create(arrow1),
                Write(decide_text), Create(arrow2),
                Write(actions_text), Create(arrow3),
                Write(goal_text), Create(arrow4),
                lag_ratio=0.1 # Faster animation for the flow
            )
        )
        self.wait(1.5)

        # 4. Highlight Autonomy
        autonomy_text = Text("Autonomy", font_size=32, color=RED)
        autonomy_text.next_to(goal_text, DOWN, buff=0.5)
        autonomy_box = Square(color=RED, fill_opacity=0.2).surround(autonomy_text, stretch=1.2)
        autonomy_group = VGroup(autonomy_box, autonomy_text)

        self.play(FadeIn(autonomy_box), Write(autonomy_text))
        self.wait(2)

        # Final cleanup: Fade out all mobjects
        self.play(FadeOut(VGroup(
            agent_group, component_group, process_flow_group, autonomy_group, title, concept
        )))
        self.wait(1)