from manim import *

class Scene1(Scene):
    def construct(self):
        # 1. Title and Layout
        title = Text("Layer 1: Physical Layer", color=WHITE).scale(0.8).to_edge(UP)
        divider = Line(UP * 2, DOWN * 3, color=WHITE)
        
        rep_label = Text("Repeater", color=BLUE).scale(0.6).move_to([-3.5, 2.5, 0])
        hub_label = Text("Hub", color=TEAL).scale(0.6).move_to([3.5, 2.5, 0])
        
        self.add(title, divider, rep_label, hub_label)

        # 2. Repeater Section (Left)
        repeater_box = Rectangle(width=1.5, height=1.0, color=BLUE, fill_opacity=0.3).move_to([-3.5, 0, 0])
        rep_text = Text("Regenerate", color=WHITE).scale(0.3).move_to(repeater_box.get_center())
        
        weak_signal = VGroup(*[Dot(radius=0.05, color=RED).move_to([-6 + i*0.3, 0, 0]) for i in range(3)])
        strong_signal = VGroup(*[Dot(radius=0.12, color=GREEN).move_to([-2 + i*0.4, 0, 0]) for i in range(3)])
        
        in_arrow = Arrow(start=[-5.5, 0, 0], end=[-4.3, 0, 0], color=WHITE, buff=0.1)
        out_arrow = Arrow(start=[-2.7, 0, 0], end=[-1.5, 0, 0], color=WHITE, buff=0.1)

        repeater_grp = VGroup(repeater_box, rep_text, in_arrow, out_arrow)
        self.play(Create(repeater_grp))
        
        # Animate weak signal entering and strong signal leaving
        self.play(weak_signal.animate.move_to([-4.0, 0, 0]), run_time=1.5)
        self.play(FadeOut(weak_signal), Create(strong_signal))
        self.play(strong_signal.animate.move_to([-0.5, 0, 0]), run_time=1.5)
        self.play(FadeOut(strong_signal))

        # 3. Hub Section (Right)
        hub_node = Square(side_length=0.8, color=TEAL, fill_opacity=0.5).move_to([3.5, 0, 0])
        hub_text = Text("Hub", color=WHITE).scale(0.4).move_to(hub_node.get_center())
        
        # Star Topology Devices
        pc1 = Circle(radius=0.3, color=WHITE).move_to([2, 1.2, 0])
        pc2 = Circle(radius=0.3, color=WHITE).move_to([5, 1.2, 0])
        pc3 = Circle(radius=0.3, color=WHITE).move_to([2, -1.2, 0])
        pc4 = Circle(radius=0.3, color=WHITE).move_to([5, -1.2, 0])
        
        l1 = Line(hub_node.get_center(), pc1.get_center(), stroke_width=2)
        l2 = Line(hub_node.get_center(), pc2.get_center(), stroke_width=2)
        l3 = Line(hub_node.get_center(), pc3.get_center(), stroke_width=2)
        l4 = Line(hub_node.get_center(), pc4.get_center(), stroke_width=2)
        
        devices = VGroup(pc1, pc2, pc3, pc4, l1, l2, l3, l4, hub_node, hub_text)
        self.play(Create(devices))

        # Hub Logic: Receive from PC1, Broadcast to all
        packet_in = Dot(color=YELLOW).move_to(pc1.get_center())
        self.play(packet_in.animate.move_to(hub_node.get_center()), run_time=1)
        self.remove(packet_in)
        
        # Simultaneous broadcast
        p1 = Dot(color=YELLOW).move_to(hub_node.get_center())
        p2 = Dot(color=YELLOW).move_to(hub_node.get_center())
        p3 = Dot(color=YELLOW).move_to(hub_node.get_center())
        p4 = Dot(color=YELLOW).move_to(hub_node.get_center())
        
        self.play(
            p1.animate.move_to(pc1.get_center()),
            p2.animate.move_to(pc2.get_center()),
            p3.animate.move_to(pc3.get_center()),
            p4.animate.move_to(pc4.get_center()),
            run_time=1.5
        )
        
        # 4. Final Explanation Labels
        exp_rep = Text("Regenerates Signal", color=GOLD).scale(0.4).move_to([-3.5, -2, 0])
        exp_hub = Text("Broadcasts to All", color=GOLD).scale(0.4).move_to([3.5, -2, 0])
        
        self.play(Write(exp_rep), Write(exp_hub))
        self.wait(2)