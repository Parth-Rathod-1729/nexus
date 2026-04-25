import manim
from manim import *

class Scene1(Scene):
    def construct(self):
        # Title and Definition
        title = Text("Defining the AI Agent", color=WHITE).scale(0.8).to_edge(UP)
        definition = Text(
            "Autonomous system: perceives, decides, acts.", 
            font_size=24, color=WHITE
        ).to_edge(DOWN)

        # Agent Block
        agent_box = Rectangle(width=3, height=1.5, color=BLUE, fill_opacity=0.3)
        agent_box.move_to(UP * 1)
        agent_text = Text("Agent", color=BLUE).scale(0.7).move_to(agent_box.get_center())
        agent_group = VGroup(agent_box, agent_text)

        # Environment Block
        env_box = Rectangle(width=5, height=1.2, color=GREEN, fill_opacity=0.3)
        env_box.move_to(DOWN * 2)
        env_text = Text("Environment", color=GREEN).scale(0.7).move_to(env_box.get_center())
        env_group = VGroup(env_box, env_text)

        # Sensor Path (Environment -> Agent)
        sensor_arrow = Arrow(
            start=env_box.get_top() + LEFT * 1.5, 
            end=agent_box.get_bottom() + LEFT * 1.5, 
            color=TEAL, 
            stroke_width=4
        )
        sensor_label = Text("Sensors", color=TEAL, font_size=20).next_to(sensor_arrow, LEFT)

        # Actuator Path (Agent -> Environment)
        actuator_arrow = Arrow(
            start=agent_box.get_bottom() + RIGHT * 1.5, 
            end=env_box.get_top() + RIGHT * 1.5, 
            color=GOLD, 
            stroke_width=4
        )
        actuator_label = Text("Actuators", color=GOLD, font_size=20).next_to(actuator_arrow, RIGHT)

        # Animation Sequence
        self.play(Write(title))
        self.play(Create(agent_group), Create(env_group))
        self.wait(1)

        # Sensors Step
        self.play(
            Create(sensor_arrow),
            Write(sensor_label),
            run_time=1.5
        )
        
        # Perception/Decision indicator
        decision_dot = Dot(color=YELLOW).move_to(agent_box.get_center())
        self.play(Flash(decision_dot, color=YELLOW, flash_radius=0.5))

        # Actuators Step
        self.play(
            Create(actuator_arrow),
            Write(actuator_label),
            run_time=1.5
        )

        self.play(Write(definition))
        self.wait(2)

        # Final loop cleanup (optional)
        self.play(
            Indicate(agent_group, color=BLUE),
            Indicate(env_group, color=GREEN),
            run_time=2
        )
        self.wait(1)