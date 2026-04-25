from manim import *

class Scene3(Scene):
    def construct(self):
        # Title
        title = Text("Network Interconnectivity", font_size=36, color=WHITE).to_edge(UP)
        
        # --- Router Section (Top) ---
        router_title = Text("IP Routing", font_size=24, color=TEAL).shift(UP * 2.2 + LEFT * 3)
        lan = Rectangle(width=2, height=1.2, color=BLUE, fill_opacity=0.1).shift(UP * 0.8 + LEFT * 4)
        lan_label = Text("LAN", font_size=20).move_to(lan.get_center())
        
        router = Circle(radius=0.5, color=TEAL, fill_opacity=0.3).shift(UP * 0.8 + LEFT * 0)
        router_label = Text("Router", font_size=18).next_to(router, DOWN, buff=0.1)
        
        wan = Circle(radius=0.7, color=WHITE, fill_opacity=0.1).shift(UP * 0.8 + RIGHT * 4)
        wan_label = Text("WAN", font_size=20).move_to(wan.get_center())
        
        arrow1 = Arrow(lan.get_right(), router.get_left(), color=WHITE, buff=0.1)
        arrow2 = Arrow(router.get_right(), wan.get_left(), color=WHITE, buff=0.1)
        
        table_rect = Rectangle(width=1.8, height=0.6, color=GOLD, fill_opacity=0.2).next_to(router, UP, buff=0.2)
        table_text = Text("IP -> Path", font_size=22, color=GOLD).move_to(table_rect.get_center())
        routing_table = VGroup(table_rect, table_text)

        router_group = VGroup(lan, lan_label, router, router_label, wan, wan_label, arrow1, arrow2, router_title)
        
        # --- Gateway Section (Bottom) ---
        gateway_title = Text("Protocol Conversion", font_size=24, color=GREEN).shift(DOWN * 0.5 + LEFT * 3)
        net_a = Square(side_length=1.2, color=RED, fill_opacity=0.1).shift(DOWN * 2 + LEFT * 4)
        net_a_label = Text("Proprietary", font_size=18).move_to(net_a.get_center())
        
        gateway = Rectangle(width=1.6, height=1.0, color=GREEN, fill_opacity=0.3).shift(DOWN * 2 + LEFT * 0)
        gateway_label = Text("Gateway", font_size=18).next_to(gateway, DOWN, buff=0.1)
        
        net_b = Circle(radius=0.6, color=YELLOW, fill_opacity=0.1).shift(DOWN * 2 + RIGHT * 4)
        net_b_label = Text("TCP/IP", font_size=18).move_to(net_b.get_center())
        
        arrow3 = Arrow(net_a.get_right(), gateway.get_left(), color=WHITE, buff=0.1)
        arrow4 = Arrow(gateway.get_right(), net_b.get_left(), color=WHITE, buff=0.1)
        
        trans_label = Text("Translate", font_size=20, color=GOLD).next_to(gateway, UP, buff=0.2)
        
        gateway_group = VGroup(net_a, net_a_label, gateway, gateway_label, net_b, net_b_label, arrow3, arrow4, gateway_title)

        # --- Animations ---
        self.play(Write(title))
        self.wait(1)
        
        # Show Router Process
        self.play(Create(router_group))
        self.play(FadeIn(routing_table))
        
        packet1 = Dot(color=BLUE).move_to(lan.get_center())
        self.play(packet1.animate.move_to(router.get_center()), run_time=1)
        self.play(routing_table.animate.scale(1.2).set_color(YELLOW), run_time=0.5)
        self.play(routing_table.animate.scale(0.833).set_color(GOLD), run_time=0.5)
        self.play(packet1.animate.move_to(wan.get_center()), run_time=1)
        self.play(FadeOut(packet1))
        
        self.wait(1)
        
        # Show Gateway Process
        self.play(Create(gateway_group))
        self.play(Write(trans_label))
        
        packet2 = Dot(color=RED).move_to(net_a.get_center())
        self.play(packet2.animate.move_to(gateway.get_center()), run_time=1)
        self.play(packet2.animate.set_color(YELLOW), run_time=0.5)
        self.play(packet2.animate.move_to(net_b.get_center()), run_time=1)
        self.play(FadeOut(packet2))
        
        self.wait(2)
        
        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(router_group),
            FadeOut(routing_table),
            FadeOut(gateway_group),
            FadeOut(trans_label)
        )