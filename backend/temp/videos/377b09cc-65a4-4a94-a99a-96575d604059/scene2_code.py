from manim import *

class Scene2(Scene):
    def construct(self):
        self.camera.background_color = "#282828"

        # Title
        title_text = Text("How Agents Interact with their Environment", font_size=40, color=GOLD).to_edge(UP)
        self.play(Write(title_text))
        self.wait(1)

        # Core Interaction Flow
        env_label = Text("Environment", font_size=30, color=BLUE)
        sensors_label = Text("Sensors", font_size=30, color=GREEN)
        agent_label = Text("Agent", font_size=30, color=TEAL)
        actuators_label = Text("Actuators", font_size=30, color=RED)

        flow_group = VGroup(env_label, sensors_label, agent_label, actuators_label).arrange(RIGHT, buff=1.5)
        flow_group.next_to(title_text, DOWN, buff=1.0)

        arrow1 = Arrow(env_label.get_right(), sensors_label.get_left(), buff=0.2, max_tip_length_to_length_ratio=0.1)
        arrow2 = Arrow(sensors_label.get_right(), agent_label.get_left(), buff=0.2, max_tip_length_to_length_ratio=0.1)
        arrow3 = Arrow(agent_label.get_right(), actuators_label.get_left(), buff=0.2, max_tip_length_to_length_ratio=0.1)
        arrow4 = Arrow(actuators_label.get_right(), env_label.get_right() + RIGHT * 0.5, buff=0.2, max_tip_length_to_length_ratio=0.1)
        arrow4.put_start_and_end_on(actuators_label.get_right(), env_label.get_right() + RIGHT * 0.5) # Initial positioning
        arrow4_curve = ArcBetweenPoints(
            actuators_label.get_right(),
            env_label.get_right(),
            angle= -PI / 2 # Curve downwards then up to reconnect
        )
        # Manually adjust for a loop
        arrow4_points = [
            actuators_label.get_right() + RIGHT * 0.2,
            actuators_label.get_right() + RIGHT * 1.0 + DOWN * 0.5,
            env_label.get_right() + RIGHT * 1.0 + DOWN * 0.5,
            env_label.get_right() + RIGHT * 0.2
        ]
        arrow4_line = Line(arrow4_points[0], arrow4_points[1])
        arrow4_line2 = Line(arrow4_points[1], arrow4_points[2])
        arrow4_line3 = Line(arrow4_points[2], arrow4_points[3])

        curved_arrow4 = Arrow(
            actuators_label.get_right(),
            env_label.get_right(),
            path_arc=-PI/2, # Makes it curve downwards then up
            tip_length=0.2
        )
        # Position adjustments for the curved arrow
        curved_arrow4.shift(RIGHT * 1.5 + DOWN * 0.5) # Shift the entire arc
        curved_arrow4.put_start_and_end_on(actuators_label.get_right(), env_label.get_right()) # Correct start/end points after shifting
        curved_arrow4.shift(RIGHT * 0.5 + DOWN * 0.5) # Fine tune

        # Create a more controlled curved arrow by using a quadratic Bezier curve
        p1 = actuators_label.get_right() + RIGHT * 0.2
        p2 = actuators_label.get_right() + RIGHT * 1.0 + DOWN * 0.5
        p3 = env_label.get_right() + RIGHT * 1.0 + DOWN * 0.5
        p4 = env_label.get_right() + RIGHT * 0.2

        curved_arrow_segment1 = Line(p1, p2, color=RED)
        curved_arrow_segment2 = Line(p2, p3, color=RED)
        curved_arrow_segment3 = Arrow(p3, p4, color=RED) # Arrowhead on the last segment

        feedback_flow = VGroup(arrow1, arrow2, arrow3, curved_arrow_segment1, curved_arrow_segment2, curved_arrow_segment3)

        self.play(
            FadeIn(flow_group),
            Create(arrow1),
            Create(arrow2),
            Create(arrow3),
            run_time=2
        )
        self.play(Create(curved_arrow_segment1), Create(curved_arrow_segment2), Create(curved_arrow_segment3))
        self.wait(1)

        # Explanation boxes for Percept and Percept Sequence
        percept_box_label = Text("Percept", font_size=24, color=GREEN).shift(UP * 2 + LEFT * 4.5)
        percept_box = Rectangle(width=3, height=1.5, color=GREEN, fill_opacity=0.1).next_to(percept_box_label, DOWN, buff=0.2)
        percept_def = Text("Agent's perceptual input\nat any instant.", font_size=20, color=WHITE).move_to(percept_box.get_center())

        percept_seq_box_label = Text("Percept Sequence", font_size=24, color=TEAL).shift(UP * 2 + RIGHT * 4.5)
        percept_seq_box = Rectangle(width=3, height=1.5, color=TEAL, fill_opacity=0.1).next_to(percept_seq_box_label, DOWN, buff=0.2)
        percept_seq_def = Text("Complete record of\neverything perceived\n(history).", font_size=20, color=WHITE).move_to(percept_seq_box.get_center())

        self.play(
            Write(percept_box_label), Create(percept_box), Write(percept_def),
            Write(percept_seq_box_label), Create(percept_seq_box), Write(percept_seq_def)
        )
        self.wait(2)

        self.play(
            FadeOut(percept_box_label), FadeOut(percept_box), FadeOut(percept_def),
            FadeOut(percept_seq_box_label), FadeOut(percept_seq_box), FadeOut(percept_seq_def),
            FadeOut(feedback_flow),
            FadeOut(flow_group)
        )
        self.wait(1)

        # Human Agent Example
        human_agent_title = Text("Human Agent Example", font_size=36, color=GOLD).to_edge(UP)
        self.play(Transform(title_text, human_agent_title))
        self.wait(0.5)

        # Human agent box
        human_agent_box_label = Text("HUMAN AGENT", font_size=24, color=TEAL).next_to(title_text, DOWN, buff=0.8).shift(LEFT * 3)
        human_agent_box = Rectangle(width=4.5, height=3, color=TEAL, fill_opacity=0.1).next_to(human_agent_box_label, DOWN, buff=0.2)
        
        # Human Sensors
        human_sensors_label = Text("Sensors (5 Senses)", font_size=24, color=GREEN).next_to(human_agent_box_label, DOWN, buff=0.2).align_to(human_agent_box.get_left(), LEFT).shift(LEFT * 0.5)
        human_sensors_list = VGroup(
            Text("- Eyes (Sight)", font_size=20, color=WHITE),
            Text("- Ears (Hearing)", font_size=20, color=WHITE),
            Text("- Nose (Smell)", font_size=20, color=WHITE),
            Text("- Tongue (Taste)", font_size=20, color=WHITE),
            Text("- Skin (Touch)", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(human_agent_box.get_left(), RIGHT, buff=0.5).shift(DOWN * 0.3)
        
        # Human Actuators
        human_actuators_label = Text("Actuators", font_size=24, color=RED).next_to(human_sensors_list, RIGHT, buff=2).shift(UP * 0.5)
        human_actuators_list = VGroup(
            Text("- Hands (Manipulate)", font_size=20, color=WHITE),
            Text("- Legs (Locomotion)", font_size=20, color=WHITE),
            Text("- Mouth (Speak)", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(human_actuators_label, DOWN, buff=0.2)

        self.play(
            Write(human_agent_box_label), Create(human_agent_box),
            Write(human_sensors_label), Write(human_sensors_list),
            Write(human_actuators_label), Write(human_actuators_list)
        )
        self.wait(2)

        # Arrows for human interaction
        human_env_label = Text("Environment", font_size=24, color=BLUE).next_to(human_sensors_list, LEFT, buff=1.0)
        human_env_arrow_to_sensors = Arrow(human_env_label.get_right(), human_sensors_list.get_left(), buff=0.2, max_tip_length_to_length_ratio=0.1)
        human_sensors_arrow_to_agent = Arrow(human_sensors_list.get_right(), human_agent_box.get_left(), buff=0.2, max_tip_length_to_length_ratio=0.1)
        human_agent_arrow_to_actuators = Arrow(human_agent_box.get_right(), human_actuators_list.get_left(), buff=0.2, max_tip_length_to_length_ratio=0.1)
        human_actuators_arrow_to_env = Arrow(human_actuators_list.get_right(), human_env_label.get_right() + RIGHT * 0.5, buff=0.2, max_tip_length_to_length_ratio=0.1)
        
        # Curved arrow for human feedback
        p_h1 = human_actuators_list.get_right() + RIGHT * 0.2
        p_h2 = human_actuators_list.get_right() + RIGHT * 1.0 + DOWN * 0.5
        p_h3 = human_env_label.get_right() + RIGHT * 1.0 + DOWN * 0.5
        p_h4 = human_env_label.get_right() + RIGHT * 0.2

        human_curved_segment1 = Line(p_h1, p_h2, color=RED)
        human_curved_segment2 = Line(p_h2, p_h3, color=RED)
        human_curved_segment3 = Arrow(p_h3, p_h4, color=RED)

        self.play(
            Write(human_env_label),
            Create(human_env_arrow_to_sensors),
            Create(human_sensors_arrow_to_agent),
            Create(human_agent_arrow_to_actuators),
            Create(human_curved_segment1), Create(human_curved_segment2), Create(human_curved_segment3)
        )
        self.wait(2)

        self.play(
            FadeOut(human_agent_box_label), FadeOut(human_agent_box),
            FadeOut(human_sensors_label), FadeOut(human_sensors_list),
            FadeOut(human_actuators_label), FadeOut(human_actuators_list),
            FadeOut(human_env_label), FadeOut(human_env_arrow_to_sensors),
            FadeOut(human_sensors_arrow_to_agent), FadeOut(human_agent_arrow_to_actuators),
            FadeOut(human_curved_segment1), FadeOut(human_curved_segment2), FadeOut(human_curved_segment3)
        )
        self.wait(1)

        # Robot Agent Example
        robot_agent_title = Text("Robot Agent Example", font_size=36, color=GOLD).to_edge(UP)
        self.play(Transform(title_text, robot_agent_title))
        self.wait(0.5)

        # Robot agent box
        robot_agent_box_label = Text("ROBOT AGENT", font_size=24, color=TEAL).next_to(title_text, DOWN, buff=0.8).shift(LEFT * 3)
        robot_agent_box = Rectangle(width=4.5, height=3, color=TEAL, fill_opacity=0.1).next_to(robot_agent_box_label, DOWN, buff=0.2)
        
        # Robot Sensors
        robot_sensors_label = Text("Sensors", font_size=24, color=GREEN).next_to(robot_agent_box_label, DOWN, buff=0.2).align_to(robot_agent_box.get_left(), LEFT).shift(LEFT * 0.5)
        robot_sensors_list = VGroup(
            Text("- Cameras (Vision)", font_size=20, color=WHITE),
            Text("- Microphones (Audio)", font_size=20, color=WHITE),
            Text("- Sonar/Lidar (Distance)", font_size=20, color=WHITE),
            Text("- Temperature Sensors", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(robot_agent_box.get_left(), RIGHT, buff=0.5).shift(DOWN * 0.3)
        
        # Robot Actuators
        robot_actuators_label = Text("Actuators", font_size=24, color=RED).next_to(robot_sensors_list, RIGHT, buff=2).shift(UP * 0.5)
        robot_actuators_list = VGroup(
            Text("- Motors (Movement)", font_size=20, color=WHITE),
            Text("- Grippers (Manipulation)", font_size=20, color=WHITE),
            Text("- Speakers (Sound)", font_size=20, color=WHITE),
            Text("- Wheels (Locomotion)", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(robot_actuators_label, DOWN, buff=0.2)

        self.play(
            Write(robot_agent_box_label), Create(robot_agent_box),
            Write(robot_sensors_label), Write(robot_sensors_list),
            Write(robot_actuators_label), Write(robot_actuators_list)
        )
        self.wait(2)

        # Arrows for robot interaction
        robot_env_label = Text("Environment", font_size=24, color=BLUE).next_to(robot_sensors_list, LEFT, buff=1.0)
        robot_env_arrow_to_sensors = Arrow(robot_env_label.get_right(), robot_sensors_list.get_left(), buff=0.2, max_tip_length_to_length_ratio=0.1)
        robot_sensors_arrow_to_agent = Arrow(robot_sensors_list.get_right(), robot_agent_box.get_left(), buff=0.2, max_tip_length_to_length_ratio=0.1)
        robot_agent_arrow_to_actuators = Arrow(robot_agent_box.get_right(), robot_actuators_list.get_left(), buff=0.2, max_tip_length_to_length_ratio=0.1)
        
        # Curved arrow for robot feedback
        p_r1 = robot_actuators_list.get_right() + RIGHT * 0.2
        p_r2 = robot_actuators_list.get_right() + RIGHT * 1.0 + DOWN * 0.5
        p_r3 = robot_env_label.get_right() + RIGHT * 1.0 + DOWN * 0.5
        p_r4 = robot_env_label.get_right() + RIGHT * 0.2

        robot_curved_segment1 = Line(p_r1, p_r2, color=RED)
        robot_curved_segment2 = Line(p_r2, p_r3, color=RED)
        robot_curved_segment3 = Arrow(p_r3, p_r4, color=RED)

        self.play(
            Write(robot_env_label),
            Create(robot_env_arrow_to_sensors),
            Create(robot_sensors_arrow_to_agent),
            Create(robot_agent_arrow_to_actuators),
            Create(robot_curved_segment1), Create(robot_curved_segment2), Create(robot_curved_segment3)
        )
        self.wait(3)

        self.play(
            FadeOut(title_text),
            FadeOut(robot_agent_box_label), FadeOut(robot_agent_box),
            FadeOut(robot_sensors_label), FadeOut(robot_sensors_list),
            FadeOut(robot_actuators_label), FadeOut(robot_actuators_list),
            FadeOut(robot_env_label), FadeOut(robot_env_arrow_to_sensors),
            FadeOut(robot_sensors_arrow_to_agent), FadeOut(robot_agent_arrow_to_actuators),
            FadeOut(robot_curved_segment1), FadeOut(robot_curved_segment2), FadeOut(robot_curved_segment3)
        )
        self.wait(1)