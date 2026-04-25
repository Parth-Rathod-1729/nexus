from manim import *

class Scene1(Scene):
    def construct(self):
        # Title
        title = Text("Signal Regeneration: Repeaters and Hubs", font_size=36, color=WHITE).to_edge(UP)
        self.add(title)

        # --- REPEATER SECTION (Left) ---
        repeater_box = Square(side_length=1.5, color=BLUE, fill_opacity=0.4).shift(LEFT * 4 + UP * 0.5)
        repeater_label = Text("Repeater", font_size=24).next_to(repeater_box, DOWN)
        
        weak_line = Line(LEFT * 6.5, LEFT * 4.75 + UP * 0.5, color=RED, stroke_width=2)
        strong_line = Line(LEFT * 3.25 + UP * 0.5, LEFT * 1.5, color=GREEN, stroke_width=10)
        
        repeater_group = VGroup(repeater_box, repeater_label)
        
        # --- HUB SECTION (Right) ---
        hub_core = Circle(radius=0.6, color=TEAL, fill_opacity=0.6).shift(RIGHT * 3.5 + UP * 0.5)
        hub_label = Text("Hub", font_size=24).next_to(hub_core, DOWN)
        
        # Connected Devices (Squares)
        pc1 = Square(side_length=0.4, color=WHITE).next_to(hub_core, UP + RIGHT, buff=0.8)
        pc2 = Square(side_length=0.4, color=WHITE).next_to(hub_core, UP + LEFT, buff=0.8)
        pc3 = Square(side_length=0.4, color=WHITE).next_to(hub_core, DOWN + RIGHT, buff=0.8)
        pc4 = Square(side_length=0.4, color=WHITE).next_to(hub_core, DOWN + LEFT, buff=0.8)
        devices = VGroup(pc1, pc2, pc3, pc4)
        
        hub_group = VGroup(hub_core, hub_label, devices)

        # --- ANIMATION SEQUENCE ---
        
        # 1. Show Repeater and Signal Regeneration
        self.play(Create(repeater_group))
        self.play(Create(weak_line))
        
        pulse = Dot(color=YELLOW).move_to(weak_line.get_start())
        self.play(pulse.animate.move_to(repeater_box.get_center()), run_time=1.5)
        
        # Signal gets strong
        self.play(
            pulse.animate.scale(3).set_color(GREEN),
            Create(strong_line),
            run_time=0.5
        )
        self.play(pulse.animate.move_to(strong_line.get_end()), run_time=1)
        self.play(FadeOut(pulse))
        
        self.wait(1)

        # 2. Show Hub and Broadcast
        self.play(Create(hub_group))
        
        # Incoming data packet
        packet = Dot(color=GOLD).move_to(RIGHT * 6 + UP * 0.5)
        self.play(packet.animate.move_to(hub_core.get_center()), run_time=1)
        
        # Broadcast to all ports
        p1 = Dot(color=GOLD).move_to(hub_core.get_center())
        p2 = Dot(color=GOLD).move_to(hub_core.get_center())
        p3 = Dot(color=GOLD).move_to(hub_core.get_center())
        p4 = Dot(color=GOLD).move_to(hub_core.get_center())
        
        self.play(
            p1.animate.move_to(pc1.get_center()),
            p2.animate.move_to(pc2.get_center()),
            p3.animate.move_to(pc3.get_center()),
            p4.animate.move_to(pc4.get_center()),
            FadeOut(packet),
            run_time=1.5
        )
        
        # Final indicators
        broadcast_text = Text("Broadcast to all", font_size=20, color=YELLOW).next_to(hub_label, DOWN)
        self.play(Write(broadcast_text))
        
        self.wait(2)