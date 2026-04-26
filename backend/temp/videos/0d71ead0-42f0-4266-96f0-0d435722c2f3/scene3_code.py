from manim import *

class Scene3(Scene):
    def construct(self):
        # --- Router Section (Top) ---
        lan_box = Rectangle(width=2.5, height=1.5, color=WHITE)
        lan_text = Text("Office LAN", font_size=24).move_to(lan_box.get_center())
        lan = VGroup(lan_box, lan_text).shift(UP * 2 + LEFT * 4)

        router_sq = Square(side_length=1.2, color=BLUE, fill_opacity=0.4)
        router_text = Text("Router", font_size=20).move_to(router_sq.get_center())
        router = VGroup(router_sq, router_text).shift(UP * 2)

        wan_circ = Circle(radius=0.9, color=TEAL, fill_opacity=0.4)
        wan_text = Text("WAN Cloud", font_size=22).move_to(wan_circ.get_center())
        wan = VGroup(wan_circ, wan_text).shift(UP * 2 + RIGHT * 4)

        # Connections for Router
        arrow_r1 = Arrow(lan.get_right(), router.get_left(), buff=0.1, color=WHITE)
        arrow_r2 = Arrow(router.get_right(), wan.get_left(), buff=0.1, color=WHITE)

        # Routing Table
        table_box = Rectangle(width=2, height=1, color=GOLD)
        table_title = Text("IP Table", font_size=16).next_to(table_box.get_top(), DOWN, buff=0.1)
        entry1 = Line(LEFT*0.6, RIGHT*0.6, color=GOLD).shift(DOWN*0.1)
        entry2 = Line(LEFT*0.6, RIGHT*0.6, color=GOLD).shift(DOWN*0.3)
        routing_table = VGroup(table_box, table_title, entry1, entry2).next_to(router, DOWN, buff=0.2)

        # --- Gateway Section (Bottom) ---
        sys_a_circ = Circle(radius=0.7, color=RED, fill_opacity=0.3)
        sys_a_text = Text("System A", font_size=18).move_to(sys_a_circ.get_center())
        sys_a = VGroup(sys_a_circ, sys_a_text).shift(DOWN * 2 + LEFT * 4)

        gateway_rect = Rectangle(width=2, height=1.2, color=YELLOW, fill_opacity=0.3)
        gateway_text = Text("Gateway", font_size=20).move_to(gateway_rect.get_center())
        gateway = VGroup(gateway_rect, gateway_text).shift(DOWN * 2)

        sys_b_sq = Square(side_length=1.4, color=GREEN, fill_opacity=0.3)
        sys_b_text = Text("System B", font_size=18).move_to(sys_b_sq.get_center())
        sys_b = VGroup(sys_b_sq, sys_b_text).shift(DOWN * 2 + RIGHT * 4)

        # Protocol Arrow
        conv_arrow = Arrow(sys_a.get_right(), sys_b.get_left(), color=YELLOW, buff=0.2)
        conv_label = Text("Protocol Conversion", font_size=14, color=YELLOW).next_to(conv_arrow, UP, buff=0.1)

        # --- Animations ---
        # Part 1: Router and IP Table
        self.play(Create(lan), Create(router), Create(wan))
        self.play(Create(arrow_r1), Create(arrow_r2))
        self.play(Write(routing_table))
        
        # Packet flow
        packet = Dot(color=YELLOW).move_to(lan.get_center())
        self.play(packet.animate.move_to(router.get_center()), run_time=1)
        self.play(entry1.animate.set_color(WHITE), run_time=0.5)
        self.play(packet.animate.move_to(wan.get_center()), run_time=1)
        self.play(FadeOut(packet))
        
        # Part 2: Gateway and Protocol Conversion
        self.play(Create(sys_a), Create(gateway), Create(sys_b))
        self.play(Create(conv_arrow), Write(conv_label))
        
        # Symbolic pulse of conversion
        pulse = Circle(radius=0.1, color=WHITE).move_to(gateway.get_center())
        self.play(pulse.animate.scale(8).set_fill_opacity(0), run_time=1.5)
        
        self.wait(2)