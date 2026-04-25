from manim import *

class Scene3(Scene):
    def construct(self):
        # 1. Setup Rooms and Environment
        room_a = Square(side_length=3, color=WHITE).move_to(LEFT * 2)
        room_b = Square(side_length=3, color=WHITE).move_to(RIGHT * 2)
        
        label_a = Text("Room A", font_size=24).next_to(room_a, DOWN)
        label_b = Text("Room B", font_size=24).next_to(room_b, DOWN)
        
        rooms = VGroup(room_a, room_b, label_a, label_b)
        
        # 2. Performance Measure (Score)
        title = Text("Rationality: Maximize Performance", font_size=32, color=TEAL).to_edge(UP)
        score_val = 0
        score_txt = Text(f"Score: {score_val}", font_size=36, color=YELLOW).next_to(title, DOWN)
        
        # 3. Agent and Dirt
        dirt_a = Dot(point=room_a.get_center() + UP * 0.5, color=GOLD, radius=0.2)
        dirt_b = Dot(point=room_b.get_center() + UP * 0.5, color=GOLD, radius=0.2)
        
        agent_body = Circle(radius=0.4, color=BLUE, fill_opacity=0.8)
        agent_handle = Rectangle(height=0.1, width=0.5, color=BLUE, fill_opacity=1).move_to(agent_body.get_top())
        agent = VGroup(agent_body, agent_handle).move_to(room_a.get_center() + DOWN * 0.5)
        
        # 4. Display Initial Scene
        self.play(Write(title))
        self.play(Create(rooms), Write(score_txt))
        self.play(FadeIn(dirt_a), FadeIn(dirt_b), FadeIn(agent))
        self.wait(1)
        
        # 5. Action 1: Detect and Clean Room A
        self.play(agent.animate.move_to(dirt_a.get_center()), run_time=1)
        self.play(FadeOut(dirt_a))
        
        score_val += 10
        score_txt_2 = Text(f"Score: {score_val}", font_size=36, color=YELLOW).move_to(score_txt.get_center())
        self.play(Transform(score_txt, score_txt_2))
        self.wait(1)
        
        # 6. Action 2: Move to Room B
        arrow_move = Arrow(start=room_a.get_center(), end=room_b.get_center(), color=WHITE)
        self.play(Create(arrow_move))
        self.play(agent.animate.move_to(room_b.get_center() + DOWN * 0.5), FadeOut(arrow_move))
        
        # 7. Action 3: Clean Room B
        self.play(agent.animate.move_to(dirt_b.get_center()), run_time=1)
        self.play(FadeOut(dirt_b))
        
        score_val += 10
        score_txt_3 = Text(f"Score: {score_val}", font_size=36, color=YELLOW).move_to(score_txt.get_center())
        self.play(Transform(score_txt, score_txt_3))
        
        # 8. Final Statement
        conclusion = Text("Action based on Percepts", font_size=28, color=GREEN).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)