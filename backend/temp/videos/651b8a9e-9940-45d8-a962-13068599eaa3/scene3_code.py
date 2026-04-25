from manim import *

class Scene3(Scene):
    def construct(self):
        # Title
        title = Text("Inter-Network Routing & Gateways", font_size=32, color=WHITE).to_edge(UP)
        self.play(Write(title))

        # --- ROUTER SECTION ---
        lan_box = Rectangle(height=1.2, width=1.8, color=BLUE).shift(LEFT * 4 + UP * 1)
        lan_text = Text("LAN", font_size=20).next_to(lan_box, UP)
        
        wan_box = Rectangle(height=1.2, width=1.8, color=TEAL).shift(RIGHT * 4 + UP * 1)
        wan_text = Text("WAN", font_size=20).next_to(wan_box, UP)
        
        router_box = Square(side_length=1.0, color=GOLD).shift(UP * 1)
        router_text = Text("Router", font_size=18).next_to(router_box, DOWN)
        
        router_group = VGroup(lan_box, lan_text, wan_box, wan_text, router_box, router_text)
        self.play(Create(router_group))

        # Packet movement for Router
        packet_r = Dot(color=YELLOW).move_to(lan_box.get_center())
        self.play(packet_r.animate.move_to(router_box.get_center()), run_time=1)
        self.play(packet_r.animate.move_to(wan_box.get_center()), run_time=1)
        self.play(FadeOut(packet_r))

        # --- GATEWAY SECTION ---
        line_divider = Line(LEFT * 6, RIGHT * 6, color=GRAY).shift(DOWN * 0.5)
        self.play(Create(line_divider))

        gw_box = Rectangle(height=1.2, width=3.0, color=RED).shift(DOWN * 2)
        gw_label = Text("Gateway (Converter)", font_size=18).next_to(gw_box, DOWN)
        
        net_a_label = Text("Network Type A", font_size=16, color=BLUE).shift(LEFT * 4.5 + DOWN * 2)
        net_b_label = Text("Network Type B", font_size=16, color=GREEN).shift(RIGHT * 4.5 + DOWN * 2)
        
        gateway_group = VGroup(gw_box, gw_label, net_a_label, net_b_label)
        self.play(Create(gateway_group))

        # Gateway Conversion Animation
        # Packet enters as a Blue Square (Type A)
        packet_in = Square(side_length=0.3, color=BLUE, fill_opacity=0.8).move_to(LEFT * 5 + DOWN * 2)
        self.play(packet_in.animate.move_to(gw_box.get_left() + RIGHT * 0.4), run_time=1.5)
        
        # Morphing inside the gateway
        packet_out = Circle(radius=0.15, color=GREEN, fill_opacity=0.8).move_to(gw_box.get_right() - RIGHT * 0.4)
        self.play(ReplacementTransform(packet_in, packet_out))
        
        # Packet leaves as a Green Circle (Type B)
        self.play(packet_out.animate.move_to(RIGHT * 5 + DOWN * 2), run_time=1.5)

        # Final display
        self.wait(2)

        # Cleanup
        self.play(
            FadeOut(router_group),
            FadeOut(gateway_group),
            FadeOut(line_divider),
            FadeOut(packet_out),
            FadeOut(title)
        )

if __name__ == "__main__":
    pass