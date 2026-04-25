from manim import *

class Scene3(Scene):
    def construct(self):
        # Header
        title = Text("Layer 3 and Above: Routers & Gateways", color=GOLD, font_size=36)
        title.to_edge(UP)

        # --- Router Section (Top) ---
        router_circle = Circle(radius=0.5, color=BLUE, fill_opacity=0.2)
        router_label = Text("Router", font_size=20).next_to(router_circle, DOWN)
        router_icon = VGroup(
            router_circle,
            Line(router_circle.get_left(), router_circle.get_right(), color=BLUE),
            Line(router_circle.get_top(), router_circle.get_bottom(), color=BLUE),
            router_label
        ).shift(UP * 1)

        lan_box = Rectangle(width=2, height=1, color=TEAL).shift(LEFT * 4 + UP * 1)
        lan_text = Text("LAN (Local)", font_size=18).move_to(lan_box)
        wan_box = Rectangle(width=2, height=1, color=RED).shift(RIGHT * 4 + UP * 1)
        wan_text = Text("WAN (Internet)", font_size=18).move_to(wan_box)

        routing_table = Rectangle(width=1.8, height=0.8, color=WHITE).shift(UP * 2.5)
        # Using Text instead of MathTex to avoid subprocess errors if LaTeX is missing
        table_content = Text("192.168.1.1 -> Eth0", font_size=16).move_to(routing_table)
        table_label = Text("Routing Table", font_size=14).next_to(routing_table, UP, buff=0.1)
        table_group = VGroup(routing_table, table_content, table_label)

        # --- Gateway Section (Bottom) ---
        gateway_rect = Rectangle(width=1.2, height=1.6, color=GOLD, fill_opacity=0.2).shift(DOWN * 1.5)
        gateway_label = Text("Gateway", font_size=20).next_to(gateway_rect, DOWN)
        
        net_a = Square(side_length=1.2, color=BLUE).shift(LEFT * 4 + DOWN * 1.5)
        net_a_label = Text("Legacy Protocol", font_size=18).next_to(net_a, UP)
        net_b = Circle(radius=0.6, color=GREEN).shift(RIGHT * 4 + DOWN * 1.5)
        net_b_label = Text("Modern Protocol", font_size=18).next_to(net_b, UP)

        # Arrows
        arrow_router_in = Arrow(lan_box.get_right(), router_circle.get_left(), buff=0.1, color=WHITE)
        arrow_router_out = Arrow(router_circle.get_right(), wan_box.get_left(), buff=0.1, color=WHITE)
        arrow_gw_in = Arrow(net_a.get_right(), gateway_rect.get_left(), buff=0.1, color=WHITE)
        arrow_gw_out = Arrow(gateway_rect.get_right(), net_b.get_left(), buff=0.1, color=WHITE)

        # --- Animations ---
        self.play(Write(title))
        self.play(
            Create(lan_box), Write(lan_text),
            Create(wan_box), Write(wan_text),
            Create(router_icon)
        )
        self.play(Create(table_group))
        
        # Packet Routing Animation
        packet = Dot(color=YELLOW).move_to(lan_box.get_center())
        self.play(packet.animate.move_to(router_circle.get_center()), Create(arrow_router_in))
        self.play(Indicate(table_group, color=YELLOW))
        self.play(packet.animate.move_to(wan_box.get_center()), Create(arrow_router_out))
        self.play(FadeOut(packet))

        self.wait(0.5)

        # Gateway Animation
        self.play(
            Create(net_a), Write(net_a_label),
            Create(net_b), Write(net_b_label),
            Create(gateway_rect), Write(gateway_label)
        )

        # Protocol Translation Animation
        proto_packet = Square(side_length=0.2, color=BLUE, fill_opacity=1).move_to(net_a.get_center())
        self.play(proto_packet.animate.move_to(gateway_rect.get_center()), Create(arrow_gw_in))
        
        # Change format inside gateway
        new_packet = Circle(radius=0.1, color=GREEN, fill_opacity=1).move_to(gateway_rect.get_center())
        self.play(ReplacementTransform(proto_packet, new_packet))
        
        self.play(new_packet.animate.move_to(net_b.get_center()), Create(arrow_gw_out))
        
        self.wait(2)

        # Final Clean up
        self.play(FadeOut(VGroup(title, lan_box, wan_box, router_icon, table_group, net_a, net_b, gateway_rect, new_packet, arrow_router_in, arrow_router_out, arrow_gw_in, arrow_gw_out, lan_text, wan_text, net_a_label, net_b_label, gateway_label)))

        self.wait(1)