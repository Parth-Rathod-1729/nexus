from manim import *

class Scene2(Scene):
    def construct(self):
        # 1. Environment Setup (Grid-like rooms A and B)
        room_a = Square(side_length=2, color=WHITE).shift(LEFT * 1.5 + UP * 1.2)
        room_b = Square(side_length=2, color=WHITE).next_to(room_a, RIGHT, buff=0.1)
        
        label_a = Text("Room A", font_size=24, color=WHITE).next_to(room_a, UP)
        label_b = Text("Room B", font_size=24, color=WHITE).next_to(room_b, UP)
        
        # 2. Agent and Dirt
        agent = Circle(radius=0.4, color=BLUE, fill_opacity=0.8).move_to(room_a.get_center())
        dirt = Dot(radius=0.15, color=GOLD).move_to(room_a.get_center() + DOWN * 0.4)
        
        # 3. Titles and Headings
        title = Text("Agent Function: Mapping Percepts to Actions", font_size=32, color=YELLOW).to_edge(UP)
        
        # 4. Agent Function Table / Mapping Visualization
        table_box = Rectangle(width=8, height=2.5, color=TEAL).shift(DOWN * 2)
        table_header = Text("Percept Sequence  ->  Action", font_size=28, color=TEAL).move_to(table_box.get_top() + DOWN * 0.4)
        
        mapping_1 = MathTex(r"[\text{A, Dirty}]", r"\rightarrow", r"\text{Suck}", font_size=34).move_to(table_box.get_center() + UP * 0.2)
        mapping_1.set_color_by_tex("Suck", RED)
        
        mapping_2 = MathTex(r"[\text{A, Clean}]", r"\rightarrow", r"\text{Move Right}", font_size=34).move_to(table_box.get_center() + DOWN * 0.6)
        mapping_2.set_color_by_tex("Move Right", GREEN)

        # Execution of Animations
        self.play(Create(VGroup(room_a, room_b)), Write(VGroup(label_a, label_b, title)))
        self.play(Create(agent), Create(dirt))
        self.wait(1)
        
        self.play(Create(table_box), Write(table_header))
        
        # Rule 1
        self.play(mapping_1.animate.set_color(WHITE), run_time=1)
        self.play(Indicate(mapping_1))
        self.play(dirt.animate.scale(0), run_time=0.5) # Action "Suck"
        self.remove(dirt)
        self.wait(1)
        
        # Rule 2
        self.play(Write(mapping_2))
        self.play(Indicate(mapping_2))
        self.play(agent.animate.move_to(room_b.get_center()), run_time=1.5) # Action "Move Right"
        
        self.wait(2)

        # Final cleanup for smooth ending
        self.play(FadeOut(VGroup(room_a, room_b, label_a, label_b, agent, table_box, table_header, mapping_1, mapping_2, title)))