from manim import *

class Scene1(Scene):
    def construct(self):
        # --- Part 1: Repeater ---
        title_rep = Text("Repeater: Signal Regeneration", color=BLUE).scale(0.8).to_edge(UP)
        repeater_box = Square(color=WHITE, fill_opacity=0.2).scale(0.7)
        repeater_label = Text("Repeater", font_size=24).move_to(repeater_box)
        
        in_line = Line(LEFT * 4, LEFT * 0.7, color=RED)
        out_line = Line(RIGHT * 0.7, RIGHT * 4, color=GREEN)
        
        weak_dot = Dot(color=RED, fill_opacity=0.4).scale(0.5).move_to(LEFT * 4)
        strong_dot = Dot(color=GREEN, fill_opacity=1.0).scale(1.5).move_to(ORIGIN)

        repeater_group = VGroup(repeater_box, repeater_label, in_line, out_line)
        
        self.play(Write(title_rep))
        self.play(Create(repeater_group))
        
        # Signal regeneration animation
        self.play(weak_dot.animate.move_to(ORIGIN), run_time=2, rate_func=linear)
        self.remove(weak_dot)
        self.add(strong_dot)
        self.play(strong_dot.animate.move_to(RIGHT * 4), run_time=1.5, rate_func=linear)
        self.play(FadeOut(repeater_group), FadeOut(strong_dot), FadeOut(title_rep))

        # --- Part 2: Hub ---
        title_hub = Text("Hub: Multi-port Broadcast", color=GOLD).scale(0.8).to_edge(UP)
        hub_center = Circle(radius=0.5, color=GOLD, fill_opacity=0.3)
        hub_label = Text("Hub", font_size=20).move_to(hub_center)
        
        # Nodes in star topology
        n1 = Rectangle(height=0.4, width=0.6, color=TEAL).shift(UP * 2)
        n2 = Rectangle(height=0.4, width=0.6, color=TEAL).shift(DOWN * 2)
        n3 = Rectangle(height=0.4, width=0.6, color=TEAL).shift(LEFT * 3)
        n4 = Rectangle(height=0.4, width=0.6, color=TEAL).shift(RIGHT * 3)
        
        l1 = Line(hub_center.get_top(), n1.get_bottom())
        l2 = Line(hub_center.get_bottom(), n2.get_top())
        l3 = Line(hub_center.get_left(), n3.get_right())
        l4 = Line(hub_center.get_right(), n4.get_left())
        
        nodes = VGroup(n1, n2, n3, n4)
        lines = VGroup(l1, l2, l3, l4)
        hub_group = VGroup(hub_center, hub_label, nodes, lines)

        self.play(Write(title_hub))
        self.play(Create(hub_group))
        
        # Data packet enters from left node (n3)
        packet = Dot(color=YELLOW).move_to(n3.get_center())
        self.play(packet.animate.move_to(hub_center.get_center()), run_time=1.5)
        
        # Hub broadcasts to all other ports (n1, n2, n4)
        p1 = Dot(color=YELLOW).move_to(hub_center.get_center())
        p2 = Dot(color=YELLOW).move_to(hub_center.get_center())
        p4 = Dot(color=YELLOW).move_to(hub_center.get_center())
        
        self.play(
            p1.animate.move_to(n1.get_center()),
            p2.animate.move_to(n2.get_center()),
            p4.animate.move_to(n4.get_center()),
            FadeOut(packet),
            run_time=2
        )
        
        self.wait(1)
        self.play(FadeOut(hub_group), FadeOut(p1), FadeOut(p2), FadeOut(p4), FadeOut(title_hub))