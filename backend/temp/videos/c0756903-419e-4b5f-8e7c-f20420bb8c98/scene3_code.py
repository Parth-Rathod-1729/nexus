from manim import *

class Scene3(Scene):
    def construct(self):
        # Title
        title = Text("Inter-Network Communication", font_size=36, color=WHITE).to_edge(UP)
        self.add(title)

        # Router Section (Left)
        router = Circle(radius=0.6, color=BLUE, fill_opacity=0.2)
        router.move_to(LEFT * 3.5 + UP * 0.5)
        router_label = Text("Router", font_size=24, color=BLUE).next_to(router, UP)
        ip_label = Text("IP: 192.168.1.1", font_size=24, color=YELLOW).next_to(router, DOWN)

        # Networks nodes
        net_a = Rectangle(width=1, height=0.6, color=GOLD).move_to(LEFT * 1 + UP * 1.5)
        net_b = Rectangle(width=1, height=0.6, color=GOLD).move_to(LEFT * 1 + DOWN * 0.5)
        net_c = Rectangle(width=1, height=0.6, color=GOLD).move_to(LEFT * 1 + DOWN * 2.0)
        
        nets = VGroup(net_a, net_b, net_c)
        net_labels = VGroup(
            Text("LAN 1", font_size=18).move_to(net_a),
            Text("WAN", font_size=18).move_to(net_b),
            Text("LAN 2", font_size=18).move_to(net_c)
        )

        path1 = Line(router.get_right(), net_a.get_left(), stroke_width=2)
        path2 = Line(router.get_right(), net_b.get_left(), stroke_width=2)
        path3 = Line(router.get_right(), net_c.get_left(), stroke_width=2)
        paths = VGroup(path1, path2, path3)

        # Router Pathfinding Animation
        self.play(Create(router), Write(router_label))
        self.play(Create(nets), Create(net_labels), Create(paths))
        self.play(Write(ip_label))
        
        highlight_arrow = Arrow(router.get_right(), net_b.get_left(), color=YELLOW, buff=0.1)
        self.play(Create(highlight_arrow), path2.animate.set_stroke(color=YELLOW, width=4))
        self.wait(1)

        # Gateway Section (Right)
        gateway = Square(side_length=1.5, color=TEAL, fill_opacity=0.3)
        gateway.move_to(RIGHT * 3 + UP * 0.5)
        gw_label = Text("Gateway", font_size=24, color=TEAL).next_to(gateway, UP)
        conv_text = Text("Protocol\nConverter", font_size=20).move_to(gateway)

        # Data Packets for Gateway
        packet_in = Square(side_length=0.4, color=RED, fill_opacity=0.8).move_to(RIGHT * 1 + UP * 0.5)
        packet_out = Circle(radius=0.2, color=GREEN, fill_opacity=0.8).move_to(RIGHT * 5 + UP * 0.5)
        
        in_label = Text("TCP/IP", font_size=18, color=RED).next_to(packet_in, DOWN)
        out_label = Text("OSI/Other", font_size=18, color=GREEN).next_to(packet_out, DOWN)

        # Gateway Animation
        self.play(Create(gateway), Write(gw_label), Write(conv_text))
        self.play(Create(packet_in), Write(in_label))
        
        self.play(
            packet_in.animate.move_to(gateway.get_center()),
            run_time=1.5
        )
        self.play(
            ReplacementTransform(packet_in, packet_out),
            Write(out_label),
            run_time=1.5
        )

        self.wait(2)

        # Summary Cleanup
        final_group = VGroup(router, router_label, ip_label, nets, net_labels, paths, highlight_arrow, gateway, gw_label, conv_text, packet_out, in_label, out_label)
        self.play(FadeOut(final_group), FadeOut(title))
        self.wait(1)