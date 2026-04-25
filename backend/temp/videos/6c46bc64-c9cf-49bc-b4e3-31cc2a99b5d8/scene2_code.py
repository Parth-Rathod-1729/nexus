from manim import *

class Scene2(Scene):
    def construct(self):
        # Title
        title = Text("Bridges and Switches", color=WHITE).to_edge(UP, buff=0.3)
        
        # Switch Component
        switch_box = Rectangle(width=3.5, height=2.0, color=BLUE, fill_opacity=0.2).move_to(UP * 0.5)
        switch_label = Text("Switch (Multi-port Bridge)", font_size=20).next_to(switch_box, UP, buff=0.1)
        buffer_label = Text("Buffer & Directory", font_size=16, color=TEAL).move_to(switch_box.get_center() + DOWN * 0.5)
        
        # Devices (Computers)
        pc_a = Square(side_length=0.8, color=WHITE, fill_opacity=0.3).move_to(LEFT * 4 + DOWN * 2.5)
        pc_b = Square(side_length=0.8, color=WHITE, fill_opacity=0.3).move_to(DOWN * 2.5)
        pc_c = Square(side_length=0.8, color=WHITE, fill_opacity=0.3).move_to(RIGHT * 4 + DOWN * 2.5)
        
        label_a = Text("MAC: A", font_size=18).next_to(pc_a, DOWN)
        label_b = Text("MAC: B", font_size=18).next_to(pc_b, DOWN)
        label_c = Text("MAC: C", font_size=18).next_to(pc_c, DOWN)
        
        # Connections
        link_a = Line(switch_box.get_bottom(), pc_a.get_top(), color=WHITE)
        link_b = Line(switch_box.get_bottom(), pc_b.get_top(), color=WHITE)
        link_c = Line(switch_box.get_bottom(), pc_c.get_top(), color=WHITE)
        
        # Directory (MAC Table)
        table_rect = Rectangle(width=2.2, height=1.6, color=GOLD).to_edge(RIGHT, buff=0.5).shift(UP * 0.5)
        table_head = Text("Directory", font_size=18, color=GOLD).next_to(table_rect, UP, buff=0.1)
        entry_a = Text("A -> Port 1", font_size=16).move_to(table_rect.get_center() + UP * 0.4)
        entry_b = Text("B -> Port 2", font_size=16).move_to(table_rect.get_center())
        entry_c = Text("C -> Port 3", font_size=16).move_to(table_rect.get_center() + DOWN * 0.4)
        
        directory = VGroup(table_rect, table_head, entry_a, entry_b, entry_c)
        
        # Packet
        packet = Dot(color=YELLOW, radius=0.12).move_to(switch_box.get_top() + UP * 0.5)
        packet_info = Text("Dest: MAC B", font_size=14, color=YELLOW).next_to(packet, UP, buff=0.1)
        
        # Animations
        self.play(Write(title))
        self.play(
            Create(switch_box), 
            Write(switch_label), 
            Write(buffer_label)
        )
        self.play(
            Create(VGroup(pc_a, pc_b, pc_c)),
            Write(VGroup(label_a, label_b, label_c)),
            Create(VGroup(link_a, link_b, link_c))
        )
        self.play(Create(directory))
        
        # Packet arriving at Switch
        self.play(Create(packet), Write(packet_info))
        self.play(
            packet.animate.move_to(switch_box.get_center()),
            packet_info.animate.move_to(switch_box.get_center() + UP * 0.3)
        )
        
        # Switch looks up Directory
        self.play(
            entry_b.animate.set_color(YELLOW).scale(1.2),
            table_rect.animate.set_stroke(YELLOW, width=4)
        )
        self.wait(1)
        
        # Filtering: Forward only to PC B
        self.play(
            packet.animate.move_to(pc_b.get_center()),
            packet_info.animate.set_fill(opacity=0),
            run_time=1.5
        )
        
        # Highlight recipient
        self.play(
            pc_b.animate.set_color(YELLOW).set_fill(YELLOW, fill_opacity=0.6),
            Circle(radius=0.5, color=YELLOW).move_to(pc_b.get_center()).animate.scale(2).set_stroke(opacity=0)
        )
        
        self.wait(2)

        # Cleanup
        self.play(
            VGroup(switch_box, switch_label, buffer_label, directory, pc_a, pc_b, pc_c, label_a, label_b, label_c, link_a, link_b, link_c, packet).animate.set_fill(opacity=0).set_stroke(opacity=0),
            title.animate.set_fill(opacity=0)
        )