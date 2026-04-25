from manim import *

class Scene2(Scene):
    def construct(self):
        # Title
        title = Text("Percept Sequence & Agent Function", color=BLUE).scale(0.8)
        title.to_edge(UP)

        # Percept Sequence Components
        p1 = Text("P1", color=WHITE).scale(0.6)
        p2 = Text("P2", color=WHITE).scale(0.6)
        p3 = Text("P3", color=WHITE).scale(0.6)
        dots = Text("...", color=WHITE).scale(0.6)
        pn = Text("Pn", color=WHITE).scale(0.6)
        
        percept_list = VGroup(p1, p2, p3, dots, pn).arrange(RIGHT, buff=0.3)
        percept_bg = Rectangle(width=3.5, height=1, color=TEAL).set_fill(TEAL, fill_opacity=0.1)
        percept_label = Text("Percept Sequence", color=TEAL).scale(0.4).next_to(percept_bg, UP)
        percept_group = VGroup(percept_bg, percept_list, percept_label).to_edge(LEFT, buff=0.5)

        # Agent Function Box
        agent_box = Rectangle(width=3, height=2, color=GOLD).set_fill(GOLD, fill_opacity=0.1)
        agent_text = Text("Agent\nFunction", color=GOLD).scale(0.6).move_to(agent_box.get_center())
        agent_group = VGroup(agent_box, agent_text).move_to(ORIGIN)

        # Action Output
        action_circle = Circle(radius=0.8, color=GREEN).set_fill(GREEN, fill_opacity=0.1)
        action_text = Text("Action", color=GREEN).scale(0.6).move_to(action_circle.get_center())
        action_group = VGroup(action_circle, action_text).to_edge(RIGHT, buff=0.8)

        # Arrows
        arrow1 = Arrow(percept_group.get_right(), agent_group.get_left(), color=WHITE, buff=0.1)
        arrow2 = Arrow(agent_group.get_right(), action_group.get_left(), color=WHITE, buff=0.1)

        # Mathematical mapping representation
        mapping_text = MathTex("f: P^* \\rightarrow A", color=YELLOW).scale(0.8)
        mapping_text.next_to(agent_group, DOWN, buff=0.5)

        # Animations
        self.play(Write(title))
        self.play(
            Create(percept_bg),
            Write(percept_list),
            Write(percept_label),
            run_time=2
        )
        self.wait(1)

        self.play(
            Create(agent_box),
            Write(agent_text),
            Create(arrow1),
            run_time=2
        )
        
        self.play(
            Create(action_circle),
            Write(action_text),
            Create(arrow2),
            run_time=2
        )

        self.play(Write(mapping_text))
        self.wait(2)

        # Final Highlight
        self.play(
            agent_box.animate.set_fill(GOLD, fill_opacity=0.4),
            action_circle.animate.set_fill(GREEN, fill_opacity=0.4),
            run_time=1
        )
        self.wait(2)