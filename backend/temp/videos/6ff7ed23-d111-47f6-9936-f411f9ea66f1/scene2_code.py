from manim import *

class Scene2(Scene):
    def construct(self):
        # Title and Concept
        title = Text("Intelligent Switching: Data Link Layer", font_size=32, color=WHITE)
        title.to_edge(UP)
        explanation = Text("Switches filter traffic using MAC addresses", font_size=24, color=TEAL)
        explanation.next_to(title, DOWN)

        # Main Switch Visual
        switch_box = Rectangle(width=7, height=4, color=BLUE, fill_opacity=0.1)
        switch_label = Text("Ethernet Switch", font_size=28, color=BLUE).next_to(switch_box, UP, buff=0.1)
        
        # Ports
        port_in = Rectangle(width=0.6, height=0.6, color=WHITE, fill_opacity=0.2)
        port_in.move_to(switch_box.get_left())
        port_in_label = Text("In", font_size=20).next_to(port_in, LEFT)

        port_out1 = Rectangle(width=0.6, height=0.6, color=WHITE, fill_opacity=0.2)
        port_out1.move_to(switch_box.get_right() + UP * 1.2)
        p1_label = Text("Port 1", font_size=20).next_to(port_out1, RIGHT)

        port_out2 = Rectangle(width=0.6, height=0.6, color=WHITE, fill_opacity=0.2)
        port_out2.move_to(switch_box.get_right())
        p2_label = Text("Port 2", font_size=20).next_to(port_out2, RIGHT)

        port_out3 = Rectangle(width=0.6, height=0.6, color=WHITE, fill_opacity=0.2)
        port_out3.move_to(switch_box.get_right() + DOWN * 1.2)
        p3_label = Text("Port 3", font_size=20).next_to(port_out3, RIGHT)

        ports = VGroup(port_in, port_out1, port_out2, port_out3)
        port_labels = VGroup(port_in_label, p1_label, p2_label, p3_label)

        # MAC Address Table
        table_box = Rectangle(width=3, height=1.5, color=TEAL, fill_opacity=0.2)
        table_box.move_to(switch_box.get_center() + UP * 0.8)
        table_title = Text("MAC Table", font_size=22, color=GOLD).move_to(table_box.get_top() + DOWN * 0.3)
        row1 = Text("MAC A -> Port 1", font_size=18).next_to(table_title, DOWN, buff=0.1)
        row2 = Text("MAC B -> Port 2", font_size=18).next_to(row1, DOWN, buff=0.1)
        row3 = Text("MAC C -> Port 3", font_size=18).next_to(row2, DOWN, buff=0.1)
        mac_table = VGroup(table_box, table_title, row1, row2, row3)

        # Data Frame
        frame_rect = Rectangle(width=1.4, height=0.7, color=GOLD, fill_opacity=1)
        frame_text = Text("Dest: MAC C", font_size=18, color=BLACK)
        data_frame = VGroup(frame_rect, frame_text)
        data_frame.move_to(LEFT * 6)

        # Animation Sequence
        self.play(Write(title), Write(explanation))
        self.play(Create(switch_box), Write(switch_label))
        self.play(Create(ports), Write(port_labels))
        self.play(Create(mac_table))
        self.wait(1)

        # 1. Frame arrives at Port In
        self.play(data_frame.animate.move_to(port_in.get_center()))
        self.wait(0.5)

        # 2. Frame moves to switch center for processing
        self.play(data_frame.animate.move_to(switch_box.get_center() + DOWN * 0.8))
        
        # 3. Consult Table (Highlight Port 3 row)
        self.play(row3.animate.set_color(YELLOW).scale(1.2))
        lookup_arrow = Arrow(data_frame.get_top(), row3.get_bottom(), color=YELLOW)
        self.play(Create(lookup_arrow))
        self.wait(1)
        self.play(FadeOut(lookup_arrow))

        # 4. Forwarding logic
        # Show Path to Port 3
        path_to_3 = Line(data_frame.get_center(), port_out3.get_center(), color=GREEN)
        self.play(Create(path_to_3))
        
        # Animation: Traffic reduced (Ports 1 and 2 show red crosses or remain idle)
        idle1 = Text("Idle", font_size=16, color=RED).next_to(port_out1, LEFT)
        idle2 = Text("Idle", font_size=16, color=RED).next_to(port_out2, LEFT)
        self.play(Write(idle1), Write(idle2))

        # 5. Delivery
        self.play(
            data_frame.animate.move_to(port_out3.get_center() + RIGHT * 2.5),
            FadeOut(path_to_3),
            run_time=2
        )

        # Conclusion Text
        footer = Text("Traffic is only sent to the required port.", font_size=24, color=GOLD)
        footer.to_edge(DOWN)
        self.play(Write(footer))
        self.wait(2)

        # Final cleanup for exit
        self.play(
            FadeOut(data_frame),
            FadeOut(footer),
            FadeOut(mac_table),
            FadeOut(switch_box),
            FadeOut(ports),
            FadeOut(port_labels),
            FadeOut(switch_label),
            FadeOut(idle1),
            FadeOut(idle2),
            FadeOut(title),
            FadeOut(explanation)
        )