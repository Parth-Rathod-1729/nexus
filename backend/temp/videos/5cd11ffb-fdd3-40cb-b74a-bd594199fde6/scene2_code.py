from manim import *

class Scene2(Scene):
    def construct(self):
        # Title
        title = Text("Intelligent Switching", color=GOLD).to_edge(UP)
        self.play(Write(title))

        # Central Switch
        switch_rect = Rectangle(height=1.5, width=3, color=BLUE, fill_opacity=0.3)
        switch_label = Text("SWITCH", color=WHITE).scale(0.6)
        switch = VGroup(switch_rect, switch_label).move_to(ORIGIN)

        # Computers
        pc_a = VGroup(Square(side_length=1, color=TEAL, fill_opacity=0.2), Text("A", color=WHITE).scale(0.6))
        pc_b = VGroup(Square(side_length=1, color=TEAL, fill_opacity=0.2), Text("B", color=WHITE).scale(0.6))
        pc_c = VGroup(Square(side_length=1, color=TEAL, fill_opacity=0.2), Text("C", color=WHITE).scale(0.6))

        pc_a.move_to(LEFT * 5 + UP * 2)
        pc_b.move_to(RIGHT * 5 + UP * 2)
        pc_c.move_to(RIGHT * 5 + DOWN * 2)

        # Connections
        line_a = Line(pc_a.get_right(), switch.get_left(), color=WHITE)
        line_b = Line(pc_b.get_left(), switch.get_right(), color=WHITE)
        line_c = Line(pc_c.get_left(), switch.get_right(), color=WHITE)

        self.play(Create(switch), Create(pc_a), Create(pc_b), Create(pc_c))
        self.play(Create(line_a), Create(line_b), Create(line_c))

        # Data Frame
        frame = Dot(color=YELLOW).move_to(pc_a.get_center())
        frame_label = Text("Data for B", color=YELLOW).scale(0.4).next_to(frame, UP)
        packet = VGroup(frame, frame_label)

        # 1. Send to Switch
        self.play(packet.animate.move_to(switch.get_center()), run_time=1.5)

        # 2. Switch checks MAC Table
        mac_table_bg = Rectangle(height=1.2, width=2, color=WHITE, fill_opacity=0.9).next_to(switch, DOWN)
        mac_table_text = VGroup(
            Text("MAC Table", color=BLACK).scale(0.3),
            Line(LEFT*0.4, RIGHT*0.4, color=BLACK),
            MathTex(r"B \rightarrow Port 2", color=BLACK).scale(0.6)
        ).arrange(DOWN, buff=0.1).move_to(mac_table_bg.get_center())
        
        mac_table = VGroup(mac_table_bg, mac_table_text)
        
        self.play(Create(mac_table))
        self.play(Indicate(mac_table_text[2], color=RED))
        self.wait(1)

        # 3. Targeted delivery
        self.play(FadeOut(mac_table), FadeOut(frame_label))
        self.play(frame.animate.move_to(pc_b.get_center()), run_time=1.5)
        
        # Success indicator
        check = Text("Received!", color=GREEN).scale(0.5).next_to(pc_b, UP)
        self.play(Write(check))
        
        # Show that PC C stayed idle
        idle_text = Text("Idle", color=RED).scale(0.4).next_to(pc_c, UP)
        self.play(Write(idle_text))
        
        self.wait(2)

        # Final explanation
        explanation = Text("Direct delivery = No collisions", color=YELLOW).scale(0.6).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)

        # Cleanup
        self.play(
            *[FadeOut(m) for m in [switch, pc_a, pc_b, pc_c, line_a, line_b, line_c, frame, check, idle_text, explanation, title]]
        )