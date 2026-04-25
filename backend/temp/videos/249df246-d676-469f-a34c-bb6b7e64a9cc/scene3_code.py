from manim import *

class Scene3(Scene):
    def construct(self):
        # Background and Title
        plane = NumberPlane(background_line_style={"stroke_opacity": 0.1})
        title = Text("Routers and Gateways", color=WHITE).scale(0.8).to_edge(UP)
        self.add(plane, title)

        # Create LAN elements
        lan_a_rect = Rectangle(width=3, height=2, color=BLUE, fill_opacity=0.1).shift(LEFT * 4)
        lan_a_label = Text("LAN A").scale(0.4).next_to(lan_a_rect, UP)
        nodes_a = VGroup(*[Circle(radius=0.15, color=BLUE, fill_opacity=1) for _ in range(3)])
        nodes_a.arrange_in_grid(rows=1, buff=0.4).move_to(lan_a_rect.get_center())
        lan_a = VGroup(lan_a_rect, lan_a_label, nodes_a)

        lan_b_rect = Rectangle(width=3, height=2, color=TEAL, fill_opacity=0.1).shift(RIGHT * 4)
        lan_b_label = Text("LAN B").scale(0.4).next_to(lan_b_rect, UP)
        nodes_b = VGroup(*[Circle(radius=0.15, color=TEAL, fill_opacity=1) for _ in range(3)])
        nodes_b.arrange_in_grid(rows=1, buff=0.4).move_to(lan_b_rect.get_center())
        lan_b = VGroup(lan_b_rect, lan_b_label, nodes_b)

        # Router Setup
        router_box = Square(side_length=1.5, color=GOLD, fill_opacity=0.2)
        router_label = Text("Router").scale(0.4).move_to(router_box.get_top()).shift(DOWN * 0.3)
        routing_table = MathTex(r"IP \to Path", color=YELLOW).scale(0.6).move_to(router_box.get_center())
        router = VGroup(router_box, router_label, routing_table)

        # Connection Lines
        line1 = Line(lan_a_rect.get_right(), router_box.get_left(), color=WHITE)
        line2 = Line(router_box.get_right(), lan_b_rect.get_left(), color=WHITE)

        self.play(Create(lan_a), Create(lan_b), Create(router), Create(line1), Create(line2))
        self.wait(1)

        # Routing Animation: Packet moving by IP
        packet = Dot(color=RED).move_to(lan_a_rect.get_center())
        ip_tag = MathTex(r"192.168.1.5", color=RED).scale(0.4).next_to(packet, UP)
        packet_group = VGroup(packet, ip_tag)

        self.play(packet_group.animate.move_to(router_box.get_center()))
        self.play(Indicate(routing_table), router_box.animate.set_color(WHITE), run_time=1)
        self.play(packet_group.animate.move_to(lan_b_rect.get_center()))
        self.play(FadeOut(packet_group))

        # Gateway Transition
        gateway_box = Rectangle(width=2.5, height=1.5, color=GREEN, fill_opacity=0.2)
        gateway_label = Text("Gateway").scale(0.4).move_to(gateway_box.get_top()).shift(DOWN * 0.3)
        protocol_text = MathTex(r"TCP/IP \leftrightarrow OSI", color=GREEN).scale(0.5).move_to(gateway_box.get_center())
        gateway = VGroup(gateway_box, gateway_label, protocol_text)

        self.play(ReplacementTransform(router, gateway))
        self.wait(1)

        # Gateway Conversion Animation
        packet_start = Dot(color=RED).move_to(lan_a_rect.get_center())
        label_start = Text("Data Pkt", color=RED).scale(0.3).next_to(packet_start, UP)
        pkt_a = VGroup(packet_start, label_start)

        self.play(pkt_a.animate.move_to(gateway_box.get_center()))
        
        # Transformation inside Gateway
        packet_end = Dot(color=GOLD).move_to(gateway_box.get_center())
        label_end = Text("Converted", color=GOLD).scale(0.3).next_to(packet_end, UP)
        pkt_b = VGroup(packet_end, label_end)
        
        self.play(ReplacementTransform(pkt_a, pkt_b))
        self.play(pkt_b.animate.move_to(lan_b_rect.get_center()))
        
        self.wait(2)