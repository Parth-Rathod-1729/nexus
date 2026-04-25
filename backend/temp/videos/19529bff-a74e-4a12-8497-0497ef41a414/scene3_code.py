from manim import *

class Scene3(Scene):
    def construct(self):
        # Title
        title = Text("Inter-Network Routing: Routers & Gateways", color=BLUE).scale(0.7)
        title.to_edge(UP)
        self.play(Write(title))

        # --- Router Section (Left) ---
        router_label = Text("Router (IP Routing)", font_size=24, color=GOLD).shift(LEFT * 3.5 + UP * 2)
        lan = Circle(radius=0.6, color=GREEN, fill_opacity=0.3).shift(LEFT * 5 + UP * 0.5)
        lan_label = Text("LAN", font_size=20).move_to(lan)
        
        wan = Circle(radius=0.6, color=TEAL, fill_opacity=0.3).shift(LEFT * 5 + DOWN * 1.5)
        wan_label = Text("WAN", font_size=20).move_to(wan)
        
        router_box = Square(side_length=0.8, color=GOLD, fill_opacity=0.5).shift(LEFT * 2.5 + DOWN * 0.5)
        router_text = Text("R", font_size=24).move_to(router_box)
        
        arrow_to_r = Arrow(lan.get_right(), router_box.get_top(), buff=0.1)
        arrow_from_r = Arrow(router_box.get_bottom(), wan.get_right(), buff=0.1)
        
        router_vgroup = VGroup(lan, lan_label, wan, wan_label, router_box, router_text, arrow_to_r, arrow_from_r)
        
        # Packet for Router
        p1 = Rectangle(width=0.3, height=0.2, color=WHITE, fill_opacity=1).move_to(lan.get_center())
        p1_label = Text("IP", font_size=10, color=BLACK).move_to(p1)
        packet1 = VGroup(p1, p1_label)

        self.play(Create(router_vgroup), Write(router_label))
        self.play(packet1.animate.move_to(router_box.get_center()))
        self.play(packet1.animate.move_to(wan.get_center()))
        self.wait(1)

        # --- Gateway Section (Right) ---
        gateway_label = Text("Gateway (Protocol Conversion)", font_size=24, color=RED).shift(RIGHT * 3.5 + UP * 2)
        
        net_a = Square(side_length=1.2, color=PURPLE, fill_opacity=0.2).shift(RIGHT * 1.5 + DOWN * 0.5)
        net_a_label = Text("Net A", font_size=20).move_to(net_a.get_top() + DOWN * 0.3)
        prot_a = Text("Prot X", font_size=16, color=PURPLE).move_to(net_a.get_center())
        
        net_b = Rectangle(width=1.5, height=1.2, color=YELLOW, fill_opacity=0.2).shift(RIGHT * 5.5 + DOWN * 0.5)
        net_b_label = Text("Net B", font_size=20).move_to(net_b.get_top() + DOWN * 0.3)
        prot_b = Text("Prot Y", font_size=16, color=YELLOW).move_to(net_b.get_center())
        
        gateway_box = Square(side_length=0.8, color=RED, fill_opacity=0.5).shift(RIGHT * 3.5 + DOWN * 0.5)
        gateway_text = Text("GW", font_size=20).move_to(gateway_box)
        
        gateway_vgroup = VGroup(net_a, net_a_label, prot_a, net_b, net_b_label, prot_b, gateway_box, gateway_text)

        # Packet for Gateway
        p2 = Rectangle(width=0.4, height=0.3, color=PURPLE, fill_opacity=0.8).move_to(net_a.get_center())
        
        self.play(Create(gateway_vgroup), Write(gateway_label))
        self.play(p2.animate.move_to(gateway_box.get_center()))
        
        # Transformation inside Gateway
        self.play(p2.animate.set_color(YELLOW).scale(1.2))
        
        self.play(p2.animate.move_to(net_b.get_center()))
        self.wait(2)

        # Final Cleanup
        self.play(FadeOut(router_vgroup), FadeOut(gateway_vgroup), FadeOut(packet1), FadeOut(p2), FadeOut(title), FadeOut(router_label), FadeOut(gateway_label))