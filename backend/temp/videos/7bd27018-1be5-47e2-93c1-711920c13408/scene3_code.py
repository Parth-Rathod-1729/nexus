from manim import *

class Scene3(Scene):
    def construct(self):
        # 1. Title
        title = Text("Routers vs. Gateways", color=WHITE, font_size=36).to_edge(UP)
        self.play(Write(title))

        # 2. Router Setup (Top Half)
        lan_rect = Rectangle(height=1.5, width=2, color=BLUE, fill_opacity=0.1).shift(LEFT * 4 + UP * 0.5)
        wan_rect = Rectangle(height=1.5, width=2, color=TEAL, fill_opacity=0.1).shift(RIGHT * 4 + UP * 0.5)
        lan_label = Text("LAN", font_size=20, color=BLUE).next_to(lan_rect, UP)
        wan_label = Text("WAN", font_size=20, color=TEAL).next_to(wan_rect, UP)
        
        router = Circle(radius=0.4, color=GOLD, fill_opacity=0.8).move_to(UP * 0.5)
        router_text = Text("Router", font_size=20).next_to(router, DOWN)
        routing_table = Text("192.168 -> Port 1", font_size=18, color=YELLOW).next_to(router, UP)
        
        router_group = VGroup(lan_rect, wan_rect, lan_label, wan_label, router, router_text)
        self.play(Create(router_group))

        # 3. Router Animation (Pathfinding)
        packet_r = Dot(color=WHITE).move_to(lan_rect.get_center())
        self.play(packet_r.animate.move_to(router.get_center()), run_time=1.5)
        self.play(Write(routing_table))
        self.play(packet_r.animate.move_to(wan_rect.get_center()), run_time=1.5)
        self.play(FadeOut(packet_r), FadeOut(routing_table))

        # 4. Gateway Setup (Bottom Half)
        divider = Line(LEFT * 6, RIGHT * 6).shift(DOWN * 1)
        self.play(Create(divider))
        
        net_a = Rectangle(height=1.2, width=1.5, color=GREEN).shift(LEFT * 4 + DOWN * 2.5)
        net_b = Rectangle(height=1.2, width=1.5, color=RED).shift(RIGHT * 4 + DOWN * 2.5)
        a_label = Text("Network A", font_size=18).next_to(net_a, UP)
        b_label = Text("Network B", font_size=18).next_to(net_b, UP)
        
        gateway = Rectangle(height=1, width=1.2, color=PURPLE, fill_opacity=0.7).shift(DOWN * 2.5)
        gateway_text = Text("Gateway", font_size=20).next_to(gateway, DOWN)
        translation_label = Text("Translating Protocol...", font_size=16, color=YELLOW).next_to(gateway, UP)

        gateway_group = VGroup(net_a, net_b, a_label, b_label, gateway, gateway_text)
        self.play(Create(gateway_group))

        # 5. Gateway Animation (Translation)
        packet_g = Circle(radius=0.1, color=BLUE, fill_opacity=1).move_to(net_a.get_center())
        self.play(packet_g.animate.move_to(gateway.get_center()), run_time=1.5)
        
        self.play(Write(translation_label))
        # Transform packet appearance to show protocol conversion
        new_packet_g = Square(side_length=0.2, color=RED, fill_opacity=1).move_to(gateway.get_center())
        self.play(Transform(packet_g, new_packet_g))
        self.wait(0.5)
        
        self.play(packet_g.animate.move_to(net_b.get_center()), run_time=1.5)
        self.play(FadeOut(translation_label), FadeOut(packet_g))

        # 6. Conclusion
        summary = Text("Routers connect paths. Gateways translate languages.", font_size=24, color=GOLD).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)