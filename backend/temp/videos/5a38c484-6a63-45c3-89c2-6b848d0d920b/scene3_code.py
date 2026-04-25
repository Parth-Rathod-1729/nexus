from manim import *

class Scene3(Scene):
    def construct(self):
        # Title
        title = Text("Routing and Protocol Conversion", color=WHITE).scale(0.8)
        title.to_edge(UP)
        self.play(Write(title))

        # Define LANs
        lan_a = Circle(color=BLUE, fill_opacity=0.3).scale(1.2).shift(LEFT * 4 + DOWN * 0.5)
        label_a = Text("LAN A", color=BLUE).scale(0.6).next_to(lan_a, UP)
        
        lan_b = Circle(color=GREEN, fill_opacity=0.3).scale(1.2).shift(RIGHT * 4 + DOWN * 0.5)
        label_b = Text("LAN B", color=GREEN).scale(0.6).next_to(lan_b, UP)

        # Router
        router = Rectangle(color=TEAL, height=1.2, width=1.8, fill_opacity=0.8).move_to(DOWN * 0.5)
        router_text = Text("ROUTER", color=WHITE).scale(0.5).move_to(router)
        routing_label = Text("IP Routing", color=TEAL).scale(0.5).next_to(router, UP)
        
        router_group = VGroup(router, router_text, routing_label)

        # Initial View: Routing
        self.play(
            Create(lan_a), Create(label_a),
            Create(lan_b), Create(label_b),
            Create(router_group)
        )
        self.wait(1)

        # Packet Animation
        packet = Square(color=YELLOW, side_length=0.4, fill_opacity=1)
        p_text = Text("IP", color=BLACK).scale(0.3).move_to(packet)
        ip_packet = VGroup(packet, p_text)
        ip_packet.move_to(lan_a.get_center())

        # Move Packet: LAN A -> Router -> LAN B
        self.play(ip_packet.animate.move_to(router.get_center()), run_time=1.5)
        self.play(ip_packet.animate.move_to(lan_b.get_center()), run_time=1.5)
        self.play(FadeOut(ip_packet))

        # Transition to Gateway
        gateway = Rectangle(color=GOLD, height=1.2, width=2.2, fill_opacity=0.8).move_to(DOWN * 0.5)
        gateway_text = Text("GATEWAY", color=WHITE).scale(0.5).move_to(gateway)
        conversion_label = Text("Protocol Conversion", color=GOLD).scale(0.5).next_to(gateway, UP)
        
        gateway_group = VGroup(gateway, gateway_text, conversion_label)

        # Replace Router with Gateway
        self.play(
            FadeOut(router_group),
            FadeIn(gateway_group)
        )
        self.wait(1)

        # Protocol Conversion Animation
        packet_in = Square(color=YELLOW, side_length=0.4, fill_opacity=1)
        pi_text = Text("TCP", color=BLACK).scale(0.3).move_to(packet_in)
        packet_in_group = VGroup(packet_in, pi_text).move_to(lan_a.get_center())

        # Move to Gateway
        self.play(packet_in_group.animate.move_to(gateway.get_center()), run_time=1.5)
        
        # Transform in Gateway
        packet_out = Square(color=RED, side_length=0.4, fill_opacity=1)
        po_text = Text("SNA", color=WHITE).scale(0.3).move_to(packet_out)
        packet_out_group = VGroup(packet_out, po_text).move_to(gateway.get_center())

        self.play(ReplacementTransform(packet_in_group, packet_out_group))
        
        # Move to LAN B (Different Network Type)
        self.play(packet_out_group.animate.move_to(lan_b.get_center()), run_time=1.5)
        
        # Final cleanup
        self.wait(2)
        self.play(
            FadeOut(lan_a), FadeOut(label_a),
            FadeOut(lan_b), FadeOut(label_b),
            FadeOut(gateway_group), FadeOut(packet_out_group),
            FadeOut(title)
        )