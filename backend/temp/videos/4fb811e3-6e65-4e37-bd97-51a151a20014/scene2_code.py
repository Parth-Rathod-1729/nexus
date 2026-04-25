from manim import *

class Scene2(Scene):
    def construct(self):
        # Title of the scene
        title = Text("The Agent Function", color=BLUE).to_edge(UP)
        
        # Percept Sequence Section
        seq_label = Text("Percept Sequence", font_size=28, color=YELLOW).move_to([-4, 1.5, 0])
        
        # Creating a stack of history inputs
        p1_rect = Rectangle(height=0.7, width=2.8, color=TEAL, fill_opacity=0.3).move_to([-4, 0.5, 0])
        p1_txt = Text("Room A: Dirty", font_size=18).move_to(p1_rect.get_center())
        p1 = VGroup(p1_rect, p1_txt)
        
        p2_rect = Rectangle(height=0.7, width=2.8, color=TEAL, fill_opacity=0.3).next_to(p1, DOWN, buff=0.2)
        p2_txt = Text("Room B: Clean", font_size=18).move_to(p2_rect.get_center())
        p2 = VGroup(p2_rect, p2_txt)
        
        percept_stack = VGroup(p1, p2)
        
        # Agent Function Representation (The Brain/Logic)
        agent_sq = Square(side_length=2.2, color=GOLD, fill_opacity=0.2).move_to([0, -0.3, 0])
        agent_txt = Text("Agent\nFunction", font_size=24, color=GOLD).move_to(agent_sq.get_center())
        agent_func = VGroup(agent_sq, agent_txt)
        
        # Mathematical representation text (Replaced MathTex with Text to avoid subprocess errors)
        math_map = Text("f: P* -> A", font_size=32, color=WHITE).next_to(agent_sq, UP, buff=0.3)
        
        # Output Action Section
        action_rect = Rectangle(height=0.8, width=2.8, color=RED, fill_opacity=0.3).move_to([4.5, -0.3, 0])
        action_txt = Text("Action: Suck", font_size=22, color=WHITE).move_to(action_rect.get_center())
        action_group = VGroup(action_rect, action_txt)
        
        # Connective Arrows
        arrow1 = Arrow(start=percept_stack.get_right(), end=agent_sq.get_left(), color=WHITE, buff=0.1)
        arrow2 = Arrow(start=agent_sq.get_right(), end=action_group.get_left(), color=WHITE, buff=0.1)
        
        # Animation sequence
        self.play(Write(title))
        self.wait(1)
        
        self.play(
            Write(seq_label),
            Create(percept_stack),
            run_time=2
        )
        
        self.play(
            Create(agent_func),
            Write(math_map),
            run_time=1.5
        )
        
        self.play(Create(arrow1))
        self.wait(1)
        
        self.play(
            Create(arrow2),
            Create(action_group),
            run_time=1.5
        )
        
        self.wait(3)