from manim import *

class Scene1(Scene):
    def construct(self):
        # 1. Header Title
        title = Text("Defining the AI Agent", color=BLUE).to_edge(UP, buff=0.5)

        # 2. Environment (Room)
        # Using a Rectangle to represent the room
        room = Rectangle(width=11, height=6, color=WHITE).shift(DOWN * 0.2)
        room_label = Text("Environment", color=WHITE, font_size=20).move_to(room.get_bottom() + UP * 0.3)

        # 3. AI Agent (Robot using basic shapes)
        # Body and head
        body = Square(side_length=1.4, fill_opacity=0.6, color=TEAL)
        head = Circle(radius=0.4, fill_opacity=1.0, color=TEAL).next_to(body, UP, buff=0)
        # Face (Eyes)
        eye_l = Dot(color=WHITE, radius=0.06).move_to(head.get_center() + LEFT * 0.15 + UP * 0.1)
        eye_r = Dot(color=WHITE, radius=0.06).move_to(head.get_center() + RIGHT * 0.15 + UP * 0.1)
        
        robot_shapes = VGroup(body, head, eye_l, eye_r)
        agent_label = Text("AI Agent", color=TEAL, font_size=28).next_to(head, UP, buff=0.2)
        agent_vgroup = VGroup(robot_shapes, agent_label).move_to(ORIGIN)

        # 4. Sensors (Inputs from room to agent)
        # Representing Cameras and IR
        sensor_arrow = Arrow(start=LEFT * 4.8 + UP * 1.5, end=LEFT * 0.8 + UP * 0.5, color=YELLOW, stroke_width=4)
        sensor_text = Text("Sensors\n(Cameras, IR)", color=YELLOW, font_size=22).next_to(sensor_arrow, UP, buff=0.1)
        sensors_vgroup = VGroup(sensor_arrow, sensor_text)

        # 5. Actuators (Outputs from agent to room/floor)
        # Representing Wheels and Vacuum Brushes
        actuator_arrow = Arrow(start=RIGHT * 0.8 + DOWN * 0.5, end=RIGHT * 4.8 + DOWN * 2.0, color=RED, stroke_width=4)
        actuator_text = Text("Actuators\n(Wheels, Brushes)", color=RED, font_size=22).next_to(actuator_arrow, UP, buff=0.1)
        actuators_vgroup = VGroup(actuator_arrow, actuator_text)

        # 6. Conclusion Text
        goal_text = Text("Achieves goals autonomously", color=GOLD, font_size=24).to_edge(DOWN, buff=0.3)

        # Animation Sequence
        self.play(Write(title))
        self.wait(0.5)

        # Show Environment and the Agent
        self.play(Create(room), Write(room_label))
        self.play(Create(robot_shapes), Write(agent_label))
        self.wait(1)

        # Animate Sensory Input
        self.play(Create(sensor_arrow), Write(sensor_text), run_time=1.5)
        self.wait(1)

        # Animate Actuator Response
        self.play(Create(actuator_arrow), Write(actuator_text), run_time=1.5)
        self.wait(1)

        # Final explanation text
        self.play(Write(goal_text))
        self.wait(2.5)