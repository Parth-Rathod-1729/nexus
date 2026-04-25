from manim import *

class Scene1(Scene):
    def construct(self):
        # Title
        title = Text("Physical Layer: Repeaters and Hubs", font_size=32, color=WHITE)
        title.to_edge(UP)
        self.add(title)
        
        # --- REPEATER SECTION ---
        repeater_label = Text("Repeater", font_size=24, color=BLUE).move_to(UP * 1.5)
        repeater_box = Square(side_length=1.5, color=BLUE, fill_opacity=0.2)
        repeater_group = VGroup(repeater_box, Text("Regenerator", font_size=18)).move_to(ORIGIN)
        
        weak_signal = Line(start=LEFT * 5, end=LEFT * 0.75, color=RED, stroke_width=1)
        weak_text = Text("Weak Signal", font_size=16, color=RED).next_to(weak_signal, UP)
        
        strong_signal = Line(start=RIGHT * 0.75, end=RIGHT * 5, color=GREEN, stroke_width=6)
        strong_text = Text("Regenerated Signal", font_size=16, color=GREEN).next_to(strong_signal, UP)
        
        self.play(Write(repeater_label), Create(repeater_group))
        self.play(Create(weak_signal), Write(weak_text))
        self.wait(1)
        self.play(Create(strong_signal), Write(strong_text))
        self.wait(2)
        
        # Transition to Hub
        self.play(
            FadeOut(weak_signal, weak_text, strong_signal, strong_text, repeater_group, repeater_label)
        )
        
        # --- HUB SECTION ---
        hub_label = Text("Hub (Multi-port Repeater)", font_size=24, color=TEAL).move_to(UP * 2.5)
        hub_box = Rectangle(width=2, height=1.2, color=TEAL, fill_opacity=0.3).move_to(ORIGIN)
        hub_text = Text("HUB", font_size=20).move_to(hub_box.get_center())
        
        pc_a = Circle(radius=0.4, color=WHITE, fill_opacity=0.1).move_to(LEFT * 4 + UP * 1.5)
        pc_b = Circle(radius=0.4, color=WHITE, fill_opacity=0.1).move_to(RIGHT * 4 + UP * 1.5)
        pc_c = Circle(radius=0.4, color=WHITE, fill_opacity=0.1).move_to(LEFT * 4 + DOWN * 1.5)
        pc_d = Circle(radius=0.4, color=WHITE, fill_opacity=0.1).move_to(RIGHT * 4 + DOWN * 1.5)
        
        pc_labels = VGroup(
            Text("PC 1", font_size=14).next_to(pc_a, DOWN),
            Text("PC 2", font_size=14).next_to(pc_b, DOWN),
            Text("PC 3", font_size=14).next_to(pc_c, DOWN),
            Text("PC 4", font_size=14).next_to(pc_d, DOWN)
        )
        
        conn_a = Line(pc_a.get_right(), hub_box.get_left(), color=GRAY)
        conn_b = Line(pc_b.get_left(), hub_box.get_right(), color=GRAY)
        conn_c = Line(pc_c.get_right(), hub_box.get_left(), color=GRAY)
        conn_d = Line(pc_d.get_left(), hub_box.get_right(), color=GRAY)
        
        connections = VGroup(conn_a, conn_b, conn_c, conn_d)
        pcs = VGroup(pc_a, pc_b, pc_c, pc_d)
        
        self.play(Write(hub_label), Create(hub_box), Write(hub_text))
        self.play(Create(pcs), Create(connections), Write(pc_labels))
        
        # Packet Broadcast Animation
        packet = Dot(color=YELLOW).move_to(pc_a.get_center())
        
        self.play(packet.animate.move_to(hub_box.get_center()), run_time=1)
        
        p2 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p3 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p4 = Dot(color=YELLOW).move_to(hub_box.get_center())
        
        broadcast_text = Text("Broadcasting to all ports...", font_size=20, color=YELLOW).to_edge(DOWN)
        
        self.play(Write(broadcast_text))
        self.play(
            p2.animate.move_to(pc_b.get_center()),
            p3.animate.move_to(pc_c.get_center()),
            p4.animate.move_to(pc_d.get_center()),
            run_time=2
        )
        
        self.wait(2)