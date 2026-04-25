from manim import *

class Scene1(Scene):
    def construct(self):
        # --- Colors ---
        BLUE_ACCENT = BLUE_E
        GREEN_ACCENT = GREEN_E
        TEAL_ACCENT = TEAL_E
        GOLD_ACCENT = GOLD_E
        RED_ACCENT = RED_E
        GREY_ACCENT = GREY_B

        # --- 1. Title and Concept ---
        title_text = Text("Networking Device: Repeater", font_size=48, weight=BOLD, color=BLUE_ACCENT)
        concept_text = Text("Function and Characteristics of a Repeater", font_size=32, color=TEAL_ACCENT)
        
        title_group = VGroup(title_text, concept_text).arrange(DOWN, buff=0.7)
        title_group.move_to(ORIGIN).shift(UP*0.5)

        self.play(Write(title_group))
        self.wait(1.5)
        self.play(FadeOut(title_group, shift=UP))
        self.wait(0.5)

        # --- 2. Repeater Introduction and Explanation ---
        repeater_box = Rectangle(width=2.5, height=1.5, color=GREEN_ACCENT, fill_opacity=0.2)
        repeater_label = Text("REPEATER", font_size=28, color=GREEN_ACCENT)
        repeater_label.next_to(repeater_box, UP, buff=0.3)
        repeater_intro_group = VGroup(repeater_box, repeater_label) # Group repeater and label for collective positioning
        
        # Position repeater and its label to the left to make space for explanation points on the right
        repeater_intro_group.shift(LEFT * 2)

        explanation_points = VGroup(
            Text("• Operates at Physical Layer", font_size=24, color=GOLD_ACCENT),
            Text("• Regenerates Signal (not amplifies)", font_size=24, color=GOLD_ACCENT),
            Text("• Extends Transmission Length", font_size=24, color=GOLD_ACCENT),
            Text("• 2-Port Device", font_size=24, color=GOLD_ACCENT)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        explanation_points.next_to(repeater_intro_group, RIGHT, buff=0.8).shift(UP*0.5)

        self.play(Create(repeater_box), Write(repeater_label)) # Create box and write label individually
        self.play(FadeIn(explanation_points, shift=LEFT))
        self.wait(2)

        # Fade out explanations and move repeater to center for the main diagram
        self.play(
            FadeOut(explanation_points, shift=RIGHT),
            repeater_intro_group.animate.move_to(ORIGIN) # Move repeater group to center
        )
        self.wait(0.5)

        # --- 3. LAN Segments and Connection ---
        lan_segment_1_box = Rectangle(width=2, height=1.5, color=BLUE_ACCENT, fill_opacity=0.1)
        lan_segment_1_label = Text("LAN Segment 1", font_size=24, color=BLUE_ACCENT)
        lan_segment_1_label.next_to(lan_segment_1_box, UP, buff=0.2)
        lan_segment_1_group = VGroup(lan_segment_1_box, lan_segment_1_label)
        lan_segment_1_group.move_to(LEFT*4.5)

        lan_segment_2_box = Rectangle(width=2, height=1.5, color=TEAL_ACCENT, fill_opacity=0.1)
        lan_segment_2_label = Text("LAN Segment 2", font_size=24, color=TEAL_ACCENT)
        lan_segment_2_label.next_to(lan_segment_2_box, UP, buff=0.2)
        lan_segment_2_group = VGroup(lan_segment_2_box, lan_segment_2_label)
        lan_segment_2_group.move_to(RIGHT*4.5)
        
        # Cables connecting the LAN segments to the Repeater
        cable_left_start = lan_segment_1_box.get_right()
        cable_left_end = repeater_box.get_left()
        cable_left = Line(cable_left_start, cable_left_end, color=GREY_ACCENT, stroke_width=3)

        cable_right_start = repeater_box.get_right()
        cable_right_end = lan_segment_2_box.get_left()
        cable_right = Line(cable_right_start, cable_right_end, color=GREY_ACCENT, stroke_width=3)
        
        self.play(
            FadeIn(lan_segment_1_group, shift=LEFT),
            FadeIn(lan_segment_2_group, shift=RIGHT),
            Create(cable_left), 
            Create(cable_right)
        )
        self.wait(1)

        # --- 4. Signal Animation ---
        signal_dot_original_radius = 0.15
        signal_dot_original_color = GOLD_ACCENT
        signal_dot_original_fill_opacity = 1

        signal_dot = Dot(radius=signal_dot_original_radius, color=signal_dot_original_color, fill_opacity=signal_dot_original_fill_opacity)
        signal_dot.move_to(cable_left_start)

        self.play(FadeIn(signal_dot, scale=0.5))
        self.wait(0.5)

        # Phase 1: Weakening Signal (LAN1 to Repeater)
        weak_signal_radius = 0.05
        weak_signal_color = RED_ACCENT
        weak_signal_fill_opacity = 0.5

        self.play(
            signal_dot.animate.move_to(cable_left_end).set_radius(weak_signal_radius).set_color(weak_signal_color).set_fill_opacity(weak_signal_fill_opacity),
            run_time=2,
            rate_func=linear
        )
        self.wait(0.5)

        # Phase 2: Regeneration (Inside Repeater)
        # Briefly highlight repeater and regenerate signal
        self.play(
            repeater_box.animate.set_color(RED_ACCENT).set_stroke_width(5),
            Flash(repeater_box, flash_radius=0.7, line_length=0.3, num_lines=10, color=GOLD_ACCENT),
            run_time=0.5
        )
        self.play(
            signal_dot.animate.set_radius(signal_dot_original_radius).set_color(signal_dot_original_color).set_fill_opacity(signal_dot_original_fill_opacity),
            repeater_box.animate.set_color(GREEN_ACCENT).set_stroke_width(DEFAULT_STROKE_WIDTH), # Revert repeater color
            run_time=0.5
        )
        self.wait(0.5)

        # Phase 3: Revitalized Signal (Repeater to LAN2)
        self.play(
            signal_dot.animate.move_to(cable_right_end),
            run_time=2,
            rate_func=linear
        )
        self.wait(1)

        # Demonstrate the process again for emphasis
        self.play(signal_dot.animate.move_to(cable_left_start)) # Reset signal position to start
        self.wait(0.5)
        
        self.play(
            signal_dot.animate.move_to(cable_left_end).set_radius(weak_signal_radius).set_color(weak_signal_color).set_fill_opacity(weak_signal_fill_opacity),
            run_time=2,
            rate_func=linear
        )
        self.play(
            repeater_box.animate.set_color(RED_ACCENT).set_stroke_width(5),
            Flash(repeater_box, flash_radius=0.7, line_length=0.3, num_lines=10, color=GOLD_ACCENT),
            run_time=0.5
        )
        self.play(
            signal_dot.animate.set_radius(signal_dot_original_radius).set_color(signal_dot_original_color).set_fill_opacity(signal_dot_original_fill_opacity),
            repeater_box.animate.set_color(GREEN_ACCENT).set_stroke_width(DEFAULT_STROKE_WIDTH),
            run_time=0.5
        )
        self.play(
            signal_dot.animate.move_to(cable_right_end),
            run_time=2,
            rate_func=linear
        )
        self.wait(1)

        # --- 5. Clean up ---
        self.play(
            FadeOut(lan_segment_1_group, shift=LEFT),
            FadeOut(repeater_intro_group, shift=UP), # Fade out the entire repeater group
            FadeOut(lan_segment_2_group, shift=RIGHT),
            FadeOut(cable_left),
            FadeOut(cable_right),
            FadeOut(signal_dot)
        )
        self.wait(1)