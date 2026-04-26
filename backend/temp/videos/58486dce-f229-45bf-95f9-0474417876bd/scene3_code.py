from manim import *

class Scene3(Scene):
    def construct(self):
        # 1. Setup Hub and Computers
        hub = Rectangle(height=1.5, width=2.5, color=TEAL, fill_opacity=0.2)
        hub_label = Text("HUB", font_size=32, color=TEAL).move_to(hub.get_center())
        hub_group = VGroup(hub, hub_label)

        pc1 = Square(side_length=1.2, color=BLUE, fill_opacity=0.2).move_to(LEFT * 4)
        pc1_label = Text("PC 1", font_size=24).next_to(pc1, DOWN)
        pc1_group = VGroup(pc1, pc1_label)

        pc2 = Square(side_length=1.2, color=BLUE, fill_opacity=0.2).move_to(RIGHT * 4)
        pc2_label = Text("PC 2", font_size=24).next_to(pc2, DOWN)
        pc2_group = VGroup(pc2, pc2_label)

        # 2. Connections
        line1 = Line(pc1.get_right(), hub.get_left(), color=WHITE)
        line2 = Line(pc2.get_left(), hub.get_right(), color=WHITE)

        # 3. Bandwidth Bar at Top
        bw_title = Text("Total Bandwidth", font_size=24).to_edge(UP).shift(LEFT * 2)
        bw_bar_outline = Rectangle(height=0.4, width=6, color=WHITE).next_to(bw_title, RIGHT)
        
        # Bandwidth segments
        seg1 = Rectangle(height=0.4, width=2, color=GOLD, fill_opacity=0.8).move_to(bw_bar_outline.get_left(), aligned_edge=LEFT)
        seg2 = Rectangle(height=0.4, width=2, color=GOLD, fill_opacity=0.6).next_to(seg1, RIGHT, buff=0)
        seg3 = Rectangle(height=0.4, width=2, color=GOLD, fill_opacity=0.4).next_to(seg2, RIGHT, buff=0)
        bw_segments = VGroup(seg1, seg2, seg3)
        bw_label = Text("Shared Segments", font_size=20, color=GOLD).next_to(bw_bar_outline, DOWN)

        # 4. Collision Graphics
        collision_circle = Circle(radius=0.6, color=RED, fill_opacity=0.7).move_to(hub.get_center())
        collision_text = Text("COLLISION", font_size=22, color=YELLOW, weight=BOLD).move_to(hub.get_center())
        collision_group = VGroup(collision_circle, collision_text)

        # Signals
        sig1 = Dot(color=YELLOW).move_to(pc1.get_center())
        sig2 = Dot(color=YELLOW).move_to(pc2.get_center())

        # --- ANIMATION SEQUENCE ---
        
        # Show setup
        self.play(
            Create(hub_group),
            Create(pc1_group),
            Create(pc2_group),
            Create(line1),
            Create(line2)
        )
        self.wait(1)

        # Signals moving toward hub
        self.play(
            sig1.animate.move_to(hub.get_center()),
            sig2.animate.move_to(hub.get_center()),
            run_time=2,
            rate_func=linear
        )

        # Collision happens
        self.play(
            FadeIn(collision_group, scale=1.5),
            Flash(hub, color=RED, line_length=0.4, flash_radius=1)
        )
        self.wait(1)

        # Show Shared Bandwidth concept
        self.play(
            FadeOut(sig1, sig2),
            Create(bw_bar_outline),
            Write(bw_title)
        )
        
        self.play(
            Create(bw_segments),
            Write(bw_label),
            run_time=2
        )
        
        # Final emphasis on collision domain
        domain_label = Text("Single Collision Domain", color=RED, font_size=28).next_to(hub, DOWN, buff=1)
        self.play(Write(domain_label))
        
        self.wait(2)

        # Cleanup
        self.play(
            FadeOut(hub_group, pc1_group, pc2_group, line1, line2, collision_group, bw_bar_outline, bw_segments, bw_title, bw_label, domain_label)
        )