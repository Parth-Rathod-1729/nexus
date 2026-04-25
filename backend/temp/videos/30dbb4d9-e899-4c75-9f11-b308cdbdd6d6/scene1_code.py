from manim import *

class Scene1(Scene):
    def construct(self):
        # Title of the scene
        title = Text("Introduction to AI Agents", color=GOLD).to_edge(UP)

        # Left side - Human Representation
        h_head = Circle(radius=0.4, color=BLUE, fill_opacity=0.2).shift(LEFT * 3 + UP * 0.5)
        h_body = Rectangle(width=0.8, height=1.0, color=BLUE, fill_opacity=0.2).next_to(h_head, DOWN, buff=0.1)
        h_label = Text("Human", font_size=20, color=BLUE).next_to(h_body, DOWN)
        human_group = VGroup(h_head, h_body, h_label)

        # Right side - Robot Representation
        r_head = Square(side_length=0.7, color=TEAL, fill_opacity=0.2).shift(RIGHT * 3 + UP * 0.5)
        r_body = Rectangle(width=0.8, height=1.0, color=TEAL, fill_opacity=0.2).next_to(r_head, DOWN, buff=0.1)
        r_label = Text("Robot", font_size=20, color=TEAL).next_to(r_body, DOWN)
        robot_group = VGroup(r_head, r_body, r_label)

        # Divider lines for split-screen look
        divider_top = Line(UP * 2.5, UP * 1.0, color=WHITE)
        divider_bottom = Line(DOWN * 1.0, DOWN * 2.5, color=WHITE)

        # Central Brain (Logic unit)
        brain_icon = Circle(radius=0.7, color=YELLOW, fill_opacity=0.1).move_to(ORIGIN)
        brain_label = Text("Brain\n(Logic)", font_size=18, color=WHITE).move_to(brain_icon.get_center())
        brain_group = VGroup(brain_icon, brain_label)

        # Sensor Labels and Arrows (Perception)
        sensor_txt = Text("Sensors", color=GREEN, font_size=28).shift(UP * 2.2)
        s_arrow_h = Arrow(sensor_txt.get_bottom(), h_head.get_top(), color=GREEN, buff=0.1)
        s_arrow_r = Arrow(sensor_txt.get_bottom(), r_head.get_top(), color=GREEN, buff=0.1)
        sensors_vgroup = VGroup(sensor_txt, s_arrow_h, s_arrow_r)

        # Actuator Labels and Arrows (Action)
        actuator_txt = Text("Actuators", color=RED, font_size=28).shift(DOWN * 2.2)
        a_arrow_h = Arrow(h_body.get_bottom(), actuator_txt.get_top(), color=RED, buff=0.1)
        a_arrow_r = Arrow(r_body.get_bottom(), actuator_txt.get_top(), color=RED, buff=0.1)
        actuators_vgroup = VGroup(actuator_txt, a_arrow_h, a_arrow_r)

        # Animation sequence
        self.play(Write(title))
        self.play(Create(human_group), Create(robot_group))
        self.play(Create(divider_top), Create(divider_bottom))
        self.wait(1)

        # Visualizing Sensors
        self.play(Write(sensors_vgroup))
        self.wait(1)

        # Visualizing Actuators
        self.play(Write(actuators_vgroup))
        self.wait(1)

        # Decision making process lighting up
        self.play(Create(brain_group))
        self.play(brain_icon.animate.set_fill(YELLOW, fill_opacity=0.7), run_time=1)
        self.wait(2)

        # Clean exit logic
        self.play(FadeOut(VGroup(title, human_group, robot_group, divider_top, divider_bottom, sensors_vgroup, actuators_vgroup, brain_group)))