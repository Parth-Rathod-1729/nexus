from manim import *

class Scene2(Scene):
    def construct(self):
        # Title and Labels
        title = Text("Routing and Global Connectivity", color=GOLD, font_size=36)
        title.to_edge(UP)
        
        concept_label = Text("Concept: Routers and IP Addressing", color=WHITE, font_size=24)
        concept_label.next_to(title, DOWN)

        # Router Representation
        router_box = Square(side_length=2.0, color=BLUE, fill_opacity=0.2)
        router_box.move_to(ORIGIN)
        router_text = Text("Router", color=BLUE, font_size=24)
        router_text.move_to(router_box.get_center())
        router_vgroup = VGroup(router_box, router_text)

        # Source and Destination Networks
        source_network = Circle(radius=0.8, color=TEAL, fill_opacity=0.1)
        source_network.move_to(LEFT * 5)
        source_label = Text("LAN A", color=TEAL, font_size=20).next_to(source_network, DOWN)

        dest_network = Circle(radius=0.8, color=GREEN, fill_opacity=0.1)
        dest_network.move_to(RIGHT * 5)
        dest_label = Text("WAN / LAN B", color=GREEN, font_size=20).next_to(dest_network, DOWN)

        # Interconnected Nodes (The "Web")
        node1 = Dot(RIGHT * 2.5 + UP * 1.5, color=WHITE)
        node2 = Dot(RIGHT * 2.5 + DOWN * 1.5, color=WHITE)
        
        line_to_n1 = Line(router_box.get_right(), node1.get_center(), color=GRAY)
        line_to_n2 = Line(router_box.get_right(), node2.get_center(), color=GRAY)
        line_n1_to_dest = Line(node1.get_center(), dest_network.get_left(), color=GRAY)
        line_n2_to_dest = Line(node2.get_center(), dest_network.get_left(), color=GRAY)
        
        web_vgroup = VGroup(node1, node2, line_to_n1, line_to_n2, line_n1_to_dest, line_n2_to_dest)

        # Data Packet
        packet_rect = Rectangle(width=1.0, height=0.6, color=WHITE, fill_opacity=1.0)
        packet_rect.move_to(source_network.get_center())
        packet_id = Text("IP: 192.0.2.1", color=BLACK, font_size=14)
        packet_id.move_to(packet_rect.get_center())
        packet = VGroup(packet_rect, packet_id)

        # Routing Table
        table_rect = Rectangle(width=2.5, height=1.5, color=GOLD, fill_opacity=0.1)
        table_rect.next_to(router_box, UP, buff=0.5)
        table_title = Text("Routing Table", color=GOLD, font_size=16).move_to(table_rect.get_top() + DOWN * 0.2)
        table_entry = Text("192.0.2.1 -> Path alpha", color=WHITE, font_size=20).move_to(table_rect.get_center())
        routing_table = VGroup(table_rect, table_title, table_entry)

        # Animation Sequence
        self.play(Write(title))
        self.play(FadeIn(concept_label))
        self.wait(1)

        # Show Networks and Router
        self.play(
            Create(source_network), Write(source_label),
            Create(dest_network), Write(dest_label),
            Create(router_vgroup)
        )
        self.play(Create(web_vgroup))
        self.wait(1)

        # Packet Arrival
        self.play(FadeIn(packet))
        self.play(packet.animate.move_to(router_box.get_left() + RIGHT * 0.5))
        self.wait(0.5)

        # Inspect IP and Routing Table
        self.play(Create(routing_table))
        self.play(packet_id.animate.set_color(RED))
        self.play(Indicate(table_entry, color=RED))
        self.wait(1)

        # Choosing the path (Highlighting a path)
        path_arrow1 = Arrow(router_box.get_right(), node1.get_center(), color=YELLOW, buff=0.1)
        path_arrow2 = Arrow(node1.get_center(), dest_network.get_left(), color=YELLOW, buff=0.1)
        
        self.play(Create(path_arrow1))
        self.play(packet.animate.move_to(node1.get_center()))
        self.play(Create(path_arrow2))
        self.play(packet.animate.move_to(dest_network.get_center()))
        
        # Conclusion of movement
        self.play(packet_id.animate.set_color(BLACK))
        self.play(FadeOut(routing_table), FadeOut(path_arrow1), FadeOut(path_arrow2))
        
        # Final Text
        explanation = Text("Router selects the best path based on destination IP.", 
                           color=WHITE, font_size=18).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)

        # Cleanup for scene end
        self.play(
            FadeOut(packet), 
            FadeOut(router_vgroup), 
            FadeOut(source_network), 
            FadeOut(dest_network),
            FadeOut(web_vgroup),
            FadeOut(title),
            FadeOut(concept_label),
            FadeOut(explanation),
            FadeOut(source_label),
            FadeOut(dest_label)
        )
        self.wait(1)