from manim import *

class Scene2(Scene):
    def construct(self):
        # Define a distinct, vibrant color palette
        BLUE = "#3F88C5"  # A vibrant blue
        GREEN = "#2B9348"  # A vibrant green
        TEAL = "#28B4C6"  # A vibrant teal
        GOLD = "#FFC300"  # A vibrant gold
        WHITE = "#F8F8F8" # A soft white for text

        # 1. Title
        title = Text("How AI Agents Interact: Percepts, Sensors, Actuators", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 2. Core Diagram: Environment <-> AI Agent <-> Environment (Actions)
        # Boxes for Environment, AI Agent, and Actions
        env_box = Square(side_length=3, color=BLUE, fill_opacity=0.2)
        env_text = Text("Environment", font_size=28, color=BLUE).next_to(env_box, UP, buff=0.2)
        environment_group = VGroup(env_box, env_text)

        agent_box = Square(side_length=3, color=GOLD, fill_opacity=0.2)
        agent_text = Text("AI Agent", font_size=28, color=GOLD).next_to(agent_box, UP, buff=0.2)
        agent_group = VGroup(agent_box, agent_text)

        actions_box = Square(side_length=3, color=BLUE, fill_opacity=0.2)
        actions_text = Text("Environment\n(Actions)", font_size=28, color=BLUE).next_to(actions_box, UP, buff=0.2)
        actions_group = VGroup(actions_box, actions_text)

        # Arrange the main boxes horizontally
        main_diagram_elements = VGroup(environment_group, agent_group, actions_group).arrange(RIGHT, buff=2.0).shift(DOWN*0.5)
        
        self.play(
            Create(env_box), Write(env_text),
            Create(agent_box), Write(agent_text),
            Create(actions_box), Write(actions_text)
        )
        self.wait(0.5)

        # Sensors and Percepts (Environment -> Agent)
        sensor_arrow = Arrow(env_box.get_right(), agent_box.get_left(), buff=0.1, color=GREEN, stroke_width=5)
        sensor_label = Text("Sensors", font_size=24, color=GREEN).next_to(sensor_arrow, UP, buff=0.2)
        percepts_label = Text("Percepts", font_size=20, color=TEAL).next_to(sensor_arrow, DOWN, buff=0.2)

        # Simplified Sensor Icons (Camera, Microphone) using basic mobjects
        camera_body = Square(side_length=0.4, color=GREEN, fill_opacity=1)
        camera_lens = Circle(radius=0.15, color=TEAL, fill_opacity=1).move_to(camera_body.get_center() + 0.05 * RIGHT)
        camera_icon = VGroup(camera_body, camera_lens)

        mic_body = Rectangle(width=0.3, height=0.6, color=GREEN, fill_opacity=1)
        mic_top = Circle(radius=0.15, color=TEAL, fill_opacity=1).next_to(mic_body, UP, buff=0)
        microphone_icon = VGroup(mic_body, mic_top)

        sensor_icons = VGroup(camera_icon, microphone_icon).arrange(RIGHT, buff=0.5).scale(0.8)
        sensor_icons.move_to(sensor_arrow.get_center()).shift(UP * 0.8) # Position icons above the arrow
        
        self.play(Create(sensor_arrow), Write(sensor_label))
        self.play(Write(percepts_label), Create(sensor_icons))
        self.wait(1)

        # Actuators and Actions (Agent -> Environment)
        actuator_arrow = Arrow(agent_box.get_right(), actions_box.get_left(), buff=0.1, color=GOLD, stroke_width=5)
        actuator_label = Text("Actuators", font_size=24, color=GOLD).next_to(actuator_arrow, UP, buff=0.2)
        actions_result_label = Text("Actions", font_size=20, color=TEAL).next_to(actuator_arrow, DOWN, buff=0.2)

        # Simplified Actuator Icons (Robot Arm, Wheel) using basic mobjects
        arm_segment1 = Rectangle(width=0.6, height=0.2, color=GOLD, fill_opacity=1).rotate(PI / 4)
        arm_segment2 = Rectangle(width=0.6, height=0.2, color=TEAL, fill_opacity=1).next_to(arm_segment1, UL, buff=0.05).rotate(-PI / 4)
        robot_arm_icon = VGroup(arm_segment1, arm_segment2)

        wheel_circle = Circle(radius=0.3, color=GOLD, fill_opacity=1)
        wheel_spoke1 = Line(wheel_circle.get_center(), wheel_circle.point_at_angle(PI/4), color=TEAL, stroke_width=2)
        wheel_spoke2 = Line(wheel_circle.get_center(), wheel_circle.point_at_angle(3*PI/4), color=TEAL, stroke_width=2)
        wheel_icon = VGroup(wheel_circle, wheel_spoke1, wheel_spoke2) # Simplified wheel with fewer spokes

        actuator_icons = VGroup(robot_arm_icon, wheel_icon).arrange(RIGHT, buff=0.5).scale(0.8)
        actuator_icons.move_to(actuator_arrow.get_center()).shift(UP * 0.8) # Position icons above the arrow

        self.play(Create(actuator_arrow), Write(actuator_label))
        self.play(Write(actions_result_label), Create(actuator_icons))
        self.wait(2)

        # Fade out core diagram components
        core_diagram_mobjects = VGroup(
            environment_group, agent_group, actions_group,
            sensor_arrow, sensor_label, percepts_label, sensor_icons,
            actuator_arrow, actuator_label, actions_result_label, actuator_icons
        )
        self.play(FadeOut(core_diagram_mobjects))
        self.wait(0.5)

        # 3. Examples for different agent types (Human, Robot, Software)
        # Helper function to create an example block with clear layout
        def create_example_block(agent_type_str, sensors_str, actuators_str):
            agent_title_text = Text(agent_type_str, font_size=28, color=GOLD)
            
            sensors_display_text = Text(f"Sensors: {sensors_str}", font_size=20, color=GREEN)
            actuators_display_text = Text(f"Actuators: {actuators_str}", font_size=20, color=BLUE)
            
            # Group content that goes inside the box
            content_inside_box = VGroup(sensors_display_text, actuators_display_text).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            
            # Create a frame around the content, ensuring proper padding
            padding_horizontal = 0.6
            padding_vertical = 0.4
            frame = Rectangle(
                width=content_inside_box.width + padding_horizontal,
                height=content_inside_box.height + padding_vertical,
                color=WHITE,
                fill_opacity=0.1
            )
            
            # Position the frame below the agent title
            frame.next_to(agent_title_text, DOWN, buff=0.3)
            # Center the content within the frame
            content_inside_box.move_to(frame.get_center()) 
            
            return VGroup(agent_title_text, frame, content_inside_box)

        # Create example blocks for Human, Robot, and Software agents
        human_block = create_example_block(
            "Human Agent",
            "Eyes, Ears, Skin (Senses)",
            "Hands, Legs, Mouth (Limbs)"
        )

        robot_block = create_example_block(
            "Robot Agent",
            "Cameras, Microphones, Sonar (Input)",
            "Motors, Wheels, Grippers (Output)"
        )

        software_block = create_example_block(
            "Software Agent",
            "Keyboard Input, Network Packets (Data)",
            "Screen Output, Network Messages (Actions)"
        )
        
        # Arrange example blocks horizontally with breathable spacing
        example_group = VGroup(human_block, robot_block, software_block).arrange(RIGHT, buff=1.0).center()
        
        # Animate the appearance of each example block with a lagged start
        self.play(LaggedStart(*[FadeIn(block) for block in example_group], lag_ratio=0.5))
        self.wait(3)

        # Fade out all mobjects at the end of the scene
        self.play(FadeOut(title), FadeOut(example_group))
        self.wait(1)