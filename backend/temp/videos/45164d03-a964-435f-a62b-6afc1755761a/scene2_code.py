from manim import *

class Scene2(Scene):
    def construct(self):
        # Title and Labels
        title = Text("Intelligent Data Filtering", color=WHITE).scale(0.8).to_edge(UP)
        layer_info = Text("Data Link Layer: Switches", color=TEAL).scale(0.5).next_to(title, DOWN)
        self.add(title, layer_info)

        # Central Switch
        switch_rect = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.2)
        switch_label = Text("Switch", color=BLUE).scale(0.6).move_to(switch_rect.get_center())
        switch_group = VGroup(switch_rect, switch_label)
        self.play(Create(switch_group))

        # Ports and Devices
        p1 = Circle(radius=0.2, color=WHITE).move_to([-4, 0, 0])
        p2 = Circle(radius=0.2, color=WHITE).move_to([4, 0, 0])
        p3 = Circle(radius=0.2, color=WHITE).move_to([0, 2, 0])
        
        l1 = Line(p1.get_right(), switch_rect.get_left())
        l2 = Line(p2.get_left(), switch_rect.get_right())
        l3 = Line(p3.get_bottom(), switch_rect.get_top())
        
        nodes = VGroup(p1, p2, p3, l1, l2, l3)
        node_labels = VGroup(
            Text("Port 1", color=YELLOW).scale(0.4).next_to(p1, LEFT),
            Text("Port 2", color=YELLOW).scale(0.4).next_to(p2, RIGHT),
            Text("Port 3", color=YELLOW).scale(0.4).next_to(p3, UP)
        )
        self.play(Create(nodes), Write(node_labels))

        # Data Frame
        frame = Rectangle(width=0.6, height=0.3, color=GOLD, fill_opacity=1)
        frame_text = Text("Data", color=BLACK).scale(0.3).move_to(frame.get_center())
        data_packet = VGroup(frame, frame_text).move_to(p1.get_center())

        # MAC Table Visualization
        table_box = Rectangle(width=2.5, height=1.5, color=GREY, fill_opacity=0.8).to_edge(DR, buff=0.5)
        table_header = Text("MAC Table", color=WHITE).scale(0.4).move_to(table_box.get_top() + DOWN * 0.3)
        entry1 = Text("P1: MAC_A", color=GREEN).scale(0.3).next_to(table_header, DOWN, buff=0.2)
        entry2 = Text("P2: MAC_B", color=GREEN).scale(0.3).next_to(entry1, DOWN, buff=0.1)
        mac_table = VGroup(table_box, table_header, entry1, entry2)

        # Animation Sequence
        # 1. Packet arrives at switch
        self.play(data_packet.animate.move_to(switch_rect.get_center()), run_time=1.5)
        
        # 2. Lookup logic
        self.play(FadeIn(mac_table))
        highlight = Square(side_length=0.4, color=RED).move_to(entry2.get_center())
        self.play(Create(highlight))
        self.wait(1)
        
        # 3. Targeted Forwarding
        self.play(FadeOut(highlight))
        self.play(data_packet.animate.move_to(p2.get_center()), run_time=1.5)
        
        # Efficiency Label
        efficiency_text = Text("Direct Path: No Collisions", color=GREEN).scale(0.5).next_to(switch_rect, DOWN, buff=0.5)
        self.play(Write(efficiency_text))
        self.wait(2)

        # Cleanup
        self.play(
            FadeOut(nodes),
            FadeOut(node_labels),
            FadeOut(switch_group),
            FadeOut(mac_table),
            FadeOut(data_packet),
            FadeOut(efficiency_text),
            FadeOut(title),
            FadeOut(layer_info)
        )
        self.wait(1)