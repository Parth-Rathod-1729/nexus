from manim import *
import numpy as np

class Scene1(Scene):
    def construct(self):
        # --- PART 1: REPEATER ---
        repeater_box = Rectangle(height=1.5, width=2.5, color=BLUE, fill_opacity=0.2)
        repeater_box.move_to(UP * 2)
        repeater_label = Text("Repeater", font_size=28, color=WHITE).move_to(repeater_box)
        
        # Weak Signal (Left of Repeater)
        weak_wave = VGroup()
        for i in range(20):
            x1 = -4.5 + i * 0.15
            x2 = -4.5 + (i + 1) * 0.15
            y1 = 0.2 * np.sin(x1 * 8) + 2
            y2 = 0.2 * np.sin(x2 * 8) + 2
            weak_wave.add(Line(start=[x1, y1, 0], end=[x2, y2, 0], color=WHITE, stroke_width=1))
            
        # Strong Signal (Right of Repeater)
        strong_wave = VGroup()
        for i in range(20):
            x1 = 1.2 + i * 0.15
            x2 = 1.2 + (i + 1) * 0.15
            y1 = 0.6 * np.sin(x1 * 8) + 2
            y2 = 0.6 * np.sin(x2 * 8) + 2
            strong_wave.add(Line(start=[x1, y1, 0], end=[x2, y2, 0], color=TEAL, stroke_width=4))

        # --- PART 2: HUB ---
        hub_box = Rectangle(height=1.2, width=1.2, color=GOLD, fill_opacity=0.3)
        hub_box.move_to(DOWN * 1.5)
        hub_label = Text("Hub", font_size=24, color=WHITE).move_to(hub_box)
        
        # Nodes (Computers)
        n1 = Circle(radius=0.4, color=WHITE, fill_opacity=0.1).move_to(hub_box.get_center() + LEFT * 3)
        n2 = Circle(radius=0.4, color=WHITE, fill_opacity=0.1).move_to(hub_box.get_center() + RIGHT * 3)
        n3 = Circle(radius=0.4, color=WHITE, fill_opacity=0.1).move_to(hub_box.get_center() + DOWN * 1.5 + LEFT * 1.5)
        n4 = Circle(radius=0.4, color=WHITE, fill_opacity=0.1).move_to(hub_box.get_center() + DOWN * 1.5 + RIGHT * 1.5)
        
        nodes = VGroup(n1, n2, n3, n4)
        node_labels = VGroup(
            Text("PC1", font_size=18).move_to(n1),
            Text("PC2", font_size=18).move_to(n2),
            Text("PC3", font_size=18).move_to(n3),
            Text("PC4", font_size=18).move_to(n4)
        )
        
        # Connections
        c1 = Line(hub_box.get_left(), n1.get_right(), color=GRAY)
        c2 = Line(hub_box.get_right(), n2.get_left(), color=GRAY)
        c3 = Line(hub_box.get_corner(DL), n3.get_top(), color=GRAY)
        c4 = Line(hub_box.get_corner(DR), n4.get_top(), color=GRAY)
        connections = VGroup(c1, c2, c3, c4)

        # --- ANIMATION ---
        # 1. Repeater Segment
        self.play(Create(repeater_box), Write(repeater_label))
        self.play(Create(weak_wave), run_time=1.5)
        self.play(Create(strong_wave), run_time=1.5)
        self.wait(1)

        # 2. Hub Segment
        self.play(Create(hub_box), Write(hub_label))
        self.play(Create(nodes), Write(node_labels), Create(connections))
        
        # Signal Transfer Animation
        sig_in = Dot(color=YELLOW).move_to(n1.get_center())
        self.play(sig_in.animate.move_to(hub_box.get_center()), run_time=1)
        self.remove(sig_in)
        
        sig_out1 = Dot(color=YELLOW).move_to(hub_box.get_center())
        sig_out2 = Dot(color=YELLOW).move_to(hub_box.get_center())
        sig_out3 = Dot(color=YELLOW).move_to(hub_box.get_center())
        
        self.play(
            sig_out1.animate.move_to(n2.get_center()),
            sig_out2.animate.move_to(n3.get_center()),
            sig_out3.animate.move_to(n4.get_center()),
            run_time=1.5
        )
        
        self.play(FadeOut(sig_out1), FadeOut(sig_out2), FadeOut(sig_out3))
        self.wait(2)