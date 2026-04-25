from manim import *

class Scene2(Scene):
    def construct(self):
        # Title
        title = Text("Percepts and Agent Function", color=WHITE, font_size=36).to_edge(UP)
        
        # Percept History Components
        history_box = Rectangle(height=3, width=4, color=TEAL, fill_opacity=0.1)
        history_box.to_edge(LEFT, buff=1)
        history_label = Text("Percept History", font_size=24, color=TEAL).next_to(history_box, UP)
        
        p1 = Text("1. [Loc A, Clean]", font_size=18).move_to(history_box.get_center() + UP * 0.8)
        p2 = Text("2. [Loc A, Dirty]", font_size=18).next_to(p1, DOWN, buff=0.3)
        p3 = Text("3. [Loc B, Dirty]", font_size=18).next_to(p2, DOWN, buff=0.3)
        history_content = VGroup(p1, p2, p3)
        history_grp = VGroup(history_box, history_label, history_content)

        # Agent Function (The Brain)
        brain_box = Square(side_length=2, color=BLUE, fill_opacity=0.2)
        brain_box.move_to(RIGHT * 1)
        brain_label = Text("Agent\nFunction", font_size=22, color=WHITE).move_to(brain_box.get_center())
        brain_grp = VGroup(brain_box, brain_label)

        # Connect Percept History to Brain
        arrow_to_brain = Arrow(history_box.get_right(), brain_box.get_left(), color=YELLOW)

        # Action Output
        action_box = Rectangle(height=1.5, width=2.5, color=GREEN, fill_opacity=0.2)
        action_box.to_edge(RIGHT, buff=1)
        action_text = Text("Action:\nSuck", font_size=22, color=GREEN).move_to(action_box.get_center())
        action_grp = VGroup(action_box, action_text)
        
        arrow_to_action = Arrow(brain_box.get_right(), action_box.get_left(), color=YELLOW)

        # Animation sequence 1: Mapping Process
        self.play(Write(title))
        self.wait(1)
        self.play(Create(history_grp), Create(brain_grp))
        self.play(Create(arrow_to_brain))
        self.wait(1)
        self.play(Create(arrow_to_action), Create(action_grp))
        self.wait(2)

        # Animation sequence 2: The Concept of a Mapping Table
        self.play(FadeOut(history_grp), FadeOut(brain_grp), FadeOut(action_grp), FadeOut(arrow_to_brain), FadeOut(arrow_to_action))
        
        table_title = Text("Mapping: Percept -> Action", font_size=32, color=GOLD).move_to(UP * 1.5)
        
        line1 = Text("[A, Dirty]  ----->  Suck", font_size=26).move_to(UP * 0.5)
        line2 = Text("[A, Clean]  ----->  Right", font_size=26).next_to(line1, DOWN, buff=0.5)
        line3 = Text("[B, Dirty]  ----->  Suck", font_size=26).next_to(line2, DOWN, buff=0.5)
        
        table_content = VGroup(line1, line2, line3)
        
        self.play(Write(table_title))
        self.play(Write(table_content))
        self.wait(3)

        # Closing
        self.play(FadeOut(table_title), FadeOut(table_content), FadeOut(title))
        self.wait(1)