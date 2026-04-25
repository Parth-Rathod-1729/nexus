from manim import *

class Scene3(Scene):
    def construct(self):
        # Title and Footer
        title = Text("Inter-Network Communication", color=WHITE, font_size=32).to_edge(UP)
        explanation = Text("Router: Routing Paths | Gateway: Protocol Translation", font_size=20, color=GOLD).to_edge(DOWN)
        self.add(title, explanation)

        # Labels for entities
        lan_label = Text("LAN 1", font_size=18).move_to(LEFT * 5 + UP * 1)
        wan_label = Text("External Network", font_size=18).move_to(RIGHT * 5 + UP * 1)

        # Router Creation
        router_body = Circle(radius=0.6, color=BLUE, fill_opacity=0.3)
        router_txt = Text("Router", font_size=20).next_to(router_body, UP)
        router = VGroup(router_body, router_txt).move_to(LEFT * 2.5)

        # Routing Table
        table_rect = Rectangle(height=0.8, width=1.2, color=WHITE, fill_opacity=0.1).next_to(router_body, DOWN, buff=0.2)
        table_txt = Text("IP Table", font_size=14).move_to(table_rect.get_center())
        routing_table = VGroup(table_rect, table_txt)

        # Gateway Creation
        gateway_body = Rectangle(height=1.2, width=1.5, color=TEAL, fill_opacity=0.3)
        gateway_txt = Text("Gateway", font_size=20).next_to(gateway_body, UP)
        gateway = VGroup(gateway_body, gateway_txt).move_to(RIGHT * 1.5)

        # Connection Lines
        line1 = Line(LEFT * 5, router_body.get_left(), color=GRAY)
        line2 = Arrow(router_body.get_right(), gateway_body.get_left(), buff=0.1, color=GRAY)
        line3 = Line(gateway_body.get_right(), RIGHT * 5, color=GRAY)

        # Packet Creation
        packet_sq = Square(side_length=0.5, color=YELLOW, fill_opacity=1)
        packet_lbl = Text("IP", font_size=16, color=BLACK).move_to(packet_sq.get_center())
        packet = VGroup(packet_sq, packet_lbl).move_to(LEFT * 5)

        # Animation Sequence
        self.play(Create(line1), Create(line2), Create(line3))
        self.play(Create(router), Create(gateway), Write(lan_label), Write(wan_label))
        self.wait(1)

        # Phase 1: Router processing
        self.play(packet.animate.move_to(router_body.get_center()), run_time=1.5)
        self.play(FadeIn(routing_table))
        self.play(routing_table.animate.set_color(YELLOW), run_time=0.5)
        self.play(routing_table.animate.set_color(WHITE), run_time=0.5)
        self.wait(0.5)
        
        # Phase 2: Moving to Gateway
        self.play(FadeOut(routing_table))
        self.play(packet.animate.move_to(gateway_body.get_center()), run_time=1.5)

        # Phase 3: Protocol Translation (Gateway Transformation)
        new_packet_sq = Square(side_length=0.5, color=RED, fill_opacity=1).move_to(gateway_body.get_center())
        new_packet_lbl = Text("TCP", font_size=16, color=WHITE).move_to(new_packet_sq.get_center())
        translated_packet = VGroup(new_packet_sq, new_packet_lbl)

        self.play(
            Transform(packet, translated_packet),
            gateway_body.animate.set_fill(color=RED, opacity=0.5),
            run_time=1
        )
        self.play(gateway_body.animate.set_fill(color=TEAL, opacity=0.3), run_time=0.5)
        self.wait(0.5)

        # Phase 4: Forwarding to WAN
        self.play(packet.animate.move_to(RIGHT * 5), run_time=1.5)
        
        # Closing
        self.wait(2)

        # Clean up
        self.play(
            FadeOut(packet), 
            FadeOut(router), 
            FadeOut(gateway), 
            FadeOut(line1), 
            FadeOut(line2), 
            FadeOut(line3),
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(lan_label),
            FadeOut(wan_label)
        )