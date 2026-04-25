from manim import *

class Scene2(Scene):
    def construct(self):
        # Title
        title = Text("MAC Addressing & Data Filtering", font_size=32, color=BLUE).to_edge(UP)
        self.add(title)

        # Central Switch
        switch_rect = Rectangle(width=3, height=1.5, color=BLUE, fill_opacity=0.2)
        switch_text = Text("Switch", font_size=24).move_to(switch_rect.get_center())
        switch = VGroup(switch_rect, switch_text).move_to(DOWN * 0.5)

        # Computers
        c1 = VGroup(Square(side_length=0.8, color=TEAL, fill_opacity=0.5), Text("AA", font_size=20)).shift(LEFT * 4 + UP * 1.5)
        c2 = VGroup(Square(side_length=0.8, color=TEAL, fill_opacity=0.5), Text("BB", font_size=20)).shift(RIGHT * 4 + UP * 1.5)
        c3 = VGroup(Square(side_length=0.8, color=TEAL, fill_opacity=0.5), Text("CC", font_size=20)).shift(LEFT * 4 + DOWN * 2.5)
        c4 = VGroup(Square(side_length=0.8, color=TEAL, fill_opacity=0.5), Text("DD", font_size=20)).shift(RIGHT * 4 + DOWN * 2.5)

        # Connections
        l1 = Line(switch.get_left(), c1.get_right(), color=WHITE)
        l2 = Line(switch.get_right(), c2.get_left(), color=WHITE)
        l3 = Line(switch.get_left(), c3.get_right(), color=WHITE)
        l4 = Line(switch.get_right(), c4.get_left(), color=WHITE)
        connections = VGroup(l1, l2, l3, l4)

        # MAC Table
        table_bg = Rectangle(width=2.5, height=1.5, color=GOLD, fill_opacity=0.1).to_edge(RIGHT).shift(UP * 0.5)
        table_title = Text("MAC Table", font_size=18, color=GOLD).next_to(table_bg, UP, buff=0.1)
        entry1 = Text("Port 1: AA", font_size=16).move_to(table_bg.get_center() + UP * 0.3)
        entry2 = Text("Port 4: DD", font_size=16).move_to(table_bg.get_center() + DOWN * 0.3)
        mac_table = VGroup(table_bg, table_title, entry1, entry2)

        # Display Initial State
        self.play(Create(switch), Create(connections), Create(c1), Create(c2), Create(c3), Create(c4))
        self.play(Write(mac_table))
        self.wait(1)

        # Data Frame (Packet)
        packet = Circle(radius=0.15, color=YELLOW, fill_opacity=1)
        packet_label = Text("To: DD", font_size=14, color=BLACK).move_to(packet.get_center())
        data_frame = VGroup(packet, packet_label).move_to(c1.get_center())

        # Animation: Traffic Flow
        # 1. Send to Switch
        self.play(data_frame.animate.move_to(switch.get_center()), run_time=2)
        
        # 2. Switch checks table
        self.play(entry2.animate.set_color(YELLOW), run_time=0.5)
        self.play(Indicate(entry2, color=YELLOW), run_time=1)
        
        # 3. Targeted delivery to C4
        self.play(data_frame.animate.move_to(c4.get_center()), run_time=2)
        
        # 4. Highlight efficiency (No traffic on other ports)
        cross_l2 = MathTex(r"\times", color=RED).move_to(l2.get_center())
        cross_l3 = MathTex(r"\times", color=RED).move_to(l3.get_center())
        efficiency_note = Text("No Congestion", font_size=20, color=GREEN).next_to(switch, DOWN)
        
        self.play(Write(cross_l2), Write(cross_l3), Write(efficiency_note))
        self.wait(2)

        # Outro
        conclusion = Text("Targeted Forwarding", font_size=28, color=WHITE).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)