from manim import *

class Scene2(Scene):
    def construct(self):
        # Create Hub (Central Device)
        hub_box = Rectangle(height=1.5, width=2.5, color=BLUE, fill_opacity=0.3)
        hub_label = Text("HUB", font_size=24, color=WHITE).move_to(hub_box.get_center())
        hub = VGroup(hub_box, hub_label)

        # Create Computers (Devices)
        comp_a = Square(side_length=0.8, color=TEAL, fill_opacity=0.5).shift(LEFT * 4)
        label_a = Text("Comp A", font_size=18).next_to(comp_a, DOWN)
        
        comp_b = Square(side_length=0.8, color=TEAL, fill_opacity=0.5).shift(RIGHT * 4 + UP * 2)
        label_b = Text("Comp B", font_size=18).next_to(comp_b, DOWN)
        
        comp_c = Square(side_length=0.8, color=TEAL, fill_opacity=0.5).shift(RIGHT * 4)
        label_c = Text("Comp C", font_size=18).next_to(comp_c, DOWN)
        
        comp_d = Square(side_length=0.8, color=TEAL, fill_opacity=0.5).shift(RIGHT * 4 + DOWN * 2)
        label_d = Text("Comp D", font_size=18).next_to(comp_d, DOWN)

        computers = VGroup(comp_a, comp_b, comp_c, comp_d, label_a, label_b, label_c, label_d)

        # Create Network Connections
        line_a = Line(comp_a.get_right(), hub_box.get_left(), color=WHITE)
        line_b = Line(hub_box.get_right(), comp_b.get_left(), color=WHITE)
        line_c = Line(hub_box.get_right(), comp_c.get_left(), color=WHITE)
        line_d = Line(hub_box.get_right(), comp_d.get_left(), color=WHITE)
        lines = VGroup(line_a, line_b, line_c, line_d)

        # Labels for Filtering
        filter_text = Text("No Filtering", color=RED, font_size=32).next_to(hub_box, UP * 1.5)

        # Add initial objects
        self.add(hub, computers, lines)
        self.wait(1)

        # 1. Packet from Computer A to Hub
        packet_a = Dot(color=YELLOW, radius=0.15).move_to(comp_a.get_center())
        self.play(packet_a.animate.move_to(hub_box.get_center()), run_time=1.5)
        
        # 2. Duplicate packet and label "No Filtering"
        self.play(Write(filter_text))
        
        packet_copy1 = Dot(color=YELLOW, radius=0.15).move_to(hub_box.get_center())
        packet_copy2 = Dot(color=YELLOW, radius=0.15).move_to(hub_box.get_center())
        packet_copy3 = Dot(color=YELLOW, radius=0.15).move_to(hub_box.get_center())
        
        self.remove(packet_a) # Remove the original to use copies for broadcast

        # 3. Broadcast to all other ports
        self.play(
            packet_copy1.animate.move_to(comp_b.get_center()),
            packet_copy2.animate.move_to(comp_c.get_center()),
            packet_copy3.animate.move_to(comp_d.get_center()),
            run_time=2
        )

        # 4. Final state hold
        self.wait(2)

        # Clean up for scene timing
        self.play(
            FadeOut(packet_copy1), 
            FadeOut(packet_copy2), 
            FadeOut(packet_copy3), 
            FadeOut(filter_text)
        )
        self.wait(1)

        # Explanation Text (Concise)
        explanation = Text("Data is sent to all ports automatically.", font_size=24, color=GOLD).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)