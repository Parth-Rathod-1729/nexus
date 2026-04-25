from manim import *

class Scene1(Scene):
    def construct(self):
        # Title of the scene
        title = Text("Physical Layer: Repeaters and Hubs", font_size=32, color=WHITE).to_edge(UP, buff=0.3)
        self.play(Write(title))

        # --- REPEATER SECTION (Top Half) ---
        # A repeater regenerates signal strength
        rep_box = Rectangle(width=2.5, height=1.2, color=BLUE, fill_opacity=0.2).shift(UP * 1.5)
        rep_text = Text("Repeater", font_size=20).move_to(rep_box.get_center())
        
        # Paths for the signal
        line_in = Line(LEFT * 5 + UP * 1.5, rep_box.get_left(), color=RED, stroke_width=2)
        line_out = Line(rep_box.get_right(), RIGHT * 5 + UP * 1.5, color=GREEN, stroke_width=8)
        
        # Signals
        weak_signal = Dot(color=RED, radius=0.06).move_to(LEFT * 5 + UP * 1.5)
        strong_signal = Dot(color=GREEN, radius=0.18).move_to(rep_box.get_right())
        
        rep_group = VGroup(rep_box, rep_text, line_in)
        self.play(Create(rep_group))
        
        # Animation: Weak signal enters
        self.play(weak_signal.animate.move_to(rep_box.get_left()), run_time=1.5)
        self.play(Indicate(rep_box, color=BLUE))
        
        # Animation: Strong signal emerges
        self.play(
            Create(line_out),
            weak_signal.animate.set_fill(opacity=0),
            Create(strong_signal)
        )
        self.play(strong_signal.animate.move_to(RIGHT * 5 + UP * 1.5), run_time=1.5)

        # --- HUB SECTION (Bottom Half) ---
        # A hub broadcasts data to all ports
        hub_sq = Square(side_length=1.2, color=GOLD, fill_opacity=0.2).shift(DOWN * 1.5)
        hub_label = Text("Hub", font_size=20).move_to(hub_sq.get_center())
        
        # Workstations
        pc_src = Circle(radius=0.3, color=WHITE).move_to(LEFT * 3 + DOWN * 1.5)
        pc_dest1 = Circle(radius=0.3, color=WHITE).move_to(RIGHT * 3 + DOWN * 0.5)
        pc_dest2 = Circle(radius=0.3, color=WHITE).move_to(RIGHT * 3 + DOWN * 2.5)
        
        # Connections
        c1 = Line(pc_src.get_right(), hub_sq.get_left(), color=WHITE)
        c2 = Line(pc_dest1.get_left(), hub_sq.get_right(), color=WHITE)
        c3 = Line(pc_dest2.get_left(), hub_sq.get_right(), color=WHITE)
        
        hub_net = VGroup(hub_sq, hub_label, pc_src, pc_dest1, pc_dest2, c1, c2, c3)
        self.play(Create(hub_net))
        
        # Animation: Data packet travels to hub
        packet = Dot(color=YELLOW, radius=0.12).move_to(pc_src.get_center())
        self.play(packet.animate.move_to(hub_sq.get_center()), run_time=1)
        
        # Animation: Hub broadcasts to all other devices
        p_copy1 = Dot(color=YELLOW, radius=0.12).move_to(hub_sq.get_center())
        p_copy2 = Dot(color=YELLOW, radius=0.12).move_to(hub_sq.get_center())
        
        self.play(
            p_copy1.animate.move_to(pc_dest1.get_center()),
            p_copy2.animate.move_to(pc_dest2.get_center()),
            packet.animate.set_fill(opacity=0),
            run_time=1.5
        )
        
        self.wait(2)