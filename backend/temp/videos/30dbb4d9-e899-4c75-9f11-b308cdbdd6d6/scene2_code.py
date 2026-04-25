from manim import *

class Scene2(Scene):
    def construct(self):
        # Title
        title = Text("Percepts and Agent Function", color=BLUE, font_size=36)
        title.to_edge(UP, buff=0.5)
        
        # Percept History representation
        p1 = Circle(radius=0.3, color=TEAL, fill_opacity=0.6)
        p2 = Circle(radius=0.3, color=TEAL, fill_opacity=0.6)
        p3 = Circle(radius=0.3, color=TEAL, fill_opacity=0.6)
        dots = Text("...", font_size=30)
        
        percept_group = VGroup(p1, p2, p3, dots).arrange(RIGHT, buff=0.3)
        percept_group.move_to(LEFT * 4)
        
        percept_label = Text("Percept History", font_size=24, color=WHITE)
        percept_label.next_to(percept_group, UP)
        
        # Agent Function Box
        box = Rectangle(height=2, width=3.5, color=GOLD, fill_opacity=0.2)
        box.move_to(ORIGIN)
        
        box_label = Text("Agent Function", font_size=24, color=GOLD)
        box_label.next_to(box, UP)
        
        math_logic = MathTex(r"f: P^* \rightarrow A", color=WHITE)
        math_logic.move_to(box.get_center())
        
        # Action Output
        action_box = Square(side_length=1.2, color=RED, fill_opacity=0.4)
        action_box.move_to(RIGHT * 4.5)
        
        action_text = Text("Action", font_size=24, color=WHITE)
        action_text.move_to(action_box.get_center())
        
        # Connectors
        arrow_in = Arrow(percept_group.get_right(), box.get_left(), color=WHITE, buff=0.1)
        arrow_out = Arrow(box.get_right(), action_box.get_left(), color=WHITE, buff=0.1)
        
        # Animation sequence
        self.play(Write(title))
        self.wait(1)
        
        self.play(
            Create(percept_group),
            Write(percept_label)
        )
        self.wait(1)
        
        self.play(
            Create(box),
            Write(box_label),
            Write(math_logic)
        )
        self.play(GrowArrow(arrow_in))
        self.wait(1)
        
        self.play(
            GrowArrow(arrow_out),
            Create(action_box),
            Write(action_text)
        )
        self.wait(2)
        
        # Summary highlight
        explanation = Text("Maps Percept Sequence to Action", font_size=20, color=YELLOW)
        explanation.to_edge(DOWN, buff=1)
        self.play(Write(explanation))
        self.wait(2)

        # Clear for clean exit
        self.play(
            FadeOut(percept_group),
            FadeOut(percept_label),
            FadeOut(box),
            FadeOut(box_label),
            FadeOut(math_logic),
            FadeOut(arrow_in),
            FadeOut(arrow_out),
            FadeOut(action_box),
            FadeOut(action_text),
            FadeOut(explanation),
            FadeOut(title)
        )