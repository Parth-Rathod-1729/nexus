from manim import *

class Scene3(Scene):
    def construct(self):
        # Title
        title = Text("Routers vs Gateways", font_size=36, color=WHITE).to_edge(UP)
        self.add(title)

        # --- ROUTER SECTION ---
        router_group = VGroup()
        router_box = Square(color=BLUE, fill_opacity=0.5).scale(0.7)
        router_text = Text("Router", font_size=20).move_to(router_box)
        
        node_a = Circle(radius=0.3, color=WHITE).shift(LEFT * 3 + DOWN * 1)
        node_b = Circle(radius=0.3, color=WHITE).shift(RIGHT * 3 + UP * 1)
        node_c = Circle(radius=0.3, color=WHITE).shift(RIGHT * 3 + DOWN * 2)
        
        line_a = Line(node_a.get_right(), router_box.get_left(), color=GRAY)
        line_b = Line(router_box.get_right(), node_b.get_left(), color=GRAY)
        line_c = Line(router_box.get_bottom(), node_c.get_top(), color=GRAY)
        
        router_group.add(router_box, router_text, node_a, node_b, node_c, line_a, line_b, line_c)
        
        routing_table = Rectangle(width=2.5, height=1.5, color=GOLD, fill_opacity=0.2).to_edge(RIGHT).shift(UP * 1)
        table_label = Text("Routing Table", font_size=16).next_to(routing_table, UP, buff=0.1)
        table_data = Text("IP -> Path", font_size=20).move_to(routing_table)
        table_group = VGroup(routing_table, table_label, table_data)

        self.play(Create(router_group))
        self.play(FadeIn(table_group))
        
        # Packet movement for Router
        packet = Dot(color=YELLOW).move_to(node_a.get_center())
        self.play(packet.animate.move_to(router_box.get_center()), run_time=1)
        self.play(Indicate(table_group, color=GOLD))
        self.play(packet.animate.move_to(node_b.get_center()), run_time=1)
        self.play(FadeOut(packet))
        
        self.play(FadeOut(router_group), FadeOut(table_group))

        # --- GATEWAY SECTION ---
        gateway = Rectangle(width=1.2, height=3, color=TEAL, fill_opacity=0.6).move_to(ORIGIN)
        gw_label = Text("Gateway", font_size=24).rotate(90 * DEGREES).move_to(gateway)
        
        net_l_bg = Rectangle(width=3, height=4, color=BLUE, fill_opacity=0.1).shift(LEFT * 3.5)
        net_r_bg = Rectangle(width=3, height=4, color=RED, fill_opacity=0.1).shift(RIGHT * 3.5)
        
        label_l = Text("LAN (TCP/IP)", font_size=20, color=BLUE).next_to(net_l_bg, UP)
        label_r = Text("Legacy Net", font_size=20, color=RED).next_to(net_r_bg, UP)
        
        self.play(
            Create(gateway),
            Write(gw_label),
            Create(net_l_bg),
            Create(net_r_bg),
            Write(label_l),
            Write(label_r)
        )

        # Translation visual
        packet_start = Circle(radius=0.15, color=BLUE, fill_opacity=1).move_to(net_l_bg.get_center())
        packet_end = Square(side_length=0.3, color=RED, fill_opacity=1).move_to(gateway.get_center())
        
        arrow_in = Arrow(net_l_bg.get_right(), gateway.get_left(), buff=0.1, color=WHITE)
        arrow_out = Arrow(gateway.get_right(), net_r_bg.get_left(), buff=0.1, color=WHITE)
        
        self.play(Create(arrow_in), Create(arrow_out))
        
        # Animate translation
        self.play(packet_start.animate.move_to(gateway.get_center()), run_time=1.5)
        self.play(
            ReplacementTransform(packet_start, packet_end),
            Flash(gateway, color=WHITE)
        )
        self.play(packet_end.animate.move_to(net_r_bg.get_center()), run_time=1.5)

        self.wait(2)