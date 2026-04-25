from manim import *

class Scene1(Scene):
    def construct(self):
        # Title and Split Screen Setup
        title = Text("Physical and Data Link Layer Devices", font_size=36, color=WHITE)
        title.to_edge(UP, buff=0.5)
        
        divider = Line(start=UP * 2, end=DOWN * 3, color=WHITE)
        
        # HUB SIDE (Left)
        hub_title = Text("Hub (Physical Layer)", color=BLUE, font_size=24)
        hub_title.move_to([-3.5, 2.3, 0])
        
        hub_box = Rectangle(width=1.4, height=0.8, color=BLUE, fill_opacity=0.6)
        hub_box.move_to([-3.5, 0, 0])
        hub_label = Text("HUB", font_size=20).move_to(hub_box.get_center())
        hub_group = VGroup(hub_box, hub_label)
        
        # Hub Computers
        hc1 = Square(side_length=0.5, color=WHITE, fill_opacity=0.2).move_to([-5.5, 1.5, 0])
        hc2 = Square(side_length=0.5, color=WHITE, fill_opacity=0.2).move_to([-1.5, 1.5, 0])
        hc3 = Square(side_length=0.5, color=WHITE, fill_opacity=0.2).move_to([-5.5, -1.5, 0])
        hc4 = Square(side_length=0.5, color=WHITE, fill_opacity=0.2).move_to([-1.5, -1.5, 0])
        
        hub_computers = VGroup(hc1, hc2, hc3, hc4)
        
        # Connections for Hub
        hl1 = Line(hc1.get_center(), hub_box.get_center(), stroke_width=2, color=WHITE)
        hl2 = Line(hc2.get_center(), hub_box.get_center(), stroke_width=2, color=WHITE)
        hl3 = Line(hc3.get_center(), hub_box.get_center(), stroke_width=2, color=WHITE)
        hl4 = Line(hc4.get_center(), hub_box.get_center(), stroke_width=2, color=WHITE)
        hub_lines = VGroup(hl1, hl2, hl3, hl4)
        
        # SWITCH SIDE (Right)
        switch_title = Text("Switch/Bridge (Data Link)", color=GREEN, font_size=24)
        switch_title.move_to([3.5, 2.3, 0])
        
        switch_box = Rectangle(width=1.4, height=0.8, color=GREEN, fill_opacity=0.6)
        switch_box.move_to([3.5, 0, 0])
        switch_label = Text("SWITCH", font_size=18).move_to(switch_box.get_center())
        switch_group = VGroup(switch_box, switch_label)
        
        # Switch Computers
        sc1 = Square(side_length=0.5, color=WHITE, fill_opacity=0.2).move_to([1.5, 1.5, 0])
        sc2 = Square(side_length=0.5, color=WHITE, fill_opacity=0.2).move_to([5.5, 1.5, 0])
        sc3 = Square(side_length=0.5, color=WHITE, fill_opacity=0.2).move_to([1.5, -1.5, 0])
        sc4 = Square(side_length=0.5, color=WHITE, fill_opacity=0.2).move_to([5.5, -1.5, 0])
        
        switch_computers = VGroup(sc1, sc2, sc3, sc4)
        
        # Connections for Switch
        sl1 = Line(sc1.get_center(), switch_box.get_center(), stroke_width=2, color=WHITE)
        sl2 = Line(sc2.get_center(), switch_box.get_center(), stroke_width=2, color=WHITE)
        sl3 = Line(sc3.get_center(), switch_box.get_center(), stroke_width=2, color=WHITE)
        sl4 = Line(sc4.get_center(), switch_box.get_center(), stroke_width=2, color=WHITE)
        switch_lines = VGroup(sl1, sl2, sl3, sl4)

        # Build Scene
        self.add(title, divider)
        self.play(Write(hub_title), Write(switch_title))
        self.play(Create(hub_group), Create(switch_group))
        self.play(Create(hub_computers), Create(hub_lines), Create(switch_computers), Create(switch_lines))
        self.wait(1)

        # HUB ANIMATION (Broadcast)
        hub_signal_in = Dot(point=hc1.get_center(), color=YELLOW, radius=0.1)
        self.play(hub_signal_in.animate.move_to(hub_box.get_center()), run_time=1)
        
        hub_signal_out1 = Dot(point=hub_box.get_center(), color=YELLOW, radius=0.1)
        hub_signal_out2 = Dot(point=hub_box.get_center(), color=YELLOW, radius=0.1)
        hub_signal_out3 = Dot(point=hub_box.get_center(), color=YELLOW, radius=0.1)
        
        self.remove(hub_signal_in)
        self.play(
            hub_signal_out1.animate.move_to(hc2.get_center()),
            hub_signal_out2.animate.move_to(hc3.get_center()),
            hub_signal_out3.animate.move_to(hc4.get_center()),
            run_time=1.5
        )
        self.play(FadeOut(hub_signal_out1), FadeOut(hub_signal_out2), FadeOut(hub_signal_out3))
        
        # SWITCH ANIMATION (Selective)
        switch_signal_in = Dot(point=sc1.get_center(), color=GOLD, radius=0.1)
        self.play(switch_signal_in.animate.move_to(switch_box.get_center()), run_time=1)
        
        switch_signal_out = Dot(point=switch_box.get_center(), color=GOLD, radius=0.1)
        
        self.remove(switch_signal_in)
        self.play(
            switch_signal_out.animate.move_to(sc4.get_center()),
            run_time=1.5
        )
        self.play(FadeOut(switch_signal_out))

        # Bottom Explanation
        explanation = Text("Hubs broadcast to all ports. Switches filter by MAC address.", 
                           font_size=20, color=YELLOW).to_edge(DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(3)