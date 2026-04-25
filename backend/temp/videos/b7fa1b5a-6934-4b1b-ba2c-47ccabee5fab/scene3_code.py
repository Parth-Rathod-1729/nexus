from manim import *

class Scene3(Scene):
    def construct(self):
        # 1. Setup Title
        title = Text("Routers and Gateways", color=WHITE).scale(0.8).to_edge(UP)
        self.add(title)

        # 2. Router Section Setup
        router = Square(side_length=1.2, color=BLUE, fill_opacity=0.2).move_to(ORIGIN)
        router_label = Text("Router", font_size=28, color=BLUE).next_to(router, DOWN)
        
        net_a = Circle(radius=0.8, color=GREEN).shift(LEFT * 4)
        net_b = Circle(radius=0.8, color=GOLD).shift(RIGHT * 4)
        label_a = Text("Local Net", font_size=20).next_to(net_a, UP)
        label_b = Text("Internet", font_size=20).next_to(net_b, UP)
        
        arrow_in = Arrow(net_a.get_right(), router.get_left(), buff=0.1, color=WHITE)
        arrow_out = Arrow(router.get_right(), net_b.get_left(), buff=0.1, color=WHITE)
        
        router_group = VGroup(router, router_label, net_a, net_b, label_a, label_b, arrow_in, arrow_out)
        self.play(Create(router_group), run_time=2)

        # 3. Router Animation (IP Routing)
        packet = Dot(color=RED).move_to(net_a.get_center())
        ip_label = MathTex(r"192.168.1.1 \to 8.8.8.8", font_size=24, color=RED).next_to(router, UP)
        
        self.play(packet.animate.move_to(router.get_center()), run_time=1)
        self.play(Write(ip_label))
        self.play(packet.animate.move_to(net_b.get_center()), run_time=1)
        self.wait(0.5)
        
        # 4. Transition to Gateway
        gateway = Rectangle(width=2.0, height=1.2, color=TEAL, fill_opacity=0.2).move_to(ORIGIN)
        gateway_label = Text("Gateway", font_size=28, color=TEAL).next_to(gateway, DOWN)
        net_c_shape = Square(side_length=1.6, color=GOLD).move_to(net_b.get_center())
        label_c = Text("Legacy Net", font_size=20).next_to(net_c_shape, UP)

        self.play(
            FadeOut(router), FadeOut(router_label), FadeOut(ip_label), FadeOut(packet),
            FadeOut(net_b), FadeOut(label_b),
            Create(gateway), Create(gateway_label), Create(net_c_shape), Write(label_c)
        )

        # 5. Gateway Animation (Protocol Conversion)
        # Packet A (Circle) to Packet B (Square)
        p_start = Circle(radius=0.1, color=WHITE, fill_opacity=1).move_to(net_a.get_center())
        conv_text = Text("Protocol Translation", font_size=22, color=YELLOW).next_to(gateway, UP)
        
        self.play(p_start.animate.move_to(gateway.get_center()), run_time=1)
        
        p_end = Square(side_length=0.2, color=YELLOW, fill_opacity=1).move_to(gateway.get_center())
        self.play(
            ReplacementTransform(p_start, p_end),
            Write(conv_text),
            run_time=1
        )
        
        self.play(p_end.animate.move_to(net_c_shape.get_center()), run_time=1)
        self.wait(2)