from manim import *

class Scene3(Scene):
    def construct(self):
        # Title
        title = Text("Routing and Gateways", color=WHITE, font_size=36).to_edge(UP)
        self.play(Write(title))

        # --- Router Section ---
        router_group = VGroup()
        
        lan_box = Rectangle(width=2.5, height=1.5, color=BLUE, fill_opacity=0.3).shift(LEFT * 4 + UP * 1)
        lan_label = Text("Home LAN", font_size=20, color=BLUE).next_to(lan_box, UP)
        
        router_circle = Circle(radius=0.6, color=GOLD, fill_opacity=0.5).shift(UP * 1)
        router_label = Text("Router", font_size=20, color=GOLD).next_to(router_circle, UP)
        
        wan_box = Rectangle(width=2.5, height=1.5, color=GREEN, fill_opacity=0.3).shift(RIGHT * 4 + UP * 1)
        wan_label = Text("Internet (WAN)", font_size=20, color=GREEN).next_to(wan_box, UP)
        
        arrow_r1 = Arrow(lan_box.get_right(), router_circle.get_left(), buff=0.1, color=WHITE)
        arrow_r2 = Arrow(router_circle.get_right(), wan_box.get_left(), buff=0.1, color=WHITE)
        
        routing_logic = MathTex(r"192.168.1.5 \rightarrow 203.0.113.1", font_size=22, color=YELLOW).next_to(router_circle, DOWN, buff=0.2)
        
        router_group.add(lan_box, lan_label, router_circle, router_label, wan_box, wan_label, arrow_r1, arrow_r2, routing_logic)
        
        self.play(Create(router_group))
        self.wait(2)

        # --- Gateway Section ---
        gateway_group = VGroup()
        
        net_a = Rectangle(width=2.5, height=1.5, color=TEAL, fill_opacity=0.3).shift(LEFT * 4 + DOWN * 2)
        label_a = Text("TCP/IP Net", font_size=20, color=TEAL).next_to(net_a, UP)
        
        gateway_sq = Square(side_length=1.2, color=RED, fill_opacity=0.5).shift(DOWN * 2)
        gateway_label = Text("Gateway", font_size=20, color=RED).next_to(gateway_sq, UP)
        
        net_b = Rectangle(width=2.5, height=1.5, color=WHITE, fill_opacity=0.2).shift(RIGHT * 4 + DOWN * 2)
        label_b = Text("Legacy Net", font_size=20, color=WHITE).next_to(net_b, UP)
        
        arrow_g1 = Arrow(net_a.get_right(), gateway_sq.get_left(), buff=0.1, color=WHITE)
        arrow_g2 = Arrow(gateway_sq.get_right(), net_b.get_left(), buff=0.1, color=WHITE)
        
        translation_txt = Text("Protocol Translation", color=GOLD, font_size=22).next_to(gateway_sq, DOWN, buff=0.2)
        
        gateway_group.add(net_a, label_a, gateway_sq, gateway_label, net_b, label_b, arrow_g1, arrow_g2, translation_txt)
        
        self.play(Create(gateway_group))
        self.wait(3)

        # Final cleanup for exit
        self.play(FadeOut(router_group), FadeOut(gateway_group), FadeOut(title))