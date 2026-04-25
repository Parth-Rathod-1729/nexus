from manim import *

class Scene3(Scene):
    def construct(self):
        # Title
        title = Text("Router and Gateway", color=WHITE, font_size=36).to_edge(UP)
        self.play(Write(title))

        # Router Section
        router_circ = Circle(color=BLUE, fill_opacity=0.5).scale(0.7)
        router_text = Text("Router", font_size=24).move_to(router_circ)
        router_group = VGroup(router_circ, router_text)

        lan_rect = Rectangle(color=GREEN, height=1.5, width=2, fill_opacity=0.2).to_edge(LEFT, buff=1)
        lan_label = Text("LAN", font_size=20).next_to(lan_rect, UP)
        
        wan_rect = Rectangle(color=TEAL, height=1.5, width=2, fill_opacity=0.2).to_edge(RIGHT, buff=1)
        wan_label = Text("WAN (Internet)", font_size=20).next_to(wan_rect, UP)

        arrow_in = Arrow(lan_rect.get_right(), router_circ.get_left(), buff=0.1, color=WHITE)
        arrow_out = Arrow(router_circ.get_right(), wan_rect.get_left(), buff=0.1, color=WHITE)
        
        routing_label = MathTex(r"\text{IP Routing}", color=YELLOW).scale(0.8).next_to(router_circ, DOWN)

        self.play(
            Create(lan_rect), Write(lan_label),
            Create(wan_rect), Write(wan_label),
            Create(router_group)
        )
        self.play(Create(arrow_in), Create(arrow_out), Write(routing_label))

        # Packet movement for Router
        packet = Dot(color=WHITE).move_to(lan_rect.get_center())
        self.play(packet.animate.move_to(router_circ.get_center()), run_time=1)
        self.play(packet.animate.move_to(wan_rect.get_center()), run_time=1)
        self.play(FadeOut(packet))
        
        self.wait(1)

        # Transition to Gateway
        self.play(
            FadeOut(lan_rect), FadeOut(lan_label), FadeOut(wan_rect), FadeOut(wan_label), 
            FadeOut(arrow_in), FadeOut(arrow_out), FadeOut(routing_label), FadeOut(router_group)
        )

        # Gateway Section
        gateway_box = Rectangle(color=GOLD, height=1.5, width=2.5, fill_opacity=0.4)
        gw_label = Text("Gateway", font_size=24).move_to(gateway_box)
        translator_text = Text("Protocol Translator", font_size=20, color=GOLD).next_to(gateway_box, DOWN)
        
        proto_a_box = Square(side_length=1.5, color=RED, fill_opacity=0.2).to_edge(LEFT, buff=1.5)
        proto_a_text = Text("Protocol A", font_size=20, color=RED).next_to(proto_a_box, UP)
        
        proto_b_box = Circle(radius=0.75, color=TEAL, fill_opacity=0.2).to_edge(RIGHT, buff=1.5)
        proto_b_text = Text("Protocol B", font_size=20, color=TEAL).next_to(proto_b_box, UP)

        self.play(Create(gateway_box), Write(gw_label), Write(translator_text))
        self.play(
            Create(proto_a_box), Write(proto_a_text),
            Create(proto_b_box), Write(proto_b_text)
        )

        # Packet conversion movement
        p2 = Dot(color=RED).move_to(proto_a_box.get_center())
        self.play(p2.animate.move_to(gateway_box.get_center()), run_time=1.5)
        self.play(p2.animate.set_color(TEAL).move_to(proto_b_box.get_center()), run_time=1.5)

        self.wait(2)
        self.play(FadeOut(title), FadeOut(gateway_box), FadeOut(gw_label), FadeOut(translator_text), FadeOut(proto_a_box), FadeOut(proto_a_text), FadeOut(proto_b_box), FadeOut(proto_b_text), FadeOut(p2))