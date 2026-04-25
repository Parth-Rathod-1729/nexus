from manim import *

class Scene1(Scene):
    def construct(self):
        # Repeater Section
        title = Text("Physical Layer: Repeaters", color=WHITE).to_edge(UP)
        repeater_box = Rectangle(height=1.5, width=2.5, color=BLUE, fill_opacity=0.3)
        repeater_label = Text("Repeater", font_size=24).move_to(repeater_box)
        repeater_group = VGroup(repeater_box, repeater_label)

        # Signals
        weak_signal = Line(LEFT * 4, LEFT * 1.5, color=RED).set_stroke(width=2)
        weak_text = Text("Weak Signal", font_size=18, color=RED).next_to(weak_signal, UP)
        
        strong_signal = Line(RIGHT * 1.5, RIGHT * 4, color=GREEN).set_stroke(width=8)
        strong_text = Text("Regenerated Signal", font_size=18, color=GREEN).next_to(strong_signal, UP)

        self.play(Write(title))
        self.play(Create(repeater_group))
        self.play(Create(weak_signal), Write(weak_text))
        self.wait(1)
        self.play(Create(strong_signal), Write(strong_text))
        self.wait(2)

        # Transition to Hub
        self.play(FadeOut(repeater_group, weak_signal, weak_text, strong_signal, strong_text, title))

        # Hub Section
        title2 = Text("Physical Layer: Hubs", color=WHITE).to_edge(UP)
        hub_box = Square(side_length=1.5, color=TEAL, fill_opacity=0.3)
        hub_label = Text("Hub", font_size=24).move_to(hub_box)
        hub_group = VGroup(hub_box, hub_label)

        # Star Topology Nodes
        node_a = Circle(radius=0.4, color=GOLD, fill_opacity=0.5).shift(LEFT * 3)
        node_b = Circle(radius=0.4, color=GOLD, fill_opacity=0.5).shift(UP * 2 + RIGHT * 2)
        node_c = Circle(radius=0.4, color=GOLD, fill_opacity=0.5).shift(RIGHT * 3)
        node_d = Circle(radius=0.4, color=GOLD, fill_opacity=0.5).shift(DOWN * 2 + RIGHT * 2)
        
        nodes = VGroup(node_a, node_b, node_c, node_d)
        
        # Connections
        l1 = Line(node_a.get_right(), hub_box.get_left())
        l2 = Line(node_b.get_bottom(), hub_box.get_top())
        l3 = Line(node_c.get_left(), hub_box.get_right())
        l4 = Line(node_d.get_top(), hub_box.get_bottom())
        lines = VGroup(l1, l2, l3, l4)

        self.play(Write(title2))
        self.play(Create(hub_group), Create(nodes), Create(lines))
        
        # Packet broadcasting animation
        packet_in = Dot(color=YELLOW).move_to(node_a.get_center())
        self.play(packet_in.animate.move_to(hub_box.get_center()), run_time=1)
        
        packet_out1 = Dot(color=YELLOW).move_to(hub_box.get_center())
        packet_out2 = Dot(color=YELLOW).move_to(hub_box.get_center())
        packet_out3 = Dot(color=YELLOW).move_to(hub_box.get_center())
        
        self.play(
            packet_out1.animate.move_to(node_b.get_center()),
            packet_out2.animate.move_to(node_c.get_center()),
            packet_out3.animate.move_to(node_d.get_center()),
            run_time=1.5
        )
        
        explanation = Text("Hubs broadcast to all ports", font_size=24, color=YELLOW).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)