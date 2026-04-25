from manim import *

class Scene2(Scene):
    def construct(self):
        # Title
        title = Text("Intelligent Data Filtering", color=WHITE).scale(0.8)
        title.to_edge(UP)
        
        # Central Switch
        switch_rect = Rectangle(width=3, height=1.5, color=BLUE, fill_opacity=0.4)
        switch_label = Text("Switch", color=WHITE).scale(0.6)
        switch_group = VGroup(switch_rect, switch_label).move_to(ORIGIN)

        # MAC Table (Simplified)
        table_box = Rectangle(width=2.5, height=1.5, color=GOLD, fill_opacity=0.2)
        table_box.next_to(switch_group, UP, buff=0.5)
        table_title = Text("MAC Table", color=GOLD).scale(0.4).next_to(table_box, UP, buff=0.1)
        table_content = VGroup(
            Text("Port 1: Device A", color=WHITE).scale(0.35),
            Text("Port 2: Device B", color=WHITE).scale(0.35),
            Text("Port 3: Device C", color=WHITE).scale(0.35)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(table_box.get_center())
        mac_table = VGroup(table_box, table_title, table_content)

        # Connected Devices
        dev_a = Circle(radius=0.4, color=TEAL, fill_opacity=0.8)
        label_a = Text("A", color=WHITE).scale(0.5).move_to(dev_a.get_center())
        device_a = VGroup(dev_a, label_a).to_edge(LEFT, buff=1.5)

        dev_b = Circle(radius=0.4, color=TEAL, fill_opacity=0.8)
        label_b = Text("B", color=WHITE).scale(0.5).move_to(dev_b.get_center())
        device_b = VGroup(dev_b, label_b).shift(RIGHT * 4 + UP * 1.5)

        dev_c = Circle(radius=0.4, color=TEAL, fill_opacity=0.8)
        label_c = Text("C", color=WHITE).scale(0.5).move_to(dev_c.get_center())
        device_c = VGroup(dev_c, label_c).shift(RIGHT * 4 + DOWN * 1.5)

        # Connection Lines
        line_a = Line(device_a.get_right(), switch_rect.get_left(), color=WHITE)
        line_b = Line(switch_rect.get_right(), device_b.get_left(), color=WHITE)
        line_c = Line(switch_rect.get_right(), device_c.get_left(), color=WHITE)

        # Initial Display
        self.add(title)
        self.play(
            Create(switch_group),
            Create(VGroup(device_a, device_b, device_c)),
            Create(VGroup(line_a, line_b, line_c)),
            run_time=2
        )
        self.wait(1)

        # Data Frame (The Packet)
        packet = Square(side_length=0.3, color=YELLOW, fill_opacity=1.0)
        packet_dest = Text("To: B", color=BLACK).scale(0.2).move_to(packet.get_center())
        data_frame = VGroup(packet, packet_dest).move_to(device_a.get_center())

        # Step 1: Data moves from Device A to Switch
        self.play(data_frame.animate.move_to(switch_group.get_center()), run_time=2)
        
        # Step 2: Switch looks up MAC table
        self.play(FadeIn(mac_table), run_time=1)
        self.play(table_content[1].animate.set_color(YELLOW).scale(1.2), run_time=1)
        self.wait(1)

        # Step 3: Highlight specific path and bypass others
        self.play(
            line_b.animate.set_color(GREEN).set_stroke(width=6),
            line_c.animate.set_stroke(opacity=0.2),
            run_time=1
        )

        # Step 4: Forward only to Device B
        self.play(data_frame.animate.move_to(device_b.get_center()), run_time=2)
        
        # Final emphasis
        success_text = Text("Targeted Forwarding", color=GREEN).scale(0.6).next_to(device_b, RIGHT)
        self.play(Write(success_text), run_time=1)
        self.wait(2)