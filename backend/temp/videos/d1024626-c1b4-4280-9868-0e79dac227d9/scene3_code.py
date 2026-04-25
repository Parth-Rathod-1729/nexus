from manim import *

class Scene3(Scene):
    def construct(self):
        # Title
        title = Text("Inter-Network Communication", color=WHITE).to_edge(UP)
        
        # Router Section (Top Half)
        router_group = VGroup()
        lan = Circle(radius=0.6, color=TEAL, fill_opacity=0.3)
        lan.move_to(LEFT * 4 + UP * 1)
        lan_label = Text("LAN", font_size=20).next_to(lan, DOWN)
        
        router_body = Circle(radius=0.4, color=GOLD, fill_opacity=0.9)
        router_body.move_to(LEFT * 1.5 + UP * 1)
        router_label = Text("R", color=BLACK, font_size=24).move_to(router_body)
        router_text = Text("Router: IP Path", font_size=24, color=GOLD).next_to(router_body, UP)
        
        internet = Rectangle(width=1.5, height=1, color=BLUE, fill_opacity=0.3)
        internet.move_to(RIGHT * 1 + UP * 1)
        internet_label = Text("Internet", font_size=20).next_to(internet, DOWN)
        
        arrow_r1 = Arrow(lan.get_right(), router_body.get_left(), buff=0.1)
        arrow_r2 = Arrow(router_body.get_right(), internet.get_left(), buff=0.1)
        
        router_group.add(lan, lan_label, router_body, router_label, router_text, internet, internet_label, arrow_r1, arrow_r2)
        
        # Gateway Section (Bottom Half)
        gateway_group = VGroup()
        net_a = Rectangle(width=1.2, height=0.8, color=RED, fill_opacity=0.3)
        net_a.move_to(LEFT * 4 + DOWN * 2)
        label_a = Text("Model A", font_size=20).next_to(net_a, DOWN)
        
        gateway_body = Square(side_length=0.8, color=WHITE, fill_opacity=0.9)
        gateway_body.move_to(LEFT * 1.5 + DOWN * 2)
        gateway_label = Text("G", color=BLACK, font_size=24).move_to(gateway_body)
        gateway_text = Text("Gateway: Conversion", font_size=24, color=WHITE).next_to(gateway_body, UP)
        
        net_b = Circle(radius=0.6, color=GREEN, fill_opacity=0.3)
        net_b.move_to(RIGHT * 1 + DOWN * 2)
        label_b = Text("Model B", font_size=20).next_to(net_b, DOWN)
        
        arrow_g1 = Arrow(net_a.get_right(), gateway_body.get_left(), buff=0.1)
        arrow_g2 = Arrow(gateway_body.get_right(), net_b.get_left(), buff=0.1)
        
        gateway_group.add(net_a, label_a, gateway_body, gateway_label, gateway_text, net_b, label_b, arrow_g1, arrow_g2)
        
        # Animations
        self.play(Write(title))
        self.play(Create(router_group))
        self.wait(1)
        
        # Router movement
        packet1 = Dot(color=YELLOW).move_to(lan.get_center())
        self.play(packet1.animate.move_to(router_body.get_center()))
        self.play(packet1.animate.move_to(internet.get_center()))
        self.play(FadeOut(packet1))
        
        self.play(Create(gateway_group))
        
        # Gateway movement and transformation
        packet2 = Dot(color=RED).move_to(net_a.get_center())
        self.play(packet2.animate.move_to(gateway_body.get_center()))
        
        # Repackaging visual
        converted_packet = Square(side_length=0.2, color=GREEN, fill_opacity=1).move_to(gateway_body.get_center())
        self.play(ReplacementTransform(packet2, converted_packet))
        self.play(converted_packet.animate.move_to(net_b.get_center()))
        
        self.wait(2)

        # Conclusion Text
        summary = Text("Pathfinding vs. Translation", font_size=32, color=YELLOW).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)