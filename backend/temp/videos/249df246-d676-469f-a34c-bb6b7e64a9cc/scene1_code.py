from manim import *

class Scene1(Scene):
    def construct(self):
        # 1. Setup Title
        title = Text("Repeaters and Hubs: The Physical Layer", color=BLUE, font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # 2. Repeater Section
        repeater_box = Rectangle(width=2, height=1.2, color=GOLD, fill_opacity=0.2)
        repeater_box.move_to(LEFT * 3.5 + UP * 0.5)
        repeater_text = Text("Repeater", font_size=24, color=GOLD).next_to(repeater_box, UP)
        
        # Signal lines
        weak_signal = Line(LEFT * 6 + UP * 0.5, LEFT * 4.5 + UP * 0.5, color=RED, stroke_width=2)
        strong_signal = Line(LEFT * 2.5 + UP * 0.5, LEFT * 1 + UP * 0.5, color=GREEN, stroke_width=6)
        
        self.play(Create(repeater_box), Write(repeater_text))
        self.play(Create(weak_signal))

        # Signal pulse animation
        pulse = Dot(color=RED).move_to(weak_signal.get_start())
        self.play(pulse.animate.move_to(repeater_box.get_center()), run_time=1)
        self.play(pulse.animate.set_color(GREEN).scale(1.5))
        self.play(Create(strong_signal), pulse.animate.move_to(strong_signal.get_end()), run_time=1)
        self.play(FadeOut(pulse))

        # 3. Hub Section
        hub_box = Square(side_length=1.5, color=TEAL, fill_opacity=0.2)
        hub_box.move_to(RIGHT * 3.5 + DOWN * 0.5)
        hub_text = Text("Hub", font_size=24, color=TEAL).next_to(hub_box, UP)
        
        # Nodes
        node1 = Circle(radius=0.3, color=WHITE).next_to(hub_box, LEFT, buff=1)
        node2 = Circle(radius=0.3, color=WHITE).next_to(hub_box, RIGHT, buff=1)
        node3 = Circle(radius=0.3, color=WHITE).next_to(hub_box, DOWN, buff=1)
        
        # Connections
        c1 = Line(node1.get_right(), hub_box.get_left())
        c2 = Line(node2.get_left(), hub_box.get_right())
        c3 = Line(node3.get_top(), hub_box.get_bottom())
        
        # Rule: Use VGroup instead of Group for Create
        hub_group = VGroup(hub_box, hub_text, node1, node2, node3, c1, c2, c3)
        self.play(Create(hub_group))

        # Packet Broadcasting
        packet = Dot(color=YELLOW).move_to(node1.get_center())
        self.play(packet.animate.move_to(hub_box.get_center()), run_time=1)
        
        # Create copies for broadcast
        p2 = Dot(color=YELLOW).move_to(hub_box.get_center())
        p3 = Dot(color=YELLOW).move_to(hub_box.get_center())
        
        # Rule: Replace opacity= with fill_opacity=
        self.play(
            p2.animate.move_to(node2.get_center()),
            p3.animate.move_to(node3.get_center()),
            packet.animate.set_fill(fill_opacity=0),
            run_time=1.5
        )

        self.wait(2)
        self.play(FadeOut(VGroup(title, repeater_box, repeater_text, weak_signal, strong_signal, hub_group, p2, p3)))