from manim import *

class Scene3(Scene):
    def construct(self):
        # Title Setup
        title = Text("Routers and Gateways", font_size=32, color=WHITE).to_edge(UP)
        self.add(title)

        # --- ROUTER SECTION ---
        # Router is a circle with a routing table below it
        router_node = Circle(radius=0.6, color=GOLD, fill_opacity=0.3).move_to(ORIGIN)
        router_label = Text("Router", font_size=20).next_to(router_node, UP)
        
        net_lan = Rectangle(width=2.5, height=1.5, color=TEAL).shift(LEFT * 4.5)
        lan_label = Text("Local Network", font_size=18).move_to(net_lan)
        
        net_wan = Rectangle(width=2.5, height=1.5, color=WHITE).shift(RIGHT * 4.5)
        wan_label = Text("Internet", font_size=18).move_to(net_wan)
        
        routing_table = Rectangle(width=2.0, height=1.0, color=YELLOW, fill_opacity=0.1).next_to(router_node, DOWN)
        table_content = Text("IP -> Path", font_size=22).move_to(routing_table)
        
        router_group = VGroup(router_node, router_label, net_lan, lan_label, net_wan, wan_label, routing_table, table_content)
        
        self.play(Create(router_group))

        # Packet movement through router
        packet = Dot(color=RED).move_to(net_lan)
        self.play(packet.animate.move_to(router_node), run_time=1)
        self.play(Indicate(routing_table, color=YELLOW), run_time=0.8)
        self.play(packet.animate.move_to(net_wan), run_time=1)
        self.play(FadeOut(packet))
        
        self.play(FadeOut(router_group))

        # --- GATEWAY SECTION ---
        # Gateway sits between two different protocol architectures
        gateway_node = Rectangle(width=2.0, height=1.5, color=GOLD, fill_opacity=0.4).move_to(ORIGIN)
        gateway_label = Text("Gateway", font_size=24).move_to(gateway_node)
        
        arch_left = Rectangle(width=3.2, height=2.2, color=BLUE, fill_opacity=0.1).shift(LEFT * 4.5)
        arch_left_txt = Text("Protocol A (TCP/IP)", font_size=18, color=BLUE).next_to(arch_left, UP)
        
        arch_right = Rectangle(width=3.2, height=2.2, color=GREEN, fill_opacity=0.1).shift(RIGHT * 4.5)
        arch_right_txt = Text("Protocol B (Legacy)", font_size=18, color=GREEN).next_to(arch_right, UP)
        
        gateway_group = VGroup(gateway_node, gateway_label, arch_left, arch_left_txt, arch_right, arch_right_txt)
        
        self.play(Create(gateway_group))

        # Translation visual
        packet_a = Text("Format: A", color=BLUE, font_size=24).move_to(arch_left)
        packet_b = Text("Format: B", color=GREEN, font_size=24).move_to(arch_right)

        self.play(Write(packet_a))
        self.play(packet_a.animate.move_to(gateway_node), run_time=1.5)
        
        # Translation occurs inside gateway
        self.play(Transform(packet_a, packet_b.move_to(gateway_node)), run_time=0.8)
        
        # Move to target network
        self.play(packet_a.animate.move_to(arch_right), run_time=1.5)

        self.wait(2)
        self.play(FadeOut(gateway_group), FadeOut(packet_a), FadeOut(title))