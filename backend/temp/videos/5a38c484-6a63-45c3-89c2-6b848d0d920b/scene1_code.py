from manim import *

class Scene1(Scene):
    def construct(self):
        # Title and Layout
        title = Text("Physical Layer: Signal Maintenance", font_size=32, color=WHITE).to_edge(UP)
        divider = Line(UP * 2, DOWN * 3, color=WHITE)
        self.add(title, divider)

        # Labels for Split Screen
        repeater_label = Text("Repeater (1-to-1)", font_size=24, color=TEAL).move_to(LEFT * 3.5 + UP * 1.5)
        hub_label = Text("Hub (Multi-port)", font_size=24, color=GOLD).move_to(RIGHT * 3.5 + UP * 1.5)
        self.add(repeater_label, hub_label)

        # --- REPEATER SECTION (LEFT) ---
        rep_box = Rectangle(width=1.2, height=0.8, color=TEAL, fill_opacity=0.3).move_to(LEFT * 3.5)
        rep_text = Text("Repeater", font_size=16).move_to(rep_box.get_center())
        cable_left = Line(LEFT * 6, LEFT * 4.1, color=WHITE)
        cable_right = Line(LEFT * 2.9, LEFT * 1, color=WHITE)
        
        repeater_group = VGroup(rep_box, rep_text, cable_left, cable_right)
        self.play(Create(repeater_group))

        # Signal Animation - Left
        sig_l = Dot(color=BLUE).move_to(LEFT * 6)
        self.play(sig_l.animate.move_to(LEFT * 4.1).set_color(WHITE), run_time=2, rate_func=linear)
        # Signal enters repeater and gets regenerated
        self.play(sig_l.animate.move_to(LEFT * 2.9).set_color(BLUE), run_time=0.5)
        self.play(sig_l.animate.move_to(LEFT * 1), run_time=1.5, rate_func=linear)
        self.remove(sig_l)

        # --- HUB SECTION (RIGHT) ---
        hub_center = RIGHT * 3.5
        hub_box = Square(side_length=1.0, color=GOLD, fill_opacity=0.3).move_to(hub_center)
        hub_text = Text("Hub", font_size=16).move_to(hub_box.get_center())
        
        # Nodes in Star Topology
        n1 = Circle(radius=0.2, color=WHITE, fill_opacity=1).move_to(hub_center + UP * 1.5)
        n2 = Circle(radius=0.2, color=WHITE, fill_opacity=1).move_to(hub_center + LEFT * 1.5 + DOWN * 0.5)
        n3 = Circle(radius=0.2, color=WHITE, fill_opacity=1).move_to(hub_center + RIGHT * 1.5 + DOWN * 0.5)
        
        l1 = Line(n1.get_center(), hub_center + UP * 0.5)
        l2 = Line(n2.get_center(), hub_center + LEFT * 0.5 + DOWN * 0.2)
        l3 = Line(n3.get_center(), hub_center + RIGHT * 0.5 + DOWN * 0.2)
        
        hub_group = VGroup(hub_box, hub_text, n1, n2, n3, l1, l2, l3)
        self.play(Create(hub_group))

        # Signal Animation - Right (Broadcast)
        sig_h_in = Dot(color=BLUE).move_to(n1.get_center())
        self.play(sig_h_in.animate.move_to(hub_center), run_time=1.5)
        
        # Broadcast to all other ports
        sig_h_out1 = Dot(color=BLUE).move_to(hub_center)
        sig_h_out2 = Dot(color=BLUE).move_to(hub_center)
        
        self.play(
            sig_h_out1.animate.move_to(n2.get_center()),
            sig_h_out2.animate.move_to(n3.get_center()),
            sig_h_in.animate.set_fill(opacity=0),
            run_time=1.5
        )

        # Final Concept Text
        explanation = Text("Regenerates and Broadcasts Bits", font_size=20, color=YELLOW).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)

        # Cleanup for concise video
        self.play(FadeOut(VGroup(repeater_group, hub_group, explanation, title, divider, sig_h_out1, sig_h_out2, repeater_label, hub_label)))