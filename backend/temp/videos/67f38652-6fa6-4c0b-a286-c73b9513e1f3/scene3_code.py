from manim import *

class Scene3(Scene):
    def construct(self):
        # Title
        title = Text("Inter-Network Connectivity", font_size=32, color=WHITE).to_edge(UP)
        self.play(Write(title))

        # --- Router Section ---
        router_group = VGroup()
        router_node = Circle(radius=0.6, color=GOLD, fill_opacity=0.3)
        router_text = Text("Router", font_size=24).move_to(router_node.get_center())
        router_group.add(router_node, router_text).shift(UP * 0.5)

        lan_left = Square(side_length=1.2, color=TEAL, fill_opacity=0.2).shift(LEFT * 4 + UP * 0.5)
        lan_left_text = Text("LAN A", font_size=20).next_to(lan_left, UP)
        
        lan_right = Square(side_length=1.2, color=TEAL, fill_opacity=0.2).shift(RIGHT * 4 + UP * 0.5)
        lan_right_text = Text("LAN B", font_size=20).next_to(lan_right, UP)

        conn_l = Line(lan_left.get_right(), router_node.get_left(), color=WHITE)
        conn_r = Line(lan_right.get_left(), router_node.get_right(), color=WHITE)

        self.play(
            Create(lan_left), Create(lan_left_text),
            Create(lan_right), Create(lan_right_text),
            Create(router_group),
            Create(conn_l), Create(conn_r)
        )

        # Packet movement through router
        packet = Dot(color=YELLOW).move_to(lan_left.get_center())
        label_ip = Text("IP Label", font_size=16, color=YELLOW).next_to(packet, UP)
        
        self.play(FadeIn(packet), FadeIn(label_ip))
        self.play(
            packet.animate.move_to(router_node.get_center()),
            label_ip.animate.move_to(router_node.get_top() + UP * 0.2)
        )
        self.wait(0.5)
        self.play(
            packet.animate.move_to(lan_right.get_center()),
            label_ip.animate.move_to(lan_right.get_top() + UP * 0.2)
        )
        self.play(FadeOut(packet), FadeOut(label_ip))

        # --- Gateway Section ---
        gateway_group = VGroup()
        gateway_box = Rectangle(width=2.5, height=1.2, color=RED, fill_opacity=0.3).shift(DOWN * 2)
        gateway_text = Text("Gateway\n(Converter)", font_size=20).move_to(gateway_box.get_center())
        gateway_group.add(gateway_box, gateway_text)

        net_square = Square(side_length=1, color=BLUE, fill_opacity=0.2).shift(LEFT * 4 + DOWN * 2)
        net_circle = Circle(radius=0.5, color=GREEN, fill_opacity=0.2).shift(RIGHT * 4 + DOWN * 2)
        
        arrow_in = Arrow(net_square.get_right(), gateway_box.get_left(), color=WHITE, buff=0.1)
        arrow_out = Arrow(gateway_box.get_right(), net_circle.get_left(), color=WHITE, buff=0.1)

        self.play(
            Create(gateway_group),
            Create(net_square),
            Create(net_circle),
            Create(arrow_in),
            Create(arrow_out)
        )

        # Translation visual
        p_sq = Square(side_length=0.3, color=BLUE, fill_opacity=1).move_to(net_square.get_center())
        self.play(FadeIn(p_sq))
        self.play(p_sq.animate.move_to(gateway_box.get_center()))
        
        p_circ = Circle(radius=0.15, color=GREEN, fill_opacity=1).move_to(gateway_box.get_center())
        self.play(ReplacementTransform(p_sq, p_circ))
        self.play(p_circ.animate.move_to(net_circle.get_center()))
        
        self.wait(2)

        # Clean up
        self.play(
            *[FadeOut(m) for m in [title, router_group, lan_left, lan_left_text, 
                                   lan_right, lan_right_text, conn_l, conn_r,
                                   gateway_group, net_square, net_circle, 
                                   arrow_in, arrow_out, p_circ]]
        )