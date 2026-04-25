from manim import *

class Scene2(Scene):
    def construct(self):
        # Title and Concept
        title = Text("Bridges and Switches", color=WHITE).to_edge(UP, buff=0.3)
        concept = Text("MAC Address Filtering & Intelligent Forwarding", font_size=20, color=TEAL).next_to(title, DOWN, buff=0.1)
        
        # Switch Body
        switch_chassis = Rectangle(width=6.0, height=3.5, color=BLUE, fill_opacity=0.1)
        
        # Ports - positioned to not overlap with the main chassis
        p1 = Square(side_length=0.6, color=WHITE).next_to(switch_chassis, LEFT, buff=0)
        p2 = Square(side_length=0.6, color=WHITE).next_to(switch_chassis, RIGHT, buff=0).shift(UP * 0.8)
        p3 = Square(side_length=0.6, color=WHITE).next_to(switch_chassis, RIGHT, buff=0).shift(DOWN * 0.8)
        
        p1_lbl = Text("Port 1", font_size=14).next_to(p1, LEFT)
        p2_lbl = Text("Port 2", font_size=14).next_to(p2, RIGHT)
        p3_lbl = Text("Port 3", font_size=14).next_to(p3, RIGHT)
        
        # Internal Table (Directory)
        table_box = Rectangle(width=2.5, height=1.6, color=WHITE, fill_opacity=0.05).move_to(switch_chassis.get_center())
        table_header = Text("MAC Table", font_size=16, color=GOLD).next_to(table_box, UP, buff=0.1)
        entry_a = Text("MAC A -> Port 2", font_size=14, color=WHITE).move_to(table_box.get_center() + UP * 0.3)
        entry_b = Text("MAC B -> Port 3", font_size=14, color=WHITE).move_to(table_box.get_center() + DOWN * 0.3)
        
        mac_table_group = VGroup(table_box, table_header, entry_a, entry_b)
        
        # Opening Animations
        self.play(Write(title), Write(concept))
        self.play(Create(switch_chassis), Create(VGroup(p1, p2, p3)), Write(VGroup(p1_lbl, p2_lbl, p3_lbl)))
        self.play(Create(mac_table_group))
        self.wait(1)
        
        # Packet arrives at Port 1
        packet = Dot(color=YELLOW, radius=0.15).move_to(p1.get_center())
        p_text = Text("Data: Dest=MAC A", font_size=14, color=YELLOW).next_to(p1, UP)
        
        self.play(FadeIn(packet), Write(p_text))
        
        # Packet moves to the internal table for lookup
        self.play(
            packet.animate.move_to(table_box.get_center()),
            p_text.animate.move_to(table_box.get_top() + UP * 0.2),
            run_time=1.5
        )
        
        # Highlight Logic: Switch finds destination in table
        self.play(entry_a.animate.set_color(GREEN).scale(1.2), p2.animate.set_color(GREEN))
        self.wait(0.5)
        
        # Targeted Forwarding: Packet is sent only to the correct port
        self.play(
            packet.animate.move_to(p2.get_center()),
            p_text.animate.move_to(p2.get_top() + UP * 0.2),
            run_time=1.5
        )
        
        # Visualizing Filtering: Other port is idle
        p3_status = Text("Port 3 Ignored", font_size=14, color=RED).next_to(p3, DOWN)
        self.play(Write(p3_status), p3.animate.set_color(RED))
        
        # Final Summary
        summary = Text("Switches forward data only to the intended recipient.", font_size=20, color=YELLOW).to_edge(DOWN, buff=0.5)
        self.play(Write(summary))
        self.wait(2)