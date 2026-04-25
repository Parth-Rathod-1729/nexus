from manim import *

class Scene3(Scene):
    def construct(self):
        # Title and Concept Text
        title = Text("Global Connectivity: Routers and Gateways", color=WHITE).scale(0.7)
        title.to_edge(UP)
        
        concept = Text("Network Layer and Protocol Conversion", color=YELLOW).scale(0.5)
        concept.next_to(title, DOWN)
        
        self.play(Write(title), Write(concept))
        self.wait(1)

        # --- Router Section ---
        router_group = VGroup()
        router_body = Circle(radius=0.6, color=GOLD, fill_opacity=0.5)
        router_text = Text("Router", color=WHITE).scale(0.4).move_to(router_body.get_center())
        router_group.add(router_body, router_text)
        router_group.move_to(ORIGIN)

        lan_a = Square(side_length=1.5, color=BLUE, fill_opacity=0.2)
        lan_a.to_edge(LEFT, buff=1.5)
        label_a = Text("LAN A", color=BLUE).scale(0.4).next_to(lan_a, UP)

        lan_b = Square(side_length=1.5, color=GREEN, fill_opacity=0.2)
        lan_b.to_edge(RIGHT, buff=1.5)
        label_b = Text("LAN B", color=GREEN).scale(0.4).next_to(lan_b, UP)

        arrow_a_to_r = Arrow(lan_a.get_right(), router_body.get_left(), color=WHITE, buff=0.1)
        arrow_r_to_b = Arrow(router_body.get_right(), lan_b.get_left(), color=WHITE, buff=0.1)
        
        path_label = Text("IP Routing", color=GOLD).scale(0.4).next_to(router_group, DOWN)

        router_elements = VGroup(router_group, lan_a, label_a, lan_b, label_b, arrow_a_to_r, arrow_r_to_b, path_label)
        
        self.play(Create(lan_a), Create(lan_b), Write(label_a), Write(label_b))
        self.play(Create(router_group), Write(path_label))
        self.play(Create(arrow_a_to_r), Create(arrow_r_to_b))

        # Packet movement for Router
        packet = Dot(color=WHITE).move_to(lan_a.get_center())
        self.play(packet.animate.move_to(router_body.get_center()), run_time=1)
        self.play(packet.animate.move_to(lan_b.get_center()), run_time=1)
        self.play(FadeOut(packet))
        self.wait(1)
        
        self.play(FadeOut(router_elements))

        # --- Gateway Section ---
        gateway_rect = Rectangle(width=1.2, height=2.0, color=RED, fill_opacity=0.5)
        gateway_rect.move_to(ORIGIN)
        gateway_text = Text("Gateway", color=WHITE).scale(0.5).rotate(90*DEGREES).move_to(gateway_rect.get_center())
        gateway_group = VGroup(gateway_rect, gateway_text)

        net_email = Rectangle(width=2, height=1.5, color=TEAL, fill_opacity=0.3)
        net_email.to_edge(LEFT, buff=1.0)
        email_label = Text("Email Server\n(SMTP)", color=TEAL).scale(0.4).next_to(net_email, UP)

        net_legacy = Rectangle(width=2, height=1.5, color=YELLOW, fill_opacity=0.3)
        net_legacy.to_edge(RIGHT, buff=1.0)
        legacy_label = Text("Mainframe\n(SNA/Proprietary)", color=YELLOW).scale(0.4).next_to(net_legacy, UP)

        conv_label = Text("Protocol Translation", color=RED).scale(0.5).to_edge(DOWN, buff=1)

        gateway_scene_elements = VGroup(gateway_group, net_email, email_label, net_legacy, legacy_label, conv_label)
        
        self.play(Create(net_email), Write(email_label))
        self.play(Create(gateway_group), Write(conv_label))
        self.play(Create(net_legacy), Write(legacy_label))

        # Data translation animation
        data_packet = Dot(color=TEAL, radius=0.15).move_to(net_email.get_center())
        self.play(data_packet.animate.move_to(gateway_rect.get_center()), run_time=1.5)
        
        # Change color to show conversion
        self.play(data_packet.animate.set_color(YELLOW), run_time=0.2)
        
        self.play(data_packet.animate.move_to(net_legacy.get_center()), run_time=1.5)
        self.play(FadeOut(data_packet))

        # Explanation display
        explanation = Text(
            "Routers connect networks; Gateways translate between them.", 
            color=WHITE
        ).scale(0.4).to_edge(DOWN)
        
        self.play(Write(explanation))
        self.wait(2)

        # Cleanup
        self.play(
            FadeOut(title),
            FadeOut(concept),
            FadeOut(gateway_scene_elements),
            FadeOut(explanation)
        )
        self.wait(1)