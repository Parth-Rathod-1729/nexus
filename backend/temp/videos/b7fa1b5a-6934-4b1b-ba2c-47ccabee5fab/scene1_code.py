from manim import *

class Scene1(Scene):
    def construct(self):
        # Title
        title = Text("The Physical Layer: Repeaters and Hubs", color=BLUE, font_size=32)
        title.to_edge(UP)
        self.play(Write(title))

        # --- REPEATER SECTION ---
        repeater_box = Square(side_length=1.2, color=TEAL, fill_opacity=0.3)
        repeater_box.move_to(LEFT * 4 + UP * 0.5)
        repeater_label = Text("Repeater", font_size=20, color=WHITE).next_to(repeater_box, UP)
        
        # Weak Signal Visualization (Jagged Red Lines)
        w1 = LEFT * 6 + UP * 0.5
        w2 = LEFT * 5.5 + UP * 0.7
        w3 = LEFT * 5.2 + UP * 0.3
        w4 = LEFT * 4.7 + UP * 0.5
        weak_signal = VGroup(
            Line(w1, w2, color=RED, stroke_width=2),
            Line(w2, w3, color=RED, stroke_width=2),
            Line(w3, w4, color=RED, stroke_width=2)
        )
        
        # Strong Signal Visualization (Thick Green Line)
        strong_signal = Line(LEFT * 3.3 + UP * 0.5, LEFT * 1 + UP * 0.5, color=GREEN, stroke_width=8)
        
        repeater_group = VGroup(repeater_box, repeater_label)
        self.play(Create(repeater_group))
        self.play(Create(weak_signal))
        self.wait(0.5)
        
        # Signal regeneration animation
        signal_dot = Dot(color=WHITE).move_to(w1)
        self.play(signal_dot.animate.move_to(w4), run_time=1)
        self.play(FadeOut(weak_signal), FadeOut(signal_dot))
        
        self.play(Create(strong_signal))
        out_dot = Dot(color=WHITE).move_to(LEFT * 3.3 + UP * 0.5)
        self.play(out_dot.animate.move_to(LEFT * 1 + UP * 0.5), run_time=1)
        self.play(FadeOut(out_dot))
        self.wait(1)

        # --- HUB SECTION ---
        hub_box = Rectangle(height=1.0, width=1.6, color=GOLD, fill_opacity=0.3)
        hub_box.move_to(RIGHT * 3 + UP * 0.5)
        hub_label = Text("Hub", font_size=20, color=WHITE).next_to(hub_box, UP)
        
        # Nodes (Computers)
        node1 = Square(side_length=0.4, color=BLUE, fill_opacity=0.5).move_to(RIGHT * 1.5 + UP * 2)
        node2 = Square(side_length=0.4, color=BLUE, fill_opacity=0.5).move_to(RIGHT * 4.5 + UP * 2)
        node3 = Square(side_length=0.4, color=BLUE, fill_opacity=0.5).move_to(RIGHT * 1.5 + DOWN * 1)
        node4 = Square(side_length=0.4, color=BLUE, fill_opacity=0.5).move_to(RIGHT * 4.5 + DOWN * 1)
        nodes = VGroup(node1, node2, node3, node4)
        
        # Connections
        c1 = Arrow(hub_box.get_center(), node1.get_center(), buff=0.1, color=WHITE)
        c2 = Arrow(hub_box.get_center(), node2.get_center(), buff=0.1, color=WHITE)
        c3 = Arrow(hub_box.get_center(), node3.get_center(), buff=0.1, color=WHITE)
        c4 = Arrow(hub_box.get_center(), node4.get_center(), buff=0.1, color=WHITE)
        connections = VGroup(c1, c2, c3, c4)

        hub_group = VGroup(hub_box, hub_label, nodes)
        self.play(Create(hub_group))
        
        # Incoming packet to Hub
        in_packet = Dot(color=YELLOW).move_to(RIGHT * 0.5 + UP * 0.5)
        self.play(in_packet.animate.move_to(hub_box.get_center()))
        self.play(FadeOut(in_packet))
        
        # Broadcasting to all nodes
        self.play(Create(connections))
        
        p1 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p2 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p3 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p4 = Dot(color=YELLOW).move_to(hub_box.get_center())
        
        self.play(
            p1.animate.move_to(node1.get_center()),
            p2.animate.move_to(node2.get_center()),
            p3.animate.move_to(node3.get_center()),
            p4.animate.move_to(node4.get_center()),
            run_time=1.5
        )
        
        self.wait(2)
        
        # Cleanup for final look
        self.play(FadeOut(p1), FadeOut(p2), FadeOut(p3), FadeOut(p4))
        self.wait(1)