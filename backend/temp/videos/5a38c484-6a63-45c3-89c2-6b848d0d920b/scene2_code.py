from manim import *

class Scene2(Scene):
    def construct(self):
        # Title
        title = Text("Intelligent Switching & Filtering", color=WHITE, font_size=36).to_edge(UP)
        
        # Switch Body
        switch_rect = Rectangle(width=7, height=2.5, color=BLUE, fill_opacity=0.1)
        
        # Ports
        p1 = Square(side_length=0.7, color=WHITE).move_to(switch_rect.get_left() + RIGHT * 1)
        p2 = Square(side_length=0.7, color=WHITE).move_to(switch_rect.get_left() + RIGHT * 2.5)
        p3 = Square(side_length=0.7, color=WHITE).move_to(switch_rect.get_right() - RIGHT * 2.5)
        p4 = Square(side_length=0.7, color=WHITE).move_to(switch_rect.get_right() - RIGHT * 1)
        
        l1 = Text("Port 1", font_size=18).next_to(p1, DOWN)
        l2 = Text("Port 2", font_size=18).next_to(p2, DOWN)
        l3 = Text("Port 3", font_size=18).next_to(p3, DOWN)
        l4 = Text("Port 4", font_size=18).next_to(p4, DOWN)
        
        ports = VGroup(p1, p2, p3, p4, l1, l2, l3, l4)
        switch_ui = VGroup(switch_rect, ports)
        
        # MAC Table (Switching Directory)
        table_box = Rectangle(width=3.5, height=1.5, color=GOLD, fill_opacity=0.1).to_edge(UP, buff=1.2)
        table_title = Text("MAC Address Table", font_size=20, color=GOLD).next_to(table_box, UP, buff=0.1)
        table_content = Text("Device B -> Port 4", color=WHITE, font_size=20).move_to(table_box.get_center())
        mac_table = VGroup(table_box, table_title, table_content)
        
        # Initial Animation: Create Switch and Table
        self.play(Write(title))
        self.play(Create(switch_ui))
        self.play(FadeIn(mac_table))
        self.wait(1)

        # Data Frame (Packet)
        packet = Square(side_length=0.4, fill_color=YELLOW, fill_opacity=1, color=YELLOW)
        packet_label = Text("DATA", font_size=14, color=BLACK).move_to(packet.get_center())
        data_frame = VGroup(packet, packet_label)
        data_frame.move_to(p1.get_center() + LEFT * 2)

        # Animation: Data enters Port 1
        self.play(data_frame.animate.move_to(p1.get_center()), run_time=1.5)
        
        # Animation: Table Lookup (Highlighting)
        highlight = Rectangle(width=3.7, height=1.7, color=YELLOW, stroke_width=4).move_to(table_box.get_center())
        self.play(Create(highlight), run_time=0.5)
        self.play(table_content.animate.set_color(YELLOW), run_time=0.5)
        self.play(FadeOut(highlight), table_content.animate.set_color(WHITE))

        # Animation: Intelligent Routing to Port 4 only
        path_to_center = data_frame.animate.move_to(switch_rect.get_center())
        self.play(path_to_center, run_time=1)
        
        # Visual cue for filtering: Other ports stay dim/empty
        cross2 = Line(p2.get_corner(UL), p2.get_corner(DR), color=RED).scale(0.5)
        cross3 = Line(p3.get_corner(UL), p3.get_corner(DR), color=RED).scale(0.5)
        filtering_icons = VGroup(cross2, cross3)
        
        self.play(
            data_frame.animate.move_to(p4.get_center()),
            FadeIn(filtering_icons),
            run_time=1.5
        )
        
        # Animation: Exit through Port 4
        self.play(
            data_frame.animate.move_to(p4.get_center() + RIGHT * 2),
            FadeOut(filtering_icons),
            run_time=1.2
        )
        
        # Summary Text
        summary = Text("Collisions avoided via targeted forwarding", font_size=24, color=GREEN).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)

        # Clear Scene
        self.play(FadeOut(switch_ui), FadeOut(mac_table), FadeOut(data_frame), FadeOut(title), FadeOut(summary))