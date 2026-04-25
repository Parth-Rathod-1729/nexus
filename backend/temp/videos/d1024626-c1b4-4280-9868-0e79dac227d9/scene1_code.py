from manim import *

class Scene1(Scene):
    def construct(self):
        # Title and Labels
        title = Text("Physical Layer: Repeaters & Hubs", color=WHITE).scale(0.8).to_edge(UP)
        rep_label = Text("Repeater (Regeneration)", color=BLUE).scale(0.5).move_to(LEFT * 3.5 + UP * 2)
        hub_label = Text("Hub (Broadcasting)", color=GREEN).scale(0.5).move_to(RIGHT * 3.5 + UP * 2)

        # Repeater Setup
        repeater_box = Rectangle(height=1, width=1.5, color=BLUE, fill_opacity=0.2).move_to(LEFT * 3.5)
        weak_signal = Line(LEFT * 6, LEFT * 4.25, color=RED, stroke_width=1)
        strong_signal = Line(LEFT * 2.75, LEFT * 1, color=TEAL, stroke_width=10)
        
        rep_group = VGroup(repeater_box, rep_label)

        # Hub Setup
        hub_box = Rectangle(height=1.2, width=1.2, color=GREEN, fill_opacity=0.2).move_to(RIGHT * 3.5)
        n1 = Circle(radius=0.2, color=WHITE).move_to(RIGHT * 2.5 + UP * 1.2)
        n2 = Circle(radius=0.2, color=WHITE).move_to(RIGHT * 4.5 + UP * 1.2)
        n3 = Circle(radius=0.2, color=WHITE).move_to(RIGHT * 2.5 + DOWN * 1.2)
        n4 = Circle(radius=0.2, color=WHITE).move_to(RIGHT * 4.5 + DOWN * 1.2)
        
        l1 = Line(hub_box.get_center(), n1.get_center(), color=WHITE)
        l2 = Line(hub_box.get_center(), n2.get_center(), color=WHITE)
        l3 = Line(hub_box.get_center(), n3.get_center(), color=WHITE)
        l4 = Line(hub_box.get_center(), n4.get_center(), color=WHITE)
        
        hub_group = VGroup(hub_box, hub_label, n1, n2, n3, n4, l1, l2, l3, l4)

        # Animation Sequence
        self.play(Write(title))
        self.play(Create(rep_group), Create(hub_group))
        self.wait(1)

        # Repeater Animation: Weak to Strong
        self.play(Create(weak_signal))
        self.play(Create(strong_signal), weak_signal.animate.set_stroke(opacity=0.3))
        self.wait(1)

        # Hub Animation: Packet In, Broadcast Out
        packet_in = Dot(color=YELLOW).move_to(RIGHT * 3.5 + DOWN * 2.5)
        self.play(packet_in.animate.move_to(hub_box.get_center()))
        
        p1 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p2 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p3 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p4 = Dot(color=YELLOW).move_to(hub_box.get_center())

        self.add(p1, p2, p3, p4)
        self.remove(packet_in)
        
        self.play(
            p1.animate.move_to(n1.get_center()),
            p2.animate.move_to(n2.get_center()),
            p3.animate.move_to(n3.get_center()),
            p4.animate.move_to(n4.get_center()),
            run_time=2
        )
        
        # Summary Text
        summary = Text("Regenerate vs. Broadcast", color=GOLD).scale(0.6).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)

        # Cleanup
        self.play(FadeOut(rep_group), FadeOut(hub_group), FadeOut(title), FadeOut(summary), FadeOut(weak_signal), FadeOut(strong_signal), FadeOut(p1), FadeOut(p2), FadeOut(p3), FadeOut(p4))