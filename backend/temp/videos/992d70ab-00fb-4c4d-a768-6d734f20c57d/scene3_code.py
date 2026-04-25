from manim import *

class Scene3(Scene):
    def construct(self):
        # Title
        title = Text("Routers vs Gateways", color=WHITE).scale(0.8)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        # Left Side: Router
        router_label = Text("Router", color=BLUE).scale(0.6)
        router_box = Rectangle(color=BLUE, height=1, width=2, fill_opacity=0.2)
        router_group = VGroup(router_box, router_label).shift(LEFT * 3 + UP * 0.5)
        
        lan_label = Text("LAN", color=TEAL).scale(0.5)
        lan_box = Square(color=TEAL, side_length=1.2, fill_opacity=0.1)
        lan_group = VGroup(lan_box, lan_label).next_to(router_group, LEFT, buff=1)
        
        internet_label = Text("Internet", color=WHITE).scale(0.5)
        internet_circle = Circle(color=WHITE, radius=0.7, fill_opacity=0.1)
        internet_group = VGroup(internet_circle, internet_label).next_to(router_group, RIGHT, buff=1)
        
        arr1 = Arrow(lan_group.get_right(), router_group.get_left(), buff=0.1, color=GRAY)
        arr2 = Arrow(router_group.get_right(), internet_group.get_left(), buff=0.1, color=GRAY)
        
        router_desc = Text("IP Routing", color=BLUE).scale(0.4).next_to(router_group, DOWN)

        # Right Side: Gateway
        gateway_label = Text("Gateway", color=GOLD).scale(0.6)
        gateway_box = Rectangle(color=GOLD, height=1, width=2, fill_opacity=0.2)
        gateway_group = VGroup(gateway_box, gateway_label).shift(RIGHT * 3 + UP * 0.5)
        
        sys_a = Square(color=RED, side_length=1.2, fill_opacity=0.1)
        label_a = Text("System A", color=RED).scale(0.4).move_to(sys_a.get_center())
        sys_a_group = VGroup(sys_a, label_a).next_to(gateway_group, LEFT, buff=1)
        
        sys_b = Square(color=GREEN, side_length=1.2, fill_opacity=0.1)
        label_b = Text("System B", color=GREEN).scale(0.4).move_to(sys_b.get_center())
        sys_b_group = VGroup(sys_b, label_b).next_to(gateway_group, RIGHT, buff=1)
        
        arr3 = Arrow(sys_a_group.get_right(), gateway_group.get_left(), buff=0.1, color=GRAY)
        arr4 = Arrow(gateway_group.get_right(), sys_b_group.get_left(), buff=0.1, color=GRAY)
        
        gateway_desc = Text("Protocol Conversion", color=GOLD).scale(0.4).next_to(gateway_group, DOWN)

        # Animations
        self.play(
            Create(lan_group), Create(router_group), Create(internet_group),
            Create(arr1), Create(arr2), Write(router_desc)
        )
        self.wait(1)

        # Packet Animation for Router
        packet_r = Dot(color=YELLOW).move_to(lan_group.get_center())
        self.play(packet_r.animate.move_to(router_group.get_center()), run_time=1)
        self.play(packet_r.animate.move_to(internet_group.get_center()), run_time=1)
        self.remove(packet_r)

        self.play(
            Create(sys_a_group), Create(gateway_group), Create(sys_b_group),
            Create(arr3), Create(arr4), Write(gateway_desc)
        )
        self.wait(1)

        # Packet Animation for Gateway (Conversion)
        packet_g = Dot(color=RED).move_to(sys_a_group.get_center())
        self.play(packet_g.animate.move_to(gateway_group.get_center()), run_time=1)
        self.play(packet_g.animate.set_color(GREEN).move_to(sys_b_group.get_center()), run_time=1)
        
        # Summary text
        summary = Text("Routers connect via IP | Gateways convert Protocols", color=WHITE).scale(0.5)
        summary.to_edge(DOWN, buff=1)
        self.play(Write(summary))
        self.wait(2)