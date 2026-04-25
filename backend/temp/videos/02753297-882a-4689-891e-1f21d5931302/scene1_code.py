from manim import *

class Scene1(Scene):
    def construct(self):
        # Header title
        title = Text("Introduction to AI Agents", color=GOLD).to_edge(UP, buff=0.2)
        
        # Split screen divider
        divider = Line(UP * 2, DOWN * 2, color=WHITE)
        
        # --- Human Representation (Circle, Lines) ---
        head_h = Circle(radius=0.3, color=WHITE).move_to([-3, 1, 0])
        body_h = Line([-3, 0.7, 0], [-3, -0.3, 0], color=WHITE)
        arms_h = Line([-3.6, 0.2, 0], [-2.4, 0.2, 0], color=WHITE)
        leg1_h = Line([-3, -0.3, 0], [-3.3, -1.1, 0], color=WHITE)
        leg2_h = Line([-3, -0.3, 0], [-2.7, -1.1, 0], color=WHITE)
        h_label = Text("Human", font_size=24, color=WHITE).next_to(head_h, UP, buff=0.2)
        human_elements = VGroup(head_h, body_h, arms_h, leg1_h, leg2_h, h_label)
        
        # --- Robot Representation (Rectangle, Square, Circles) ---
        r_body = Rectangle(width=0.8, height=1.0, color=BLUE, fill_opacity=0.5).move_to([3, -0.2, 0])
        r_head = Square(side_length=0.5, color=BLUE, fill_opacity=0.5).next_to(r_body, UP, buff=0.1)
        r_eye = Dot(r_head.get_center(), color=YELLOW)
        w1 = Circle(radius=0.15, color=WHITE, fill_opacity=0.8).move_to([2.7, -0.85, 0])
        w2 = Circle(radius=0.15, color=WHITE, fill_opacity=0.8).move_to([3.3, -0.85, 0])
        r_label = Text("AI Agent", font_size=24, color=BLUE).next_to(r_head, UP, buff=0.2)
        robot_elements = VGroup(r_body, r_head, r_eye, w1, w2, r_label)

        # --- Labels & Arrows for Perceptual Components ---
        # Sensors
        s_txt_h = Text("Sensors", color=TEAL, font_size=22).move_to([-5.2, 1, 0])
        s_arr_h = Arrow(s_txt_h.get_right(), head_h.get_left(), color=TEAL, buff=0.1)
        s_txt_r = Text("Sensors", color=TEAL, font_size=22).move_to([5.2, 1, 0])
        s_arr_r = Arrow(s_txt_r.get_left(), r_head.get_right(), color=TEAL, buff=0.1)
        sensors_group = VGroup(s_txt_h, s_arr_h, s_txt_r, s_arr_r)

        # Actuators
        a_txt_h = Text("Actuators", color=RED, font_size=22).move_to([-5.2, -0.5, 0])
        a_arr_h = Arrow(a_txt_h.get_right(), arms_h.get_left(), color=RED, buff=0.1)
        a_txt_r = Text("Actuators", color=RED, font_size=22).move_to([5.2, -0.5, 0])
        a_arr_r = Arrow(a_txt_r.get_left(), w2.get_right(), color=RED, buff=0.1)
        actuators_group = VGroup(a_txt_h, a_arr_h, a_txt_r, a_arr_r)

        # Bottom footer explanation
        footer = Text("Autonomous: Perceives Environment -> Takes Action", color=GOLD, font_size=24).to_edge(DOWN, buff=0.4)

        # --- Execution Timeline ---
        self.play(Write(title))
        self.play(Create(divider))
        self.play(Create(human_elements), Create(robot_elements))
        self.wait(1)
        
        # Show Sensors (Eyes/Camera)
        self.play(Write(sensors_group))
        self.wait(1.5)
        
        # Show Actuators (Hands/Wheels)
        self.play(Write(actuators_group))
        self.wait(1.5)
        
        # Final conclusion
        self.play(Write(footer))
        self.wait(3)