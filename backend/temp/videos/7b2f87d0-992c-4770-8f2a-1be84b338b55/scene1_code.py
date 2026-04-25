from manim import *

class Scene1(Scene):
    def construct(self):
        # Title
        title = Text("Understanding AI Agents", color=GOLD).scale(0.8)
        title.to_edge(UP)
        self.play(Write(title))

        # Vertical Divider
        divider = Line(UP * 2.5, DOWN * 2.5, color=WHITE)
        self.play(Create(divider))

        # --- Human Side (Left) ---
        human_head = Circle(radius=0.3, color=WHITE).shift(LEFT * 2.5 + UP * 1)
        human_body = Rectangle(height=1.0, width=0.6, color=BLUE, fill_opacity=0.5).next_to(human_head, DOWN, buff=0.1)
        human_eye_l = Dot(human_head.get_center() + LEFT * 0.1 + UP * 0.05, radius=0.04, color=WHITE)
        human_eye_r = Dot(human_head.get_center() + RIGHT * 0.1 + UP * 0.05, radius=0.04, color=WHITE)
        human_arm_l = Line(human_body.get_left() + UP * 0.3, human_body.get_left() + DOWN * 0.5 + LEFT * 0.3, color=BLUE)
        human_arm_r = Line(human_body.get_right() + UP * 0.3, human_body.get_right() + DOWN * 0.5 + RIGHT * 0.3, color=BLUE)
        
        human = VGroup(human_head, human_body, human_eye_l, human_eye_r, human_arm_l, human_arm_r)
        human_label = Text("Human", font_size=24).next_to(human_body, DOWN)
        
        # Human Sensors and Actuators Labels
        h_sensor_text = Text("Sensors (Eyes)", color=GREEN, font_size=20).move_to(LEFT * 5 + UP * 1)
        h_sensor_arrow = Arrow(h_sensor_text.get_right(), human_head.get_left(), color=GREEN, buff=0.1)
        
        h_actuator_text = Text("Actuators (Hands)", color=RED, font_size=20).move_to(LEFT * 5 + DOWN * 1)
        h_actuator_arrow = Arrow(h_actuator_text.get_right(), human_arm_l.get_center(), color=RED, buff=0.1)

        # --- Robot Side (Right) ---
        robot_head = Square(side_length=0.6, color=TEAL, fill_opacity=0.5).shift(RIGHT * 2.5 + UP * 1)
        robot_body = Rectangle(height=1.0, width=0.8, color=TEAL, fill_opacity=0.8).next_to(robot_head, DOWN, buff=0.1)
        robot_camera = Circle(radius=0.1, color=RED, fill_opacity=1).move_to(robot_head.get_center())
        robot_arm_l = Line(robot_body.get_left() + UP * 0.2, robot_body.get_left() + LEFT * 0.5, color=TEAL)
        robot_arm_r = Line(robot_body.get_right() + UP * 0.2, robot_body.get_right() + RIGHT * 0.5, color=TEAL)
        robot_hand_r = Square(side_length=0.2, color=TEAL).move_to(robot_arm_r.get_end())
        
        robot = VGroup(robot_head, robot_body, robot_camera, robot_arm_l, robot_arm_r, robot_hand_r)
        robot_label = Text("AI Agent", font_size=24).next_to(robot_body, DOWN)

        # Robot Sensors and Actuators Labels
        r_sensor_text = Text("Sensors (Camera)", color=GREEN, font_size=20).move_to(RIGHT * 5 + UP * 1)
        r_sensor_arrow = Arrow(r_sensor_text.get_left(), robot_camera.get_right(), color=GREEN, buff=0.1)
        
        r_actuator_text = Text("Actuators (Arm)", color=RED, font_size=20).move_to(RIGHT * 5 + DOWN * 1)
        r_actuator_arrow = Arrow(r_actuator_text.get_left(), robot_hand_r.get_left(), color=RED, buff=0.1)

        # Animations
        self.play(Create(human), Create(robot))
        self.play(Write(human_label), Write(robot_label))
        self.wait(1)

        # Highlighting Sensors
        self.play(Write(h_sensor_text), Create(h_sensor_arrow), Write(r_sensor_text), Create(r_sensor_arrow))
        self.play(human_head.animate.set_color(GREEN), robot_camera.animate.scale(1.2).set_color(YELLOW))
        self.wait(1)
        self.play(human_head.animate.set_color(WHITE), robot_camera.animate.scale(0.8).set_color(RED))

        # Highlighting Actuators
        self.play(Write(h_actuator_text), Create(h_actuator_arrow), Write(r_actuator_text), Create(r_actuator_arrow))
        self.play(human_arm_l.animate.set_color(RED), robot_hand_r.animate.set_color(RED))
        self.wait(1)

        # Definition summary
        summary = Text("Goal: Perceive and Act Independently", color=YELLOW, font_size=28).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)