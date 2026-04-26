from manim import *

class Scene1(Scene):
    def construct(self):
        # Title
        title = Text("Star Topology: The Hub", font_size=32, color=YELLOW).to_edge(UP)
        
        # Central Hub
        hub_box = Rectangle(height=1.2, width=2.2, color=BLUE, fill_opacity=0.3)
        hub_label = Text("HUB", font_size=24).move_to(hub_box.get_center())
        hub = VGroup(hub_box, hub_label).move_to(ORIGIN)

        # Nodes (Stations)
        n1 = Square(side_length=0.8, color=TEAL, fill_opacity=0.2).move_to([-3, 2, 0])
        n2 = Square(side_length=0.8, color=TEAL, fill_opacity=0.2).move_to([3, 2, 0])
        n3 = Square(side_length=0.8, color=TEAL, fill_opacity=0.2).move_to([-3, -2, 0])
        n4 = Square(side_length=0.8, color=TEAL, fill_opacity=0.2).move_to([3, -2, 0])
        nodes = VGroup(n1, n2, n3, n4)
        
        node_labels = VGroup(
            Text("PC 1", font_size=18).next_to(n1, UP),
            Text("PC 2", font_size=18).next_to(n2, UP),
            Text("PC 3", font_size=18).next_to(n3, DOWN),
            Text("PC 4", font_size=18).next_to(n4, DOWN)
        )

        # Connection Lines
        l1 = Line(hub.get_left(), n1.get_bottom(), color=WHITE)
        l2 = Line(hub.get_right(), n2.get_bottom(), color=WHITE)
        l3 = Line(hub.get_left(), n3.get_top(), color=WHITE)
        l4 = Line(hub.get_right(), n4.get_top(), color=WHITE)
        lines = VGroup(l1, l2, l3, l4)

        # Initial Setup
        self.play(Write(title))
        self.play(Create(hub), Create(nodes), Create(node_labels))
        self.play(Create(lines))
        self.wait(1)

        # Weak Signal Animation (PC 1 to Hub)
        weak_signal = Dot(color=RED, radius=0.08).move_to(n1.get_center())
        signal_label = Text("Weak Signal", color=RED, font_size=16).next_to(weak_signal, LEFT)
        
        self.play(Write(signal_label))
        self.play(weak_signal.animate.move_to(hub.get_center()), run_time=2)
        self.play(FadeOut(signal_label))

        # Regeneration effect
        pulse = hub_box.copy().set_color(WHITE).set_stroke(width=5)
        self.play(pulse.animate.scale(1.2).set_fill_opacity(0), run_time=0.5)
        self.remove(pulse)

        # Regenerated Signal Animation (Hub to other PCs)
        reg_label = Text("Regenerated Strong Signal", color=GREEN, font_size=16).next_to(hub, DOWN)
        
        s2 = Dot(color=GREEN, radius=0.12).move_to(hub.get_center())
        s3 = Dot(color=GREEN, radius=0.12).move_to(hub.get_center())
        s4 = Dot(color=GREEN, radius=0.12).move_to(hub.get_center())
        
        self.play(Write(reg_label))
        self.play(
            s2.animate.move_to(n2.get_center()),
            s3.animate.move_to(n3.get_center()),
            s4.animate.move_to(n4.get_center()),
            run_time=2
        )
        
        self.wait(2)

        # Cleanup
        self.play(
            FadeOut(title), FadeOut(hub), FadeOut(nodes), 
            FadeOut(node_labels), FadeOut(lines), 
            FadeOut(weak_signal), FadeOut(s2), FadeOut(s3), FadeOut(s4),
            FadeOut(reg_label)
        )
        self.wait(1)