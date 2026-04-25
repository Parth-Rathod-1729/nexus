from manim import *

class Scene3(Scene):
    def construct(self):
        # 1. Environment Setup
        room_a = Square(side_length=3, color=WHITE).shift(LEFT * 2)
        room_b = Square(side_length=3, color=WHITE).shift(RIGHT * 2)
        label_a = Text("Room A", font_size=24).next_to(room_a, UP)
        label_b = Text("Room B", font_size=24).next_to(room_b, UP)
        
        rooms = VGroup(room_a, room_b, label_a, label_b)
        
        # 2. Agent and Environment State
        vacuum = Circle(radius=0.6, color=BLUE, fill_opacity=0.8).move_to(room_a.get_center())
        vacuum_label = Text("Agent", font_size=18, color=WHITE).move_to(vacuum.get_center())
        agent = VGroup(vacuum, vacuum_label)
        
        dirt_group = VGroup(
            Dot(room_a.get_center() + UP * 0.4 + LEFT * 0.3, color=GOLD, radius=0.1),
            Dot(room_a.get_center() + DOWN * 0.5 + RIGHT * 0.2, color=GOLD, radius=0.12),
            Dot(room_a.get_center() + LEFT * 0.5, color=GOLD, radius=0.08)
        )
        
        # 3. Informational Text
        title = Text("Rational Agent Function", color=TEAL).to_edge(UP, buff=0.3)
        percept_box = Rectangle(width=4, height=1, color=WHITE).to_edge(DOWN, buff=0.5)
        percept_label = Text("Percept: [A, Dirty]", font_size=22).move_to(percept_box.get_center())
        action_label = Text("Action: Suck", font_size=28, color=YELLOW).next_to(percept_box, UP)

        # 4. Animation Sequence
        self.play(Create(rooms), Write(title))
        self.play(FadeIn(agent), FadeIn(dirt_group))
        self.wait(1)
        
        # Perception phase
        self.play(Create(percept_box), Write(percept_label))
        self.play(percept_label.animate.set_color(YELLOW))
        self.wait(1)
        
        # Rational action phase
        self.play(Write(action_label))
        self.play(
            agent.animate.scale(1.2),
            dirt_group.animate.scale(0),
            run_time=1
        )
        self.play(agent.animate.scale(1/1.2))
        self.remove(dirt_group)
        
        # Show logic: Move to next room
        new_percept = Text("Percept: [A, Clean]", font_size=22).move_to(percept_box.get_center())
        new_action = Text("Action: Move Right", font_size=28, color=YELLOW).move_to(action_label.get_center())
        
        self.play(
            Transform(percept_label, new_percept),
            Transform(action_label, new_action)
        )
        
        self.play(
            agent.animate.move_to(room_b.get_center()),
            run_time=1.5
        )
        
        # Final confirmation of rationality
        rationality_desc = Text("Maximizing Performance", font_size=24, color=GREEN).next_to(title, DOWN)
        self.play(Write(rationality_desc))
        self.wait(2)