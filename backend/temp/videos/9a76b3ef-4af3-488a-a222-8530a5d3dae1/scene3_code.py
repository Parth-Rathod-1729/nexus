from manim import *

class Scene3(Scene):
    def construct(self):
        # Title and Concept
        title = Text("Gateways & Diagnostics", font_size=32, color=WHITE).to_edge(UP, buff=0.2)
        explanation = Text("Converting Protocols & Testing Paths", font_size=20, color=GOLD).next_to(title, DOWN, buff=0.1)
        
        # Network A (Left)
        cloud_a = Circle(radius=1.2, color=BLUE, fill_opacity=0.1).shift(LEFT * 4 + UP * 1)
        label_a = Text("Network A\n(HTTP)", font_size=18, color=BLUE).next_to(cloud_a, UP)
        
        # Gateway (Center)
        gateway = Rectangle(height=1.8, width=1.4, color=GOLD, fill_opacity=0.3).shift(UP * 1)
        gateway_label = Text("Gateway", font_size=22, color=GOLD).move_to(gateway.get_center())
        
        # Network B (Right)
        cloud_b = Circle(radius=1.2, color=GREEN, fill_opacity=0.1).shift(RIGHT * 4 + UP * 1)
        label_b = Text("Network B\n(Proprietary)", font_size=18, color=GREEN).next_to(cloud_b, UP)
        
        # Connection Lines
        line1 = Line(cloud_a.get_right(), gateway.get_left(), color=WHITE)
        line2 = Line(gateway.get_right(), cloud_b.get_left(), color=WHITE)
        
        # Packet Representation
        packet_wrapper = Square(side_length=0.4, color=BLUE, fill_opacity=0.8).move_to(cloud_a.get_center())
        packet_data = Dot(color=WHITE).move_to(packet_wrapper.get_center())
        packet = VGroup(packet_wrapper, packet_data)
        
        # Command Prompt / Diagnostic Window
        terminal_bg = Rectangle(height=2.8, width=10, color=WHITE, fill_opacity=0.1).to_edge(DOWN, buff=0.3)
        terminal_header = Rectangle(height=0.4, width=10, color=WHITE, fill_opacity=0.3).move_to(terminal_bg.get_top() + DOWN * 0.2)
        terminal_title = Text("Diagnostic Console", font_size=16, color=WHITE).move_to(terminal_header.get_center())
        terminal_vgroup = VGroup(terminal_bg, terminal_header, terminal_title)
        
        ping_text = Text("> ping 10.0.0.5", font_size=18, color=TEAL).next_to(terminal_header, DOWN, buff=0.3).to_edge(LEFT, buff=1.5)
        ping_res = Text("Reply from 10.0.0.5: bytes=32 time=12ms TTL=54", font_size=16, color=WHITE).next_to(ping_text, DOWN, buff=0.1).align_to(ping_text, LEFT)
        
        trace_text = Text("> tracert 10.0.0.5", font_size=18, color=TEAL).next_to(ping_res, DOWN, buff=0.2).align_to(ping_text, LEFT)
        hop1 = Text("1  <1 ms  192.168.1.1 (Gateway)", font_size=16, color=YELLOW).next_to(trace_text, DOWN, buff=0.1).align_to(ping_text, LEFT).shift(RIGHT * 0.4)
        hop2 = Text("2  12 ms  10.0.0.5 (Destination)", font_size=16, color=GREEN).next_to(hop1, DOWN, buff=0.1).align_to(hop1, LEFT)
        
        # Display Initial Elements
        self.add(title, explanation)
        self.play(
            Create(cloud_a),
            Create(cloud_b),
            Create(gateway),
            Write(label_a),
            Write(label_b),
            Write(gateway_label)
        )
        self.play(Create(line1), Create(line2))
        
        # Animation: Packet movement and protocol conversion
        self.play(FadeIn(packet))
        
        # Move to Gateway
        self.play(packet.animate.move_to(gateway.get_center()), run_time=1.5)
        
        # Visual Conversion (Change wrapper color and shape)
        new_wrapper = Circle(radius=0.25, color=GREEN, fill_opacity=0.8).move_to(gateway.get_center())
        self.play(Transform(packet_wrapper, new_wrapper), run_time=0.8)
        
        # Move to Network B
        self.play(packet.animate.move_to(cloud_b.get_center()), run_time=1.5)
        self.wait(0.5)
        
        # Diagnostic Phase
        self.play(Create(terminal_vgroup))
        
        # Show Ping
        self.play(Write(ping_text))
        self.play(Write(ping_res))
        self.wait(0.5)
        
        # Show Traceroute
        self.play(Write(trace_text))
        
        # Highlight Gateway during Hop 1
        indicator = Circle(radius=1, color=YELLOW).move_to(gateway.get_center())
        self.play(Create(indicator), Write(hop1))
        self.play(FadeOut(indicator))
        
        # Highlight Destination during Hop 2
        indicator2 = Circle(radius=1, color=GREEN).move_to(cloud_b.get_center())
        self.play(Create(indicator2), Write(hop2))
        self.play(FadeOut(indicator2))
        
        self.wait(2)

if __name__ == "__main__":
    scene = Scene3()
    scene.render()