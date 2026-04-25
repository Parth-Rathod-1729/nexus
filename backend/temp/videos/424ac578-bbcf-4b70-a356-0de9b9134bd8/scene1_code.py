from manim import *

class Scene1(Scene):
    def construct(self):
        # Title
        title = Text("Repeaters and Hubs", color=WHITE).to_edge(UP, buff=0.5)
        self.play(Write(title))

        # --- Repeater Section (Left) ---
        rep_box = Rectangle(height=1.5, width=2.0, color=BLUE, fill_opacity=0.2).shift(LEFT * 4 + DOWN * 0.5)
        rep_label = Text("Repeater", font_size=24).next_to(rep_box, UP)
        
        # Signals
        weak_signal = MathTex(r"\sim \sim \sim", color=RED).next_to(rep_box, LEFT, buff=0.5)
        strong_signal = MathTex(r"\text{Strong Signal}", color=GREEN, font_size=30).next_to(rep_box, RIGHT, buff=0.5)
        
        rep_group = VGroup(rep_box, rep_label)
        self.play(Create(rep_group))
        self.play(Write(weak_signal))
        
        # Signal regeneration animation
        self.play(weak_signal.animate.move_to(rep_box.get_center()).set_opacity(0), run_time=1.5)
        self.play(Write(strong_signal))
        self.wait(1)

        # --- Hub Section (Right) ---
        hub_center = Circle(radius=0.5, color=GOLD, fill_opacity=0.3).shift(RIGHT * 3 + DOWN * 0.5)
        hub_label = Text("Hub", font_size=24).next_to(hub_center, UP)
        
        # Nodes/Computers
        c1 = Square(side_length=0.6, color=WHITE).move_to(hub_center).shift(UP * 1.5 + LEFT * 1)
        c2 = Square(side_length=0.6, color=WHITE).move_to(hub_center).shift(UP * 1.5 + RIGHT * 1)
        c3 = Square(side_length=0.6, color=WHITE).move_to(hub_center).shift(DOWN * 1.5 + LEFT * 1)
        c4 = Square(side_length=0.6, color=WHITE).move_to(hub_center).shift(DOWN * 1.5 + RIGHT * 1)
        nodes = VGroup(c1, c2, c3, c4)
        
        # Connections
        a1 = Arrow(hub_center.get_top(), c1.get_bottom(), buff=0.1, color=WHITE)
        a2 = Arrow(hub_center.get_top(), c2.get_bottom(), buff=0.1, color=WHITE)
        a3 = Arrow(hub_center.get_bottom(), c3.get_top(), buff=0.1, color=WHITE)
        a4 = Arrow(hub_center.get_bottom(), c4.get_top(), buff=0.1, color=WHITE)
        arrows = VGroup(a1, a2, a3, a4)

        hub_group = VGroup(hub_center, hub_label, nodes, arrows)
        self.play(Create(hub_center), Write(hub_label))
        self.play(Create(nodes), Create(arrows))

        # Packet Broadcasting
        packet_in = Dot(color=YELLOW).next_to(hub_center, RIGHT, buff=1.5)
        self.play(packet_in.animate.move_to(hub_center.get_center()), run_time=1)
        
        # Duplicate packets
        p1 = Dot(color=YELLOW).move_to(hub_center.get_center())
        p2 = Dot(color=YELLOW).move_to(hub_center.get_center())
        p3 = Dot(color=YELLOW).move_to(hub_center.get_center())
        p4 = Dot(color=YELLOW).move_to(hub_center.get_center())
        
        self.play(
            p1.animate.move_to(c1.get_center()),
            p2.animate.move_to(c2.get_center()),
            p3.animate.move_to(c3.get_center()),
            p4.animate.move_to(c4.get_center()),
            run_time=1.5
        )
        
        # Conclusion
        final_text = Text("Hubs Broadcast to All", font_size=20, color=GOLD).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)