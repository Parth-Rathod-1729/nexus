from manim import *

class Scene1(Scene):
    def construct(self):
        # 1. Setup Titles and Screen Division
        title = Text("Signal Regeneration and Hubs", font_size=32, color=YELLOW).to_edge(UP)
        v_line = Line(start=[0, 2.5, 0], end=[0, -3.5, 0], color=WHITE)
        left_label = Text("Repeater (Layer 1)", font_size=24, color=BLUE).move_to([-3.5, 2.2, 0])
        right_label = Text("Hub (Multi-port)", font_size=24, color=TEAL).move_to([3.5, 2.2, 0])
        
        # 2. Repeater Components (Left Side)
        repeater_box = Square(side_length=1.2, color=BLUE, fill_opacity=0.2).shift(LEFT * 3.5 + DOWN * 0.5)
        rep_text = Text("Repeater", font_size=18).move_to(repeater_box.get_center())
        
        weak_signal = Line(start=[-6.5, -0.5, 0], end=[-4.1, -0.5, 0], color=RED, stroke_width=2)
        weak_label = Text("Weak Signal", font_size=14, color=RED).next_to(weak_signal, UP, buff=0.1)
        
        strong_signal = Line(start=[-2.9, -0.5, 0], end=[-0.5, -0.5, 0], color=GREEN, stroke_width=8)
        strong_label = Text("Regenerated", font_size=14, color=GREEN).next_to(strong_signal, UP, buff=0.1)
        
        # 3. Hub Components (Right Side)
        hub_center = [3.5, -1, 0]
        hub_node = Circle(radius=0.5, color=TEAL, fill_opacity=0.4).move_to(hub_center)
        hub_inner_text = Text("Hub", font_size=16).move_to(hub_node.get_center())
        
        # Star Topology Devices
        pc_top = Square(side_length=0.4, color=WHITE).move_to([3.5, 0.5, 0])
        pc_right = Square(side_length=0.4, color=WHITE).move_to([5.3, -1, 0])
        pc_bottom = Square(side_length=0.4, color=WHITE).move_to([3.5, -2.5, 0])
        pc_left = Square(side_length=0.4, color=WHITE).move_to([1.7, -1, 0])
        
        pcs = VGroup(pc_top, pc_right, pc_bottom, pc_left)
        lines = VGroup(
            Line(hub_node.get_center(), pc_top.get_center()),
            Line(hub_node.get_center(), pc_right.get_center()),
            Line(hub_node.get_center(), pc_bottom.get_center()),
            Line(hub_node.get_center(), pc_left.get_center())
        )

        # 4. Animation Sequence
        self.play(Write(VGroup(title, left_label, right_label)), Create(v_line))
        self.play(Create(VGroup(repeater_box, rep_text, hub_node, hub_inner_text, pcs, lines)))
        
        # Animation: Repeater Regeneration
        self.play(Create(weak_signal), Write(weak_label), run_time=1.5)
        self.play(repeater_box.animate.set_fill(BLUE, opacity=0.8), run_time=0.3)
        self.play(Create(strong_signal), Write(strong_label), repeater_box.animate.set_fill(BLUE, opacity=0.2), run_time=1.2)
        
        self.wait(1)
        
        # Animation: Hub Broadcast
        # Inbound packet from PC Left
        packet_in = Dot(pc_left.get_center(), color=YELLOW)
        self.play(packet_in.animate.move_to(hub_node.get_center()), run_time=1)
        self.play(hub_node.animate.set_fill(TEAL, opacity=0.8), FadeOut(packet_in), run_time=0.2)
        
        # Outbound packets to all other ports
        p1 = Dot(hub_node.get_center(), color=YELLOW)
        p2 = Dot(hub_node.get_center(), color=YELLOW)
        p3 = Dot(hub_node.get_center(), color=YELLOW)
        
        self.play(
            p1.animate.move_to(pc_top.get_center()),
            p2.animate.move_to(pc_right.get_center()),
            p3.animate.move_to(pc_bottom.get_center()),
            hub_node.animate.set_fill(TEAL, opacity=0.4),
            run_time=1.5
        )
        
        # Cleanup and Conclusion
        self.wait(2)