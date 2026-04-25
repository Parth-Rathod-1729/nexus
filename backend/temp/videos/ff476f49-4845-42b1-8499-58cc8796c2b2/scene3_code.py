import manim as mn

class Scene3(mn.Scene):
    def construct(self):
        # --- Color Palette ---
        BLUE = mn.BLUE_C
        GREEN = mn.GREEN_C
        TEAL = mn.TEAL_C
        GOLD = mn.GOLD_C
        RED = mn.RED_C
        YELLOW = mn.YELLOW_C
        GRAY_BROWN = mn.ManimColor("#8B4513") # A custom color for dirt

        # --- Title ---
        title_text = mn.Text("Defining Agent Behavior: Agent Function & Program", font_size=48, color=BLUE)
        title_text.to_edge(mn.UP)
        self.play(mn.Write(title_text))
        self.wait(0.5)

        # --- Agent Function Explanation ---
        agent_func_title = mn.Text("The Agent Function", font_size=36, color=GOLD)
        agent_func_title.next_to(title_text, mn.DOWN, buff=1.0)
        
        agent_func_def1 = mn.Text("Maps every possible percept sequence to an action.", font_size=28)
        agent_func_def1.next_to(agent_func_title, mn.DOWN, buff=0.4).align_to(agent_func_title, mn.LEFT)
        
        agent_func_def2 = mn.Text("Abstract & often impractical to tabulate.", font_size=28)
        agent_func_def2.next_to(agent_func_def1, mn.DOWN, buff=0.3).align_to(agent_func_title, mn.LEFT)
        
        agent_func_group = mn.VGroup(agent_func_title, agent_func_def1, agent_func_def2)
        self.play(mn.FadeIn(agent_func_title, shift=mn.UP))
        self.play(mn.Write(agent_func_def1))
        self.play(mn.Write(agent_func_def2))
        self.wait(1)

        # --- Agent Program Explanation ---
        agent_prog_title = mn.Text("The Agent Program", font_size=36, color=TEAL)
        agent_prog_title.next_to(agent_func_def2, mn.DOWN, buff=1.0).align_to(agent_func_title, mn.LEFT)
        
        agent_prog_def1 = mn.Text("Internally implements the agent function.", font_size=28)
        agent_prog_def1.next_to(agent_prog_title, mn.DOWN, buff=0.4).align_to(agent_func_title, mn.LEFT)
        
        agent_prog_def2 = mn.Text("Concrete code running on a physical system.", font_size=28)
        agent_prog_def2.next_to(agent_prog_def1, mn.DOWN, buff=0.3).align_to(agent_func_title, mn.LEFT)
        
        agent_prog_group = mn.VGroup(agent_prog_title, agent_prog_def1, agent_prog_def2)
        self.play(mn.FadeIn(agent_prog_title, shift=mn.UP))
        self.play(mn.Write(agent_prog_def1))
        self.play(mn.Write(agent_prog_def2))
        self.wait(2)

        # --- Transition to Vacuum World Example ---
        all_intro_text = mn.VGroup(title_text, agent_func_group, agent_prog_group)
        self.play(mn.FadeOut(all_intro_text))

        vac_title = mn.Text("Vacuum-Cleaner World Example", font_size=40, color=BLUE)
        vac_title.to_edge(mn.UP)
        self.play(mn.Write(vac_title))
        self.wait(0.5)

        # --- Build Vacuum-Cleaner World Environment ---
        square_A = mn.Square(side_length=2.0, color=BLUE, fill_opacity=0.2)
        label_A = mn.Text("A", font_size=30, color=BLUE).move_to(square_A.get_center())
        
        square_B = mn.Square(side_length=2.0, color=GREEN, fill_opacity=0.2)
        label_B = mn.Text("B", font_size=30, color=GREEN).move_to(square_B.get_center())

        # Arrange squares horizontally
        world_env = mn.VGroup(square_A, square_B).arrange(mn.RIGHT, buff=1.5).center()
        label_A.move_to(square_A.get_center())
        label_B.move_to(square_B.get_center())
        
        self.play(mn.Create(square_A), mn.Write(label_A),
                  mn.Create(square_B), mn.Write(label_B))
        self.wait(0.5)

        # --- Vacuum Agent Mobject ---
        vac_body = mn.Rectangle(width=0.8, height=0.6, color=TEAL, fill_opacity=1.0)
        vac_head = mn.Triangle(color=TEAL, fill_opacity=1.0).scale(0.3).rotate(mn.PI/2) # Pointing up
        vac_head.next_to(vac_body, mn.UP, buff=0)
        vac_wheels = mn.VGroup(
            mn.Circle(radius=0.1, color=TEAL, fill_opacity=1.0).next_to(vac_body, mn.DOWN + mn.LEFT, buff=0.05),
            mn.Circle(radius=0.1, color=TEAL, fill_opacity=1.0).next_to(vac_body, mn.DOWN + mn.RIGHT, buff=0.05)
        )
        vac_agent = mn.VGroup(vac_body, vac_head, vac_wheels).move_to(square_A.get_center() + mn.DOWN*0.2) # Adjusted slightly
        
        self.play(mn.FadeIn(vac_agent))
        self.wait(1)

        # --- Agent Function Rule Text ---
        agent_func_rule = mn.MathTex(r"\text{Percept (Location, Dirt Status)} \rightarrow \text{Action}", font_size=32, color=GOLD)
        agent_func_rule.to_edge(mn.LEFT).shift(mn.UP*2)
        self.play(mn.Write(agent_func_rule))
        self.wait(0.5)

        example_rule_text = mn.VGroup(
            mn.Text("If (Location, DIRTY) then Suck", font_size=24, color=RED),
            mn.Text("Else if Location == A then Right", font_size=24, color=RED),
            mn.Text("Else if Location == B then Left", font_size=24, color=RED)
        ).arrange(mn.DOWN, buff=0.3).next_to(agent_func_rule, mn.DOWN, buff=0.5).align_to(agent_func_rule, mn.LEFT)
        
        self.play(mn.LaggedStart(*[mn.Write(line) for line in example_rule_text], lag_ratio=0.3))
        self.wait(1.5)

        # --- Vacuum World Simulation ---
        percept_action_display = mn.VGroup()

        # Dirt at A
        dirt_A = mn.Circle(radius=0.2, color=GRAY_BROWN, fill_opacity=1.0).move_to(square_A.get_center() + mn.DOWN*0.5 + mn.LEFT*0.5)
        self.play(mn.FadeIn(dirt_A, scale=0.5))
        self.wait(0.5)
        
        current_percept_A = mn.Text("Percept: (A, Dirty)", font_size=24, color=YELLOW)
        current_action_A = mn.Text("Action: Suck", font_size=24, color=RED)
        percept_action_display = mn.VGroup(current_percept_A, current_action_A).arrange(mn.DOWN, buff=0.2).next_to(vac_title, mn.DOWN, buff=0.5).to_edge(mn.RIGHT)
        
        self.play(mn.Write(current_percept_A))
        self.play(mn.Write(current_action_A))
        self.wait(1)
        self.play(mn.FadeOut(dirt_A, scale=0.5), run_time=1)
        self.play(mn.FadeOut(percept_action_display))
        self.wait(0.5)

        # Move from A to B (A is clean)
        current_percept_clean_A = mn.Text("Percept: (A, Clean)", font_size=24, color=YELLOW)
        current_action_move_B = mn.Text("Action: Right", font_size=24, color=RED)
        percept_action_display = mn.VGroup(current_percept_clean_A, current_action_move_B).arrange(mn.DOWN, buff=0.2).next_to(vac_title, mn.DOWN, buff=0.5).to_edge(mn.RIGHT)
        
        self.play(mn.Write(current_percept_clean_A))
        self.play(mn.Write(current_action_move_B))
        self.play(vac_agent.animate.move_to(square_B.get_center() + mn.DOWN*0.2), run_time=1.5)
        self.play(mn.FadeOut(percept_action_display))
        self.wait(0.5)

        # Dirt at B
        dirt_B = mn.Circle(radius=0.2, color=GRAY_BROWN, fill_opacity=1.0).move_to(square_B.get_center() + mn.DOWN*0.5 + mn.RIGHT*0.5)
        self.play(mn.FadeIn(dirt_B, scale=0.5))
        self.wait(0.5)

        current_percept_B = mn.Text("Percept: (B, Dirty)", font_size=24, color=YELLOW)
        current_action_B = mn.Text("Action: Suck", font_size=24, color=RED)
        percept_action_display = mn.VGroup(current_percept_B, current_action_B).arrange(mn.DOWN, buff=0.2).next_to(vac_title, mn.DOWN, buff=0.5).to_edge(mn.RIGHT)
        
        self.play(mn.Write(current_percept_B))
        self.play(mn.Write(current_action_B))
        self.wait(1)
        self.play(mn.FadeOut(dirt_B, scale=0.5), run_time=1)
        self.play(mn.FadeOut(percept_action_display))
        self.wait(0.5)

        # Move from B to A (B is clean)
        current_percept_clean_B = mn.Text("Percept: (B, Clean)", font_size=24, color=YELLOW)
        current_action_move_A = mn.Text("Action: Left", font_size=24, color=RED)
        percept_action_display = mn.VGroup(current_percept_clean_B, current_action_move_A).arrange(mn.DOWN, buff=0.2).next_to(vac_title, mn.DOWN, buff=0.5).to_edge(mn.RIGHT)
        
        self.play(mn.Write(current_percept_clean_B))
        self.play(mn.Write(current_action_move_A))
        self.play(vac_agent.animate.move_to(square_A.get_center() + mn.DOWN*0.2), run_time=1.5)
        self.play(mn.FadeOut(percept_action_display))
        self.wait(1)

        # --- Transition to Agent Program Pseudo-code ---
        self.play(mn.FadeOut(mn.VGroup(square_A, label_A, square_B, label_B, vac_agent, agent_func_rule, example_rule_text)))
        self.wait(0.5)
        
        agent_prog_code_title = mn.Text("Agent Program (Simplified Pseudo-code)", font_size=36, color=TEAL)
        agent_prog_code_title.next_to(vac_title, mn.DOWN, buff=1.0)
        self.play(mn.Write(agent_prog_code_title))
        self.wait(0.5)

        code_lines = mn.VGroup(
            mn.MathTex(r"\text{function VACUUM-AGENT(percept)}", font_size=28, color=BLUE),
            mn.MathTex(r"\quad \text{persistent: last\_action, location}", font_size=28, color=GREEN),
            mn.MathTex(r"\quad \text{location, status} \leftarrow \text{percept}", font_size=28, color=TEAL),
            mn.MathTex(r"\quad \text{if status == DIRTY then return SUCK}", font_size=28, color=GOLD),
            mn.MathTex(r"\quad \text{else if location == A then return RIGHT}", font_size=28, color=RED),
            mn.MathTex(r"\quad \text{else if location == B then return LEFT}", font_size=28, color=RED),
        ).arrange(mn.DOWN, buff=0.4).next_to(agent_prog_code_title, mn.DOWN, buff=0.8).align_to(agent_prog_code_title, mn.LEFT)

        self.play(mn.LaggedStart(*[mn.Write(line) for line in code_lines], lag_ratio=0.3))
        self.wait(3)

        # --- Final Fade Out ---
        self.play(mn.FadeOut(vac_title, agent_prog_code_title, code_lines))
        self.wait(1)