from manim import *

class Scene2(Scene):
    def construct(self):
        # Title and Split Screen
        title = Text("Sensors and Actuators", color=WHITE).scale(0.8).to_edge(UP)
        divider = Line(UP * 2.5, DOWN * 3, color=WHITE)
        
        human_label = Text("Human", color=BLUE).move_to([-3.5, 2.5, 0]).scale(0.7)
        robot_label = Text("Robot", color=GREEN).move_to([3.5, 2.5, 0]).scale(0.7)
        
        # Human Representation
        head = Circle(radius=0.4, color=WHITE).move_to([-3.5, 0.8, 0])
        eye_l = Dot(head.get_center() + LEFT*0.15 + UP*0.1, color=BLUE)
        eye_r = Dot(head.get_center() + RIGHT*0.15 + UP*0.1, color=BLUE)
        torso = Line([-3.5, 0.4, 0], [-3.5, -0.6, 0])
        arm_l = Line([-3.5, 0.1, 0], [-4.2, -0.3, 0])
        arm_r = Line([-3.5, 0.1, 0], [-2.8, -0.3, 0])
        human_group = VGroup(head, eye_l, eye_r, torso, arm_l, arm_r)
        
        h_sensor_text = Text("Sensors", color=TEAL).scale(0.5).move_to([-5.2, 1.2, 0])
        h_sensor_arrow = Arrow(h_sensor_text.get_right(), head.get_left(), buff=0.1, color=TEAL)
        
        h_actuator_text = Text("Actuators", color=TEAL).scale(0.5).move_to([-5.2, -0.3, 0])
        h_actuator_arrow = Arrow(h_actuator_text.get_right(), arm_l.get_start(), buff=0.1, color=TEAL)

        # Robot Representation
        r_body = Square(side_length=1.0, color=WHITE).move_to([3.5, 0, 0])
        r_camera = Rectangle(width=0.4, height=0.2, color=RED, fill_opacity=0.8).next_to(r_body, UP, buff=0.05)
        wheel_l = Circle(radius=0.2, color=WHITE, fill_opacity=0.5).move_to([3.1, -0.7, 0])
        wheel_r = Circle(radius=0.2, color=WHITE, fill_opacity=0.5).move_to([3.9, -0.7, 0])
        robot_group = VGroup(r_body, r_camera, wheel_l, wheel_r)

        r_sensor_text = Text("Sensors", color=GOLD).scale(0.5).move_to([5.2, 1.2, 0])
        r_sensor_arrow = Arrow(r_sensor_text.get_left(), r_camera.get_right(), buff=0.1, color=GOLD)
        
        r_actuator_text = Text("Actuators", color=GOLD).scale(0.5).move_to([5.2, -0.7, 0])
        r_actuator_arrow = Arrow(r_actuator_text.get_left(), wheel_r.get_right(), buff=0.1, color=GOLD)

        # Animation Sequence
        self.play(Write(title))
        self.play(Create(divider))
        self.wait(1)

        # Show Human Side
        self.play(Write(human_label), Create(human_group))
        self.play(Write(h_sensor_text), Create(h_sensor_arrow))
        self.play(Write(h_actuator_text), Create(h_actuator_arrow))
        
        # Show Robot Side
        self.play(Write(robot_label), Create(robot_group))
        self.play(Write(r_sensor_text), Create(r_sensor_arrow))
        self.play(Write(r_actuator_text), Create(r_actuator_arrow))
        
        # Perception and Action Logic
        explanation = Text("Data -> Signal -> Action", color=YELLOW).scale(0.6).to_edge(DOWN)
        self.play(Write(explanation))
        
        self.wait(2)
        
        # Conclusion Fade
        self.play(
            FadeOut(human_group), FadeOut(robot_group),
            FadeOut(h_sensor_text), FadeOut(h_actuator_text),
            FadeOut(r_sensor_text), FadeOut(r_actuator_text),
            FadeOut(h_sensor_arrow), FadeOut(h_actuator_arrow),
            FadeOut(r_sensor_arrow), FadeOut(r_actuator_arrow),
            FadeOut(human_label), FadeOut(robot_label),
            FadeOut(title), FadeOut(divider), FadeOut(explanation)
        )