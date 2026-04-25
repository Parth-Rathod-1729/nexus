from manim import *

class Scene2(Scene):
    def construct(self):
        # 1. Setup Switch and Table
        title = Text("Intelligent Switching: Bridges and Switches", font_size=32, color=WHITE).to_edge(UP)
        switch_box = Rectangle(width=6, height=3.5, color=BLUE, fill_opacity=0.1)
        
        # MAC Table UI
        table_outline = Rectangle(width=2.5, height=1.5, color=GOLD).move_to(switch_box.get_center())
        table_header = Text("MAC Table", font_size=20, color=GOLD).next_to(table_outline, UP, buff=0.1)
        table_entry = Text("Dest: Port B", font_size=18, color=WHITE).move_to(table_outline.get_center())
        mac_table = VGroup(table_outline, table_header, table_entry)
        
        # Ports and Hosts
        port_a = Dot(LEFT * 4.5, color=WHITE)
        port_b = Dot(RIGHT * 4.5, color=WHITE)
        port_c = Dot(DOWN * 3, color=WHITE)
        
        label_a = Text("Port A", font_size=20).next_to(port_a, UP)
        label_b = Text("Port B", font_size=20).next_to(port_b, UP)
        label_c = Text("Port C", font_size=20).next_to(port_c, RIGHT)
        
        line_a = Line(port_a.get_center(), LEFT * 3, color=WHITE)
        line_b = Line(port_b.get_center(), RIGHT * 3, color=WHITE)
        line_c = Line(port_c.get_center(), DOWN * 1.75, color=WHITE)
        
        ports_group = VGroup(port_a, port_b, port_c, label_a, label_b, label_c, line_a, line_b, line_c)
        
        # Data Frame
        frame = Square(side_length=0.4, color=RED, fill_opacity=1)
        frame_text = Text("Data", font_size=14, color=WHITE).move_to(frame.get_center())
        data_frame = VGroup(frame, frame_text).move_to(port_a.get_center())

        # 2. Animations
        self.play(Write(title))
        self.play(Create(switch_box), Create(ports_group))
        self.play(Create(mac_table))
        self.wait(1)
        
        # Data enters the switch
        self.play(data_frame.animate.move_to(LEFT * 1.5))
        
        # Logic: Highlighting the lookup process
        self.play(
            table_outline.animate.set_fill(YELLOW, fill_opacity=0.3),
            table_entry.animate.set_color(YELLOW),
            run_time=1
        )
        
        # Create a dedicated path arrow to show filtering
        path_arrow = Arrow(LEFT * 1, RIGHT * 4, color=GREEN, buff=0)
        
        # Forward to specific port
        self.play(Create(path_arrow))
        self.play(data_frame.animate.move_to(port_b.get_center()))
        
        # Emphasize idle port
        idle_cross = VGroup(
            Line(DOWN * 2, DOWN * 2.5, color=RED),
            Line(DOWN * 2.25 + LEFT * 0.2, DOWN * 2.25 + RIGHT * 0.2, color=RED)
        ).move_to(line_c.get_center())
        
        self.play(Create(idle_cross))
        
        # Final Summary text
        summary = Text("Filtering reduces traffic congestion", font_size=24, color=TEAL).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)