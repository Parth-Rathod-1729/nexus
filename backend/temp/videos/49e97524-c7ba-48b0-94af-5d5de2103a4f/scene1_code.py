from manim import *

class Scene1(Scene):
    def construct(self):
        # Title of the scene
        title = Text("Powersort: Identifying Natural Runs", color=WHITE).scale(0.7)
        title.to_edge(UP)
        self.play(Write(title))

        # Array data to demonstrate natural runs
        vals = [2, 5, 8, 3, 7, 1, 4, 6]
        elements = VGroup()
        for v in vals:
            box = Rectangle(width=0.7, height=0.7, color=WHITE)
            lbl = Text(str(v), color=WHITE).scale(0.6).move_to(box.get_center())
            element = VGroup(box, lbl)
            elements.add(element)
        
        elements.arrange(RIGHT, buff=0.1)
        elements.move_to(ORIGIN)
        self.play(Create(elements))
        self.wait(0.5)

        # Scanner cursor that identifies the runs
        cursor = Rectangle(width=0.75, height=0.85, color=YELLOW)
        cursor.move_to(elements[0].get_center())
        self.play(Create(cursor))

        # Identify Run 1: [2, 5, 8]
        # Move cursor through the segment
        self.play(cursor.animate.move_to(elements[2].get_center()), run_time=1.2)
        r1_group = VGroup(elements[0], elements[1], elements[2])
        r1_bg = Rectangle(width=2.4, height=0.9, color=GREEN, fill_opacity=0.3, stroke_width=0)
        r1_bg.move_to(r1_group.get_center())
        r1_txt = Text("Run 1", color=GREEN).scale(0.5).next_to(r1_bg, DOWN)
        self.play(Create(r1_bg), Write(r1_txt))
        
        # Identify Run 2: [3, 7]
        # Reset cursor to start of next run and scan
        self.play(cursor.animate.move_to(elements[3].get_center()), run_time=0.4)
        self.play(cursor.animate.move_to(elements[4].get_center()), run_time=0.8)
        r2_group = VGroup(elements[3], elements[4])
        r2_bg = Rectangle(width=1.6, height=0.9, color=TEAL, fill_opacity=0.3, stroke_width=0)
        r2_bg.move_to(r2_group.get_center())
        r2_txt = Text("Run 2", color=TEAL).scale(0.5).next_to(r2_bg, DOWN)
        self.play(Create(r2_bg), Write(r2_txt))

        # Identify Run 3: [1, 4, 6]
        # Reset cursor to start of next run and scan
        self.play(cursor.animate.move_to(elements[5].get_center()), run_time=0.4)
        self.play(cursor.animate.move_to(elements[7].get_center()), run_time=1.0)
        r3_group = VGroup(elements[5], elements[6], elements[7])
        r3_bg = Rectangle(width=2.4, height=0.9, color=GOLD, fill_opacity=0.3, stroke_width=0)
        r3_bg.move_to(r3_group.get_center())
        r3_txt = Text("Run 3", color=GOLD).scale(0.5).next_to(r3_bg, DOWN)
        self.play(Create(r3_bg), Write(r3_txt))

        # Finalizing view
        self.play(cursor.animate.set_stroke(opacity=0))
        self.wait(2)