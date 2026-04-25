from manim import *
from manim import Color # Explicitly import Color

# Define BROWN explicitly if it's not being imported correctly by `from manim import *`
# Manim's default BROWN is #8B4513
BROWN = Color("#8B4513")

class Scene3(Scene):
    def construct(self):
        # --- 1. Title ---
        title = Text("An Agent in Action: Vacuum-Cleaner World", font_size=40, color=BLUE_C)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # --- 2. Vacuum-Cleaner World (Squares A & B) ---
        square_A_label = Text("A", font_size=28, color=WHITE)
        square_A = Square(side_length=2, fill_opacity=0.1, fill_color=GRAY_A, color=BLUE_E)
        square_A_label.move_to(square_A.get_center())
        location_A = VGroup(square_A, square_A_label)

        square_B_label = Text("B", font_size=28, color=WHITE)
        square_B = Square(side_length=2, fill_opacity=0.1, fill_color=GRAY_A, color=BLUE_E)
        square_B_label.move_to(square_B.get_center())
        location_B = VGroup(square_B, square_B_label)

        world = VGroup(location_A, location_B).arrange(RIGHT, buff=1.5)
        world.move_to(ORIGIN)

        self.play(Create(world))
        self.wait(0.5)

        # --- 3. Create the "Vacuum Cleaner" Mobject ---
        vac_body = Square(side_length=0.8, color=BLUE_E, fill_color=BLUE_E, fill_opacity=0.8)
        vac_wheel_left = Circle(radius=0.15, color=GOLD_C, fill_color=GOLD_C, fill_opacity=1).next_to(vac_body, DOWN + LEFT, buff=0.05)
        vac_wheel_right = Circle(radius=0.15, color=GOLD_C, fill_color=GOLD_C, fill_opacity=1).next_to(vac_body, DOWN + RIGHT, buff=0.05)
        vac_handle = Line(vac_body.get_top(), vac_body.get_top() + UP * 0.5 + RIGHT * 0.3, color=TEAL_C, stroke_width=4)
        vac_brush = Rectangle(width=0.8, height=0.2, color=GRAY_A, fill_color=GRAY_A, fill_opacity=1).next_to(vac_body, DOWN, buff=0)
        
        vacuum_cleaner = VGroup(vac_body, vac_wheel_left, vac_wheel_right, vac_handle, vac_brush)
        vacuum_cleaner.scale(0.8).move_to(square_A.get_center() + UP * 0.2) # Adjusted position to be slightly above the center
        
        self.play(FadeIn(vacuum_cleaner))
        self.wait(1)

        # --- 4. Illustrate Percepts & Actions ---

        # Phase 1: Agent perceives dirt in A and Sucks.
        dirt_dots = VGroup(
            Dot(radius=0.1, color=BROWN, fill_opacity=1).shift(DR * 0.3),
            Dot(radius=0.08, color=BROWN, fill_opacity=1).shift(UL * 0.2 + RIGHT * 0.1),
            Dot(radius=0.09, color=BROWN, fill_opacity=1).shift(DL * 0.1 + LEFT * 0.2)
        ).move_to(square_A.get_center())

        self.play(FadeIn(dirt_dots))
        self.wait(0.5)

        percept_text_1 = Text("Percept: (A, Dirty)", font_size=28, color=GREEN_C).next_to(world, DOWN, buff=0.8).shift(LEFT*2)
        action_text_1 = Text("Action: Suck", font_size=28, color=GOLD_C).next_to(percept_text_1, RIGHT, buff=1.5)
        
        self.play(Write(percept_text_1))
        self.wait(1)
        self.play(Write(action_text_1))
        self.wait(1)
        self.play(FadeOut(dirt_dots), FadeOut(vacuum_cleaner[4], shift=DOWN*0.2)) # Fade out brush to simulate sucking
        self.add(vacuum_cleaner[4]) # Re-add brush to mobjects for subsequent animations without a new `Create`
        self.play(FadeIn(vacuum_cleaner[4], shift=UP*0.2)) # Fade in brush back
        self.wait(0.5)

        # Update percept text
        percept_text_1_clean = Text("Percept: (A, Clean)", font_size=28, color=GREEN_C).move_to(percept_text_1)
        self.play(Transform(percept_text_1, percept_text_1_clean), FadeOut(action_text_1))
        self.wait(1)

        # Phase 2: Agent perceives clean in A and Moves to B.
        action_text_2 = Text("Action: Right", font_size=28, color=GOLD_C).next_to(percept_text_1, RIGHT, buff=1.5)
        self.play(Write(action_text_2))
        self.wait(1)
        self.play(
            vacuum_cleaner.animate.move_to(square_B.get_center() + UP * 0.2),
            FadeOut(percept_text_1),
            FadeOut(action_text_2)
        )
        self.wait(0.5)

        # Update percept text for location B
        percept_text_2 = Text("Percept: (B, Clean)", font_size=28, color=GREEN_C).next_to(world, DOWN, buff=0.8).shift(LEFT*2)
        self.play(Write(percept_text_2))
        self.wait(1)

        # Phase 3: Agent on B, perceives clean, moves back to A.
        action_text_3 = Text("Action: Left", font_size=28, color=GOLD_C).next_to(percept_text_2, RIGHT, buff=1.5)
        self.play(Write(action_text_3))
        self.wait(1)
        self.play(
            vacuum_cleaner.animate.move_to(square_A.get_center() + UP * 0.2),
            FadeOut(percept_text_2),
            FadeOut(action_text_3)
        )
        self.wait(1)

        self.play(FadeOut(world), FadeOut(vacuum_cleaner))
        self.wait(0.5)

        # --- 5. Represent the Agent Function (If-Then Rule) ---
        agent_func_title = Text("Agent Function", font_size=36, color=TEAL_A)
        
        # Rule 1: If Dirty, Suck
        if_dirty_text = Text("IF Percept == (Location, Dirty)", font_size=28, color=WHITE)
        then_suck_text = Text("THEN Action = Suck", font_size=28, color=WHITE)
        
        rule1_contents = VGroup(if_dirty_text, then_suck_text).arrange(DOWN, buff=0.4)
        rule1_box = Rectangle(
            width=if_dirty_text.width + 1.5,
            height=if_dirty_text.height + then_suck_text.height + 1.2,
            color=TEAL_A, fill_color=TEAL_D, fill_opacity=0.6
        ).surround(rule1_contents, stretch=True)
        rule1_label = Text("Rule 1", font_size=24, color=WHITE).next_to(rule1_box, UP, buff=0.2)
        rule1_group = VGroup(rule1_box, rule1_contents, rule1_label)

        # Rule 2: Else (Clean), Move
        else_clean_text = Text("ELSE (Percept == (Location, Clean))", font_size=28, color=WHITE)
        then_move_text = Text("THEN Action = Move to Other Square", font_size=28, color=WHITE)

        rule2_contents = VGroup(else_clean_text, then_move_text).arrange(DOWN, buff=0.4)
        rule2_box = Rectangle(
            width=else_clean_text.width + 1.5,
            height=else_clean_text.height + then_move_text.height + 1.2,
            color=TEAL_A, fill_color=TEAL_D, fill_opacity=0.6
        ).surround(rule2_contents, stretch=True)
        rule2_label = Text("Rule 2", font_size=24, color=WHITE).next_to(rule2_box, UP, buff=0.2)
        rule2_group = VGroup(rule2_box, rule2_contents, rule2_label)

        # Arrange the rules
        agent_function_rules = VGroup(rule1_group, rule2_group).arrange(DOWN, buff=0.8)
        
        # Adjust position relative to the title
        agent_func_title.next_to(title, DOWN, buff=0.8) # Adjust agent_func_title to be below the main title
        agent_function_rules.next_to(agent_func_title, DOWN, buff=0.8) # Adjust rules to be below agent_func_title

        self.play(FadeOut(title)) # Fade out main title to make space
        self.play(Write(agent_func_title))
        self.play(Create(rule1_group), Create(rule2_group))
        self.wait(2)

        self.play(FadeOut(agent_func_title), FadeOut(agent_function_rules))
        self.wait(1)