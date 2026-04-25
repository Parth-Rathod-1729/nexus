from manim import *

class Scene1(Scene):
    def construct(self):
        # Title
        title = Text("AI Agent", color=GOLD).to_edge(UP)

        # Robot construction
        body = Square(side_length=1.5, color=BLUE, fill_opacity=0.6)
        head = Circle(radius=0.4, color=WHITE, fill_opacity=0.9).next_to(body, UP, buff=0.1)
        eye_l = Dot(point=head.get_center() + LEFT * 0.15 + UP * 0.1, color=RED)
        eye_r = Dot(point=head.get_center() + RIGHT * 0.15 + UP * 0.1, color=RED)
        arm_l = Rectangle(width=0.3, height=1.0, color=TEAL, fill_opacity=0.8).next_to(body, LEFT, buff=0.1)
        arm_r = Rectangle(width=0.3, height=1.0, color=TEAL, fill_opacity=0.8).next_to(body, RIGHT, buff=0.1)
        robot = VGroup(body, head, eye_l, eye_r, arm_l, arm_r)

        # Labels and Arrows
        sensors_label = Text("Sensors", color=YELLOW).move_to(LEFT * 4.5 + UP * 1.5)
        sensor_arrow = Arrow(start=sensors_label.get_right(), end=head.get_left(), color=YELLOW)
        sensors_group = VGroup(sensors_label, sensor_arrow)

        actuators_label = Text("Actuators", color=GREEN).move_to(RIGHT * 4.5 + DOWN * 1.5)
        actuator_arrow = Arrow(start=actuators_label.get_left(), end=arm_r.get_right(), color=GREEN)
        actuators_group = VGroup(actuators_label, actuator_arrow)

        # Environment frame
        env_box = Rectangle(width=12.5, height=6.5, color=WHITE)
        env_text = Text("Environment", color=WHITE).scale(0.6).to_corner(UL, buff=0.5)

        # Animations
        self.play(Write(title))
        self.wait(0.5)
        
        self.play(Create(robot))
        self.wait(1)
        
        # Perception phase
        self.play(Create(sensors_group))
        self.play(head.animate.set_color(YELLOW), run_time=0.5)
        self.play(head.animate.set_color(WHITE), run_time=0.5)
        
        # Action phase
        self.play(Create(actuators_group))
        self.play(arm_l.animate.shift(LEFT * 0.2), arm_r.animate.shift(RIGHT * 0.2), run_time=0.5)
        self.play(arm_l.animate.shift(RIGHT * 0.2), arm_r.animate.shift(LEFT * 0.2), run_time=0.5)
        
        # Environmental context
        self.play(Create(env_box), Write(env_text))
        self.wait(2)

        # Clear scene briefly to conclude
        self.play(FadeOut(robot), FadeOut(sensors_group), FadeOut(actuators_group), FadeOut(env_box), FadeOut(env_text), FadeOut(title))
        self.wait(1)