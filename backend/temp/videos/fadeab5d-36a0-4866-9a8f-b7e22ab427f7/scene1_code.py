from manim import *

class Scene1(Scene):
    def construct(self):
        # Title
        title = Text("What is an AI Agent?", color=BLUE).to_edge(UP)
        
        # Human Representation (Left)
        h_head = Circle(radius=0.4, color=WHITE).move_to([-3, 1, 0])
        h_body = Line([-3, 0.6, 0], [-3, -0.8, 0], color=WHITE)
        h_arms = Line([-3.7, 0, 0], [-2.3, 0, 0], color=WHITE)
        h_legs = VGroup(
            Line([-3, -0.8, 0], [-3.4, -1.8, 0], color=WHITE),
            Line([-3, -0.8, 0], [-2.6, -1.8, 0], color=WHITE)
        )
        human = VGroup(h_head, h_body, h_arms, h_legs)
        human_label = Text("Human", font_size=24).next_to(human, DOWN)

        # Robot Representation (Right)
        r_head = Square(side_length=0.7, color=TEAL).move_to([3, 1, 0])
        r_eye1 = Dot(point=[2.85, 1.1, 0], color=WHITE)
        r_eye2 = Dot(point=[3.15, 1.1, 0], color=WHITE)
        r_body = Rectangle(width=1.2, height=1.5, color=TEAL, fill_opacity=0.2).move_to([3, -0.2, 0])
        r_wheels = VGroup(
            Circle(radius=0.2, color=WHITE).move_to([2.5, -1.2, 0]),
            Circle(radius=0.2, color=WHITE).move_to([3.5, -1.2, 0])
        )
        robot = VGroup(r_head, r_eye1, r_eye2, r_body, r_wheels)
        robot_label = Text("Robot Agent", font_size=24).next_to(robot, DOWN)

        # Central Labels
        sensor_label = Text("Sensors", color=YELLOW, font_size=28).move_to([0, 1, 0])
        actuator_label = Text("Actuators", color=YELLOW, font_size=28).move_to([0, -1, 0])
        
        # Arrows
        s_arrow_h = Arrow(sensor_label.get_left(), h_head.get_top(), color=GOLD, buff=0.1)
        s_arrow_r = Arrow(sensor_label.get_right(), r_head.get_top(), color=GOLD, buff=0.1)
        a_arrow_h = Arrow(actuator_label.get_left(), h_legs.get_center(), color=GOLD, buff=0.1)
        a_arrow_r = Arrow(actuator_label.get_right(), r_wheels.get_center(), color=GOLD, buff=0.1)

        # Brain Component (Robot)
        brain = Circle(radius=0.3, color=RED, fill_opacity=0.8).move_to([3, -0.2, 0])
        brain_text = Text("Brain", color=WHITE, font_size=20).move_to(brain.get_center())
        brain_group = VGroup(brain, brain_text)
        
        # Internal Connections (Robot)
        line_to_brain = Line(r_head.get_bottom(), brain.get_top(), color=RED)
        line_from_brain = Line(brain.get_bottom(), r_wheels.get_top(), color=RED)

        # Animation Sequence
        self.play(Write(title))
        self.wait(0.5)
        
        self.play(Create(human), Create(robot))
        self.play(Write(human_label), Write(robot_label))
        self.wait(1)

        self.play(
            Write(sensor_label),
            Create(s_arrow_h),
            Create(s_arrow_r)
        )
        self.wait(1)

        self.play(
            Write(actuator_label),
            Create(a_arrow_h),
            Create(a_arrow_r)
        )
        self.wait(1)

        self.play(
            Create(brain_group),
            Create(line_to_brain),
            Create(line_from_brain)
        )
        self.wait(2)

        # Final cleanup
        self.play(
            FadeOut(human), FadeOut(robot), FadeOut(title),
            FadeOut(sensor_label), FadeOut(actuator_label),
            FadeOut(s_arrow_h), FadeOut(s_arrow_r),
            FadeOut(a_arrow_h), FadeOut(a_arrow_r),
            FadeOut(brain_group), FadeOut(line_to_brain),
            FadeOut(line_from_brain), FadeOut(human_label), FadeOut(robot_label)
        )
        self.wait(1)