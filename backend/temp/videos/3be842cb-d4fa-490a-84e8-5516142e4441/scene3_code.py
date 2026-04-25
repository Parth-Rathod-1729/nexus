from manim import *

class Scene3(Scene):
    def construct(self):
        # Title
        title = Text("Network Interconnection", color=WHITE).scale(0.8)
        title.to_edge(UP)
        self.add(title)

        # --- ROUTER SECTION ---
        router_box = Rectangle(height=1.5, width=2.2, color=BLUE, fill_opacity=0.2)
        router_label = Text("Router", color=BLUE).scale(0.6).move_to(router_box.get_center())
        router_group = VGroup(router_box, router_label).shift(LEFT * 3 + UP * 0.5)

        lan_text = Text("LAN", color=GOLD).scale(0.5).next_to(router_group, LEFT, buff=1)
        wan_text = Text("WAN", color=GOLD).scale(0.5).next_to(router_group, RIGHT, buff=1)
        
        arrow_in = Arrow(lan_text.get_right(), router_group.get_left(), color=WHITE)
        arrow_out = Arrow(router_group.get_right(), wan_text.get_left(), color=WHITE)

        ip_table = Rectangle(height=1.2, width=2, color=WHITE).scale(0.6)
        ip_table.next_to(router_group, DOWN, buff=0.3)
        ip_text = MathTex(r"192.168.1.1 \\ \rightarrow 10.0.0.5", color=YELLOW).scale(0.5).move_to(ip_table.get_center())
        table_label = Text("Routing Table", color=WHITE).scale(0.3).next_to(ip_table, DOWN, buff=0.1)
        table_group = VGroup(ip_table, ip_text, table_label)

        self.play(Create(router_group), Write(lan_text), Write(wan_text))
        self.play(Create(arrow_in), Create(arrow_out), FadeIn(table_group))

        # Packet movement
        packet = Dot(color=YELLOW).move_to(lan_text.get_center())
        self.play(packet.animate.move_to(router_group.get_center()), run_time=1)
        self.play(Indicate(ip_table, color=YELLOW), run_time=1)
        self.play(packet.animate.move_to(wan_text.get_center()), run_time=1)
        self.play(FadeOut(packet))

        self.wait(1)

        # --- GATEWAY SECTION ---
        # Shift router logic to allow space or clear
        self.play(
            VGroup(router_group, lan_text, wan_text, arrow_in, arrow_out, table_group).animate.scale(0.7).to_edge(LEFT)
        )

        gateway_box = Square(side_length=1.8, color=TEAL, fill_opacity=0.2)
        gateway_label = Text("Gateway", color=TEAL).scale(0.6).move_to(gateway_box.get_center())
        converter_label = Text("Protocol Converter", color=TEAL).scale(0.4).next_to(gateway_box, UP)
        gateway_group = VGroup(gateway_box, gateway_label, converter_label).shift(RIGHT * 3)

        p1_label = Text("HTTP", color=RED).scale(0.6).next_to(gateway_group, LEFT, buff=0.8)
        p2_label = Text("MQTT", color=GREEN).scale(0.6).next_to(gateway_group, RIGHT, buff=0.8)

        line_left = Line(p1_label.get_right(), gateway_group.get_left(), color=WHITE)
        line_right = Line(gateway_group.get_right(), p2_label.get_left(), color=WHITE)

        self.play(Create(gateway_group), Write(p1_label), Write(p2_label))
        self.play(Create(line_left), Create(line_right))

        # Translation animation
        data_packet = Dot(color=RED).move_to(p1_label.get_center())
        self.play(data_packet.animate.move_to(gateway_group.get_center()), run_time=1)
        self.play(data_packet.animate.set_color(GREEN), Flash(gateway_group, color=WHITE))
        self.play(data_packet.animate.move_to(p2_label.get_center()), run_time=1)
        self.play(FadeOut(data_packet))

        # Final Summary Text
        summary = Text("Routers connect networks. Gateways translate protocols.", color=WHITE).scale(0.5)
        summary.to_edge(DOWN, buff=0.5)
        self.play(Write(summary))
        self.wait(2)