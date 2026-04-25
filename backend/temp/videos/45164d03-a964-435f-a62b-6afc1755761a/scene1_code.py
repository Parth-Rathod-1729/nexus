from manim import *

class Scene1(Scene):
    def construct(self):
        # Title and Labels
        title = Text("Signal Regeneration and Broadcasting", font_size=32, color=WHITE).to_edge(UP)
        repeater_title = Text("Repeater: Physical Layer", font_size=24, color=BLUE).move_to(UP * 2 + LEFT * 3.5)
        hub_title = Text("Hub: Multi-port Repeater", font_size=24, color=GOLD).move_to(UP * 2 + RIGHT * 3.5)

        self.play(Write(title))
        self.wait(1)

        # REPEATER SECTION
        repeater_box = Rectangle(width=2, height=1.2, color=BLUE, fill_opacity=0.2).shift(LEFT * 4 + DOWN * 1)
        repeater_text = Text("Repeater", font_size=20).move_to(repeater_box.get_center())
        
        in_line = Line(LEFT * 6, LEFT * 5, color=RED)
        out_line = Line(LEFT * 3, LEFT * 1, color=GREEN)
        
        weak_signal = VGroup(*[Dot(color=RED, fill_opacity=0.4).scale(0.5) for _ in range(3)])
        weak_signal.arrange(RIGHT, buff=0.2).move_to(LEFT * 6)
        
        strong_signal = VGroup(*[Dot(color=GREEN, fill_opacity=1.0).scale(1.2) for _ in range(3)])
        strong_signal.arrange(RIGHT, buff=0.2).move_to(LEFT * 3)

        repeater_group = VGroup(repeater_box, repeater_text, repeater_title)
        self.play(Create(repeater_group))
        
        # Animate Signal Regeneration
        self.play(weak_signal.animate.move_to(repeater_box.get_left()), run_time=1.5, rate_func=linear)
        self.play(FadeOut(weak_signal), FadeIn(strong_signal))
        self.play(strong_signal.animate.move_to(LEFT * 0.5), run_time=1.5, rate_func=linear)
        self.wait(1)

        # HUB SECTION
        hub_box = Rectangle(width=1.5, height=1.5, color=GOLD, fill_opacity=0.2).shift(RIGHT * 4 + DOWN * 1)
        hub_text = Text("Hub", font_size=20).move_to(hub_box.get_center())
        
        # Connected Nodes
        node1 = Circle(radius=0.3, color=WHITE, fill_opacity=0.1).next_to(hub_box, UP, buff=0.8)
        node2 = Circle(radius=0.3, color=WHITE, fill_opacity=0.1).next_to(hub_box, DOWN, buff=0.8)
        node3 = Circle(radius=0.3, color=WHITE, fill_opacity=0.1).next_to(hub_box, RIGHT, buff=0.8)
        
        link1 = Line(hub_box.get_top(), node1.get_bottom())
        link2 = Line(hub_box.get_bottom(), node2.get_top())
        link3 = Line(hub_box.get_right(), node3.get_left())
        
        hub_group = VGroup(hub_box, hub_text, hub_title, node1, node2, node3, link1, link2, link3)
        
        # Transition to Hub
        self.play(Create(hub_group))
        
        # Packet enters Hub
        packet_in = Dot(color=TEAL).move_to(RIGHT * 1.5 + DOWN * 1)
        self.play(packet_in.animate.move_to(hub_box.get_center()), run_time=1)
        
        # Broadcast packets
        p1 = Dot(color=TEAL).move_to(hub_box.get_center())
        p2 = Dot(color=TEAL).move_to(hub_box.get_center())
        p3 = Dot(color=TEAL).move_to(hub_box.get_center())
        
        self.play(
            p1.animate.move_to(node1.get_center()),
            p2.animate.move_to(node2.get_center()),
            p3.animate.move_to(node3.get_center()),
            FadeOut(packet_in),
            run_time=1.5
        )
        
        # Conclusion text
        conclusion = Text("Repeaters amplify. Hubs broadcast.", font_size=24, color=YELLOW).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)

        # Cleanup
        self.play(
            FadeOut(repeater_group),
            FadeOut(hub_group),
            FadeOut(strong_signal),
            FadeOut(p1), FadeOut(p2), FadeOut(p3),
            FadeOut(title),
            FadeOut(conclusion)
        )