from manim import *

class Scene1(Scene):
    def construct(self):
        # 1. Layout: Split screen divider and headers
        divider = Line(UP * 4, DOWN * 4, color=WHITE)
        title_rep = Text("Repeater: Signal Regeneration", color=BLUE).scale(0.6).to_edge(UP).shift(LEFT * 3.5)
        title_hub = Text("Hub: Multi-port Broadcast", color=GREEN).scale(0.6).to_edge(UP).shift(RIGHT * 3.5)
        
        # 2. Repeater Components (Left Side)
        repeater_node = Rectangle(width=1.4, height=0.9, color=BLUE, fill_opacity=0.3).shift(LEFT * 3.5)
        r_label = Text("REPEATER", color=WHITE).scale(0.35).move_to(repeater_node)
        
        # Weak signal: Jagged VGroup
        w1 = Line(LEFT * 6.5 + UP * 0.2, LEFT * 6.2 + DOWN * 0.2)
        w2 = Line(LEFT * 6.2 + DOWN * 0.2, LEFT * 5.9 + UP * 0.2)
        w3 = Line(LEFT * 5.9 + UP * 0.2, LEFT * 5.6 + DOWN * 0.2)
        w4 = Line(LEFT * 5.6 + DOWN * 0.2, LEFT * 5.3 + UP * 0.2)
        weak_signal = VGroup(w1, w2, w3, w4).set_color(RED).set_stroke(width=2)
        
        # Strong signal: Clean Line
        strong_signal = Line(LEFT * 2.8, LEFT * 0.5, color=TEAL, stroke_width=6)
        
        # 3. Hub Components (Right Side)
        hub_node = Square(side_length=1.0, color=GREEN, fill_opacity=0.3).shift(RIGHT * 3.5)
        h_label = Text("HUB", color=WHITE).scale(0.4).move_to(hub_node)
        
        # Star topology nodes
        n1 = Circle(radius=0.3, color=WHITE).shift(RIGHT * 3.5 + UP * 1.8)
        n2 = Circle(radius=0.3, color=WHITE).shift(RIGHT * 5.5 + DOWN * 1.0)
        n3 = Circle(radius=0.3, color=WHITE).shift(RIGHT * 1.5 + DOWN * 1.0)
        nodes = VGroup(n1, n2, n3)
        
        # Connections
        l1 = Line(hub_node.get_top(), n1.get_bottom())
        l2 = Line(hub_node.get_right(), n2.get_left())
        l3 = Line(hub_node.get_left(), n3.get_right())
        conns = VGroup(l1, l2, l3)
        
        # 4. Animation Sequence
        self.play(Create(divider), Write(title_rep), Write(title_hub))
        self.play(Create(repeater_node), Write(r_label), Create(hub_node), Write(h_label))
        self.play(Create(nodes), Create(conns))
        
        # Repeater Animation: Signal comes in weak, goes out strong
        self.play(Create(weak_signal), run_time=1.5)
        self.play(weak_signal.animate.move_to(repeater_node.get_left()), run_time=1)
        self.play(Create(strong_signal), weak_signal.animate.set_stroke(opacity=0), run_time=1)
        
        # Hub Animation: Packet arrival and multi-broadcast
        packet_in = Dot(color=YELLOW).move_to(RIGHT * 6 + UP * 2.5)
        self.play(packet_in.animate.move_to(hub_node.get_center()), run_time=1)
        
        # Simultaneous broadcast
        p1 = Dot(color=YELLOW).move_to(hub_node.get_center())
        p2 = Dot(color=YELLOW).move_to(hub_node.get_center())
        p3 = Dot(color=YELLOW).move_to(hub_node.get_center())
        
        self.play(
            p1.animate.move_to(n1.get_center()),
            p2.animate.move_to(n2.get_center()),
            p3.animate.move_to(n3.get_center()),
            packet_in.animate.set_fill(opacity=0),
            run_time=2
        )
        
        self.wait(2)