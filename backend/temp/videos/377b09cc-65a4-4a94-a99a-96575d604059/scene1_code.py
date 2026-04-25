from manim import *

class Scene1(Scene):
    def construct(self):
        # --- 1. Title ---
        title = Text("What is an AI Agent?", font_size=48, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # --- 2. Define Mobjects for the Diagram ---

        # Environment Blocks
        env_L_text = Text("Environment", font_size=30, color=GREEN)
        env_R_text = Text("Environment", font_size=30, color=GREEN)

        # Sensors Block with Icon
        # Using a Square for the sensor body and a Line for the "beam" or input
        sensor_body = Square(side_length=0.3, color=BLUE, fill_opacity=0.6, stroke_width=2)
        sensor_beam = Line(sensor_body.get_right(), sensor_body.get_right() + RIGHT * 0.3, color=BLUE, stroke_width=3)
        sensor_icon = VGroup(sensor_body, sensor_beam).move_to(ORIGIN) # Center icon for arrangement
        sensors_text_obj = Text("Sensors", font_size=30, color=BLUE)
        sensors_full_group = VGroup(sensor_icon, sensors_text_obj).arrange(DOWN, buff=0.2)

        # Actuators Block with Icon
        # Using Lines for an arm-like structure and a Square for a gripper/tool
        actuator_arm_segment1 = Line(ORIGIN, UP * 0.3, color=BLUE, stroke_width=3)
        actuator_arm_segment2 = Line(actuator_arm_segment1.get_end(), actuator_arm_segment1.get_end() + RIGHT * 0.3, color=BLUE, stroke_width=3)
        actuator_gripper = Square(side_length=0.2, color=BLUE, fill_opacity=0.6, stroke_width=2).next_to(actuator_arm_segment2.get_end(), RIGHT, buff=0).shift(LEFT*0.1) # Position gripper near arm end
        actuator_icon = VGroup(actuator_arm_segment1, actuator_arm_segment2, actuator_gripper).rotate(PI/4).move_to(ORIGIN) # Rotate and center
        actuators_text_obj = Text("Actuators", font_size=30, color=BLUE)
        actuators_full_group = VGroup(actuator_icon, actuators_text_obj).arrange(DOWN, buff=0.2)

        # Agent Block (Core) with internal components and Brain Icon
        agent_box = Square(side_length=2.5, color=TEAL, fill_opacity=0.2, stroke_width=2)
        agent_label = Text("AGENT", font_size=30, color=TEAL).next_to(agent_box, UP, buff=0.3)
        
        # Brain icon for "Brain / Model": A circle with some waves inside to suggest brain folds
        brain_outline = Circle(radius=0.2, color=GOLD, stroke_width=2)
        brain_wave1 = Line(brain_outline.point_at_angle(PI*0.7), brain_outline.point_at_angle(PI*0.3), color=GOLD)
        brain_wave2 = Line(brain_outline.point_at_angle(PI*1.3), brain_outline.point_at_angle(PI*1.7), color=GOLD)
        brain_icon = VGroup(brain_outline, brain_wave1, brain_wave2).scale(0.8) # Adjust scale to fit well
        
        brain_model_text = Text("Brain / Model", font_size=24, color=GOLD)
        brain_model_group = VGroup(brain_icon, brain_model_text).arrange(LEFT, buff=0.2) # Icon to the left of text

        memory_text = Text("Memory", font_size=24, color=GREEN)
        
        agent_internal_components = VGroup(brain_model_group, memory_text).arrange(DOWN, buff=0.3)
        agent_internal_components.move_to(agent_box.get_center())
        
        agent_full_group = VGroup(agent_label, agent_box, agent_internal_components)

        # --- 3. Arrange all main diagram elements horizontally ---
        # Temporarily create a VGroup for initial arrangement
        temp_diagram_arrangement = VGroup(
            env_L_text,
            sensors_full_group,
            agent_full_group,
            actuators_full_group,
            env_R_text
        ).arrange(RIGHT, buff=0.8)
        
        # Adjust env texts to be vertically aligned with their neighboring groups for cleaner arrow connections
        env_L_text.align_to(sensors_full_group, UP) 
        env_R_text.align_to(actuators_full_group, UP) 
        
        # Re-create the VGroup with adjusted positions and center it
        diagram_elements = VGroup(
            env_L_text,
            sensors_full_group,
            agent_full_group,
            actuators_full_group,
            env_R_text
        ).arrange(RIGHT, buff=0.8).move_to(ORIGIN)


        # --- 4. Create Arrows for the flow ---
        arrow_color = WHITE
        arrow_stroke = 4

        # Environment (Left) -> Sensors (Perception)
        env_L_to_sensors_arrow = Arrow(
            env_L_text.get_right(), sensors_full_group.get_left(),
            buff=0.1, color=arrow_color, stroke_width=arrow_stroke
        )

        # Sensors -> Agent (Input to brain)
        sensors_to_agent_arrow = Arrow(
            sensors_full_group.get_right(), agent_box.get_left(),
            buff=0.1, color=arrow_color, stroke_width=arrow_stroke
        )

        # Agent -> Actuators (Output from brain)
        agent_to_actuators_arrow = Arrow(
            agent_box.get_right(), actuators_full_group.get_left(),
            buff=0.1, color=arrow_color, stroke_width=arrow_stroke
        )

        # Actuators -> Environment (Right) (Action affecting environment)
        actuators_to_env_R_arrow = Arrow(
            actuators_full_group.get_right(), env_R_text.get_left(),
            buff=0.1, color=arrow_color, stroke_width=arrow_stroke
        )

        # Feedback loop: Environment (Right) -> Environment (Left) / Sensors
        # This arrow represents the modified environment providing new input for the next cycle
        path_start = env_R_text.get_bottom()
        # Create points for a path that goes down, across, and then up to the sensors
        path_corner1 = path_start + DOWN * 0.8
        path_corner2 = sensors_full_group.get_bottom() + DOWN * 0.8
        path_end = sensors_full_group.get_bottom()

        # Create lines for the path, and an arrow head for the final segment
        feedback_path_segment1 = Line(path_start, path_corner1, color=arrow_color, stroke_width=arrow_stroke)
        feedback_path_segment2 = Line(path_corner1, path_corner2, color=arrow_color, stroke_width=arrow_stroke)
        feedback_arrow_segment = Arrow(path_corner2, path_end, color=arrow_color, stroke_width=arrow_stroke, tip_length=0.25)
        
        feedback_loop_group = VGroup(
            feedback_path_segment1, 
            feedback_path_segment2, 
            feedback_arrow_segment
        )

        # --- 5. Animations ---
        self.play(Create(env_L_text))
        self.play(Create(sensors_full_group))
        self.play(GrowArrow(env_L_to_sensors_arrow))
        self.wait(0.5)

        self.play(
            Create(agent_box),
            Write(agent_label),
            Write(agent_internal_components)
        )
        self.play(GrowArrow(sensors_to_agent_arrow))
        self.wait(0.5)

        self.play(Create(actuators_full_group))
        self.play(GrowArrow(agent_to_actuators_arrow))
        self.wait(0.5)

        self.play(Create(env_R_text))
        self.play(GrowArrow(actuators_to_env_R_arrow))
        self.wait(1)

        # Animate the feedback loop
        self.play(
            Create(feedback_path_segment1),
            Create(feedback_path_segment2),
            GrowArrow(feedback_arrow_segment)
        )
        self.wait(2)

        # Group all diagram elements for fading out
        full_diagram = VGroup(
            env_L_text, sensors_full_group, env_L_to_sensors_arrow,
            agent_full_group, sensors_to_agent_arrow,
            actuators_full_group, agent_to_actuators_arrow,
            env_R_text, actuators_to_env_R_arrow,
            feedback_loop_group
        )
        
        self.play(FadeOut(full_diagram), FadeOut(title))
        self.wait(1)