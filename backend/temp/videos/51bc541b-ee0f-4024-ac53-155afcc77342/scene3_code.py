from manim import *

class Scene3(Scene):
    def construct(self):
        # Title of the scene
        title = Text("Routers and Gateways", font_size=32, color=WHITE).to_edge(UP)
        
        # --- SECTION 1: ROUTERS (IP Based) ---
        router = Square(color=BLUE, fill_opacity=0.5).scale(0.6)
        router_label = Text("Router", font_size=24).next_to(router, UP)
        
        lan_left = Circle(color=TEAL, fill_opacity=0.2).scale(0.7).shift(LEFT * 4)
        lan_right = Circle(color=TEAL, fill_opacity=0.2).scale(0.7).shift(RIGHT * 4)
        label_left = Text("LAN 1", font_size=18).move_to(lan_left.get_center())
        label_right = Text("LAN 2", font_size=18).move_to(lan_right.get_center())
        
        arrow_l = Arrow(lan_left.get_right(), router.get_left(), buff=0.1, color=WHITE)
        arrow_r = Arrow(router.get_right(), lan_right.get_left(), buff=0.1, color=WHITE)
        
        router_group = VGroup(router, router_label, lan_left, lan_right, label_left, label_right, arrow_l, arrow_r)
        
        self.play(Write(title))
        self.play(Create(router_group))
        
        # Data packet movement with IP info
        packet_dot = Dot(color=YELLOW).move_to(lan_left.get_center())
        ip_info = MathTex(r"IP: 192.168.1.1", font_size=20).next_to(packet_dot, UP)
        
        self.play(Create(packet_dot), Write(ip_info))
        self.play(
            packet_dot.animate.move_to(router.get_center()),
            ip_info.animate.move_to(router.get_center() + UP * 0.7)
        )
        self.play(
            packet_dot.animate.move_to(lan_right.get_center()),
            ip_info.animate.move_to(lan_right.get_center() + UP * 0.7)
        )
        self.wait(1)
        self.play(FadeOut(router_group), FadeOut(packet_dot), FadeOut(ip_info))

        # --- SECTION 2: GATEWAYS (Protocol Conversion) ---
        gateway = Rectangle(width=3.4, height=1.6, color=GOLD, fill_opacity=0.4)
        gateway_tag = Text("Gateway", font_size=28).next_to(gateway, UP)
        action_tag = Text("Protocol Converter", font_size=16, color=GOLD).move_to(gateway.get_center())
        
        net_a = Text("Network A (TCP/IP)", font_size=20, color=RED).shift(LEFT * 4.2)
        net_b = Text("Network B (Proprietary)", font_size=20, color=GREEN).shift(RIGHT * 4.2)
        
        conn_a = Arrow(net_a.get_right(), gateway.get_left(), color=WHITE)
        conn_b = Arrow(gateway.get_right(), net_b.get_left(), color=WHITE)
        
        gateway_group = VGroup(gateway, gateway_tag, action_tag, net_a, net_b, conn_a, conn_b)
        
        self.play(Create(gateway_group))
        
        # Demonstrating protocol translation
        p_start = Square(side_length=0.3, color=RED, fill_opacity=0.8).move_to(net_a.get_center())
        self.play(Create(p_start))
        self.play(p_start.animate.move_to(gateway.get_center()))
        
        # Transform packet to show it changed protocols
        p_end = Circle(radius=0.15, color=GREEN, fill_opacity=0.8).move_to(gateway.get_center())
        self.play(ReplacementTransform(p_start, p_end))
        
        self.play(p_end.animate.move_to(net_b.get_center()))
        
        self.wait(2)
        self.play(FadeOut(gateway_group), FadeOut(p_end), FadeOut(title))