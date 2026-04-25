from manim import *

class Scene2(Scene):
    def construct(self):
        # Title
        title = Text("Intelligent Filtering: Switch", font_size=36, color=WHITE).to_edge(UP)
        self.add(title)

        # Components
        switch_box = Rectangle(width=2.5, height=1.5, color=TEAL, fill_opacity=0.3)
        switch_label = Text("Switch", font_size=24).move_to(switch_box.get_center())
        switch = VGroup(switch_box, switch_label).move_to(ORIGIN)

        pc_a = VGroup(Square(side_length=0.8, color=BLUE, fill_opacity=0.2), Text("PC A", font_size=20)).next_to(switch, LEFT, buff=2.5)
        pc_b = VGroup(Square(side_length=0.8, color=BLUE, fill_opacity=0.2), Text("PC B", font_size=20)).next_to(switch, RIGHT, buff=2.5).shift(UP * 1.5)
        pc_c = VGroup(Square(side_length=0.8, color=BLUE, fill_opacity=0.2), Text("PC C", font_size=20)).next_to(switch, RIGHT, buff=2.5).shift(DOWN * 1.5)

        line_a = Line(pc_a.get_right(), switch.get_left(), color=GRAY)
        line_b = Line(switch.get_right(), pc_b.get_left(), color=GRAY)
        line_c = Line(switch.get_right(), pc_c.get_left(), color=GRAY)

        # MAC Table
        table_bg = Rectangle(width=3, height=2, color=GOLD, fill_opacity=0.1).to_corner(DL, buff=0.5)
        table_title = Text("MAC Table", font_size=20, color=GOLD).next_to(table_bg, UP, buff=0.1)
        row1 = Text("PC A: Port 1", font_size=18).move_to(table_bg.get_center() + UP * 0.4)
        row2 = Text("PC C: Port 3", font_size=18).move_to(table_bg.get_center() + DOWN * 0.4)
        mac_table = VGroup(table_bg, table_title, row1, row2)

        # Animations
        self.play(Create(switch), Create(pc_a), Create(pc_b), Create(pc_c))
        self.play(Create(line_a), Create(line_b), Create(line_c))
        self.play(Create(mac_table))
        self.wait(1)

        # Packet Flow
        packet = Rectangle(width=0.4, height=0.2, color=YELLOW, fill_opacity=1).move_to(pc_a.get_center())
        dest_text = Text("To: PC C", font_size=14, color=BLACK).move_to(packet.get_center())
        full_packet = VGroup(packet, dest_text)

        # 1. PC A to Switch
        self.play(full_packet.animate.move_to(switch.get_center()), run_time=1.5)
        
        # 2. Filtering highlight
        self.play(row2.animate.set_color(YELLOW), switch_box.animate.set_color(YELLOW))
        self.wait(1)
        self.play(row2.animate.set_color(WHITE), switch_box.animate.set_color(TEAL))

        # 3. Switch to PC C only
        self.play(
            full_packet.animate.move_to(pc_c.get_center()),
            line_c.animate.set_stroke(YELLOW, width=4),
            run_time=1.5
        )
        self.play(line_c.animate.set_stroke(GRAY, width=2))

        # Final explanation text
        explanation = Text("Directed Traffic = No Congestion", font_size=24, color=GREEN).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)

        # Cleanup
        self.play(FadeOut(full_packet), FadeOut(explanation), FadeOut(mac_table))