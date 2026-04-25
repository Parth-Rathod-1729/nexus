from manim import *

class Scene2(Scene):
    def construct(self):
        # 1. Create the Switch and Devices
        switch_rect = Rectangle(width=3, height=1.5, color=BLUE, fill_opacity=0.2)
        switch_label = Text("Intelligent Switch", font_size=24).move_to(switch_rect.get_center())
        switch_group = VGroup(switch_rect, switch_label)

        node_a = VGroup(Square(side_length=0.8, color=WHITE), Text("Node A", font_size=18).shift(DOWN * 0.6))
        node_b = VGroup(Square(side_length=0.8, color=GREEN), Text("Node B", font_size=18).shift(DOWN * 0.6))
        node_c = VGroup(Square(side_length=0.8, color=WHITE), Text("Node C", font_size=18).shift(DOWN * 0.6))

        node_a.move_to(LEFT * 5)
        node_b.move_to(RIGHT * 4 + UP * 1.5)
        node_c.move_to(RIGHT * 4 + DOWN * 1.5)

        # 2. Create Connections
        line_a = Line(node_a.get_right(), switch_rect.get_left(), color=WHITE)
        line_b = Line(switch_rect.get_right(), node_b.get_left(), color=WHITE)
        line_c = Line(switch_rect.get_right(), node_c.get_left(), color=WHITE)
        connections = VGroup(line_a, line_b, line_c)

        # 3. Create the MAC Table overlay
        table_box = Rectangle(width=3.5, height=1.2, color=GOLD, fill_opacity=0.1).to_edge(UP)
        table_title = Text("MAC Address Table", font_size=20, color=GOLD).next_to(table_box.get_top(), DOWN, buff=0.1)
        table_entry = Text("Port 2: Node B (MAC_B)", font_size=18).next_to(table_title, DOWN, buff=0.2)
        mac_table = VGroup(table_box, table_title, table_entry)

        # 4. Display Components
        self.play(Create(switch_group), Create(node_a), Create(node_b), Create(node_c))
        self.play(Create(connections))
        self.wait(1)

        # 5. Data Frame Movement: Node A to Switch
        data_packet = Dot(color=YELLOW, radius=0.15)
        data_packet.move_to(node_a.get_center())
        
        label_frame = Text("Frame for B", font_size=16, color=YELLOW).next_to(data_packet, UP)
        
        self.play(data_packet.animate.move_to(switch_rect.get_center()), 
                  label_frame.animate.move_to(switch_rect.get_top() + UP * 0.3))
        
        # 6. Show MAC Table lookup
        self.play(Create(mac_table))
        self.play(table_entry.animate.set_color(YELLOW))
        self.wait(1)

        # 7. Forwarding: Switch to Node B only
        target_arrow = Arrow(switch_rect.get_right(), node_b.get_left(), color=YELLOW, buff=0.1)
        
        self.play(FadeIn(target_arrow))
        self.play(
            data_packet.animate.move_to(node_b.get_center()),
            label_frame.animate.move_to(node_b.get_top() + UP * 0.3),
            run_time=2
        )
        
        # 8. Contrast: Port C remains idle
        idle_text = Text("Idle / No Traffic", font_size=16, color=RED).next_to(node_c, RIGHT)
        self.play(Write(idle_text))
        self.wait(1.5)

        # 9. Conclusion
        summary = Text("Switches reduce traffic via MAC filtering.", font_size=24, color=TEAL).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)