from manim import *

class Scene2(Scene):
    def construct(self):
        # Title and basic setup
        title = Text("Intelligent Forwarding (Switch)", font_size=32, color=WHITE).to_edge(UP)
        self.add(title)

        # Switch Visual (Central Hub)
        switch_body = Rectangle(width=3, height=2, color=TEAL, fill_opacity=0.3)
        switch_text = Text("Switch", font_size=24).move_to(switch_body.get_center())
        
        # Ports on the switch
        p1 = Square(side_length=0.3, color=WHITE).move_to(switch_body.get_left())
        p2 = Square(side_length=0.3, color=WHITE).move_to(switch_body.get_right()).shift(UP * 0.4)
        p3 = Square(side_length=0.3, color=WHITE).move_to(switch_body.get_right()).shift(DOWN * 0.4)
        switch_group = VGroup(switch_body, switch_text, p1, p2, p3)

        # Devices
        dev_a = Circle(radius=0.4, color=BLUE, fill_opacity=0.6).move_to([-5, 2, 0])
        label_a = Text("Host A", font_size=20).next_to(dev_a, UP)
        
        dev_b = Circle(radius=0.4, color=GREEN, fill_opacity=0.6).move_to([5, 1, 0])
        label_b = Text("Host B", font_size=20).next_to(dev_b, RIGHT)
        
        dev_c = Circle(radius=0.4, color=RED, fill_opacity=0.6).move_to([5, -2, 0])
        label_c = Text("Host C", font_size=20).next_to(dev_c, RIGHT)

        # Lines connecting devices to switch ports
        line_a = Line(dev_a.get_center(), p1.get_center(), color=WHITE)
        line_b = Line(p2.get_center(), dev_b.get_center(), color=WHITE)
        line_c = Line(p3.get_center(), dev_c.get_center(), color=WHITE)

        # MAC Address Table
        table_box = Rectangle(width=3.5, height=2.2, color=GOLD).to_edge(DOWN).shift(LEFT * 3)
        table_header = Text("MAC Address Table", font_size=20, color=GOLD).next_to(table_box, UP, buff=0.1)
        row1 = Text("MAC A : Port 1", font_size=18).move_to(table_box.get_center() + UP * 0.5)
        row2 = Text("MAC B : Port 2", font_size=18).move_to(table_box.get_center())
        row3 = Text("MAC C : Port 3", font_size=18).move_to(table_box.get_center() + DOWN * 0.5)
        mac_table = VGroup(table_box, table_header, row1, row2, row3)

        # Display Initial State
        self.play(Create(switch_group), Create(VGroup(dev_a, label_a, dev_b, label_b, dev_c, label_c)))
        self.play(Create(VGroup(line_a, line_b, line_c)))
        self.play(Create(mac_table))
        self.wait(1)

        # Packet Creation
        packet = Dot(color=YELLOW, radius=0.15)
        packet_label = Text("To: B", font_size=14).next_to(packet, UP, buff=0.05)
        packet_group = VGroup(packet, packet_label).move_to(dev_a.get_center())

        # Step 1: Data arrives at Switch
        self.play(packet_group.animate.move_to(p1.get_center()), run_time=1.5)
        self.play(packet_group.animate.move_to(switch_body.get_center()), run_time=0.5)

        # Step 2: Switch checks the MAC Table
        highlight = Rectangle(width=3.3, height=0.35, color=YELLOW, fill_opacity=0.2).move_to(row2.get_center())
        self.play(Create(highlight))
        self.wait(1)

        # Step 3: Forwarding to specific port only
        explanation = Text("Forwarding to Port 2 only", font_size=22, color=GREEN).to_edge(DOWN).shift(RIGHT * 3)
        self.play(Write(explanation))
        
        self.play(
            packet_group.animate.move_to(dev_b.get_center()),
            FadeOut(highlight),
            run_time=2
        )

        # Step 4: Show other ports remained clear
        idle_mark = Text("Port 3 Idle", font_size=20, color=RED).next_to(line_c, UP, buff=-0.5)
        self.play(Write(idle_mark))
        self.wait(2)

        # Outro cleanup
        self.play(FadeOut(packet_group), FadeOut(explanation), FadeOut(idle_mark))
        self.wait(1)