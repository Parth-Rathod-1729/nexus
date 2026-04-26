from manim import *

class Scene2(Scene):
    def construct(self):
        # Title and Title Bar
        title = Text("The Power of the Merge", color=GOLD, font_size=40).to_edge(UP, buff=0.5)
        underline = Line(LEFT * 3, RIGHT * 3, color=GOLD).next_to(title, DOWN, buff=0.1)
        
        # Runs on the Left
        run1 = Rectangle(width=2.5, height=0.7, color=BLUE, fill_opacity=0.6)
        run2 = Rectangle(width=2.5, height=0.7, color=TEAL, fill_opacity=0.6).next_to(run1, DOWN, buff=0.4)
        run3 = Rectangle(width=2.5, height=0.7, color=GREEN, fill_opacity=0.6).next_to(run2, DOWN, buff=0.4)
        
        run_label1 = Text("Run A", font_size=24).move_to(run1.get_center())
        run_label2 = Text("Run B", font_size=24).move_to(run2.get_center())
        run_label3 = Text("Run C", font_size=24).move_to(run3.get_center())
        
        runs_group = VGroup(run1, run2, run3, run_label1, run_label2, run_label3).to_edge(LEFT, buff=1)
        
        # Node Power Concept (The Boundary)
        boundary_dot = Dot(color=YELLOW).move_to(Line(run1.get_bottom(), run2.get_top()).get_center())
        power_box = Rectangle(width=3, height=1, color=WHITE).shift(RIGHT * 0.5)
        power_text = Text("Node Power = 3", color=YELLOW, font_size=32).move_to(power_box.get_center())
        arrow_to_power = Arrow(boundary_dot.get_right(), power_box.get_left(), color=WHITE, buff=0.1)
        
        # Binary Tree Representation on the Right
        node_root = Circle(radius=0.3, color=WHITE, fill_opacity=0.2).shift(RIGHT * 4.5 + UP * 1)
        node_l = Circle(radius=0.3, color=WHITE, fill_opacity=0.2).shift(RIGHT * 3.5 + DOWN * 0.5)
        node_r = Circle(radius=0.3, color=WHITE, fill_opacity=0.2).shift(RIGHT * 5.5 + DOWN * 0.5)
        
        edge_l = Line(node_root.get_bottom(), node_l.get_top(), buff=0.05)
        edge_r = Line(node_root.get_bottom(), node_r.get_top(), buff=0.05)
        
        tree_label = Text("Balanced Tree Structure", font_size=20, color=WHITE).next_to(node_root, UP, buff=0.5)
        tree_group = VGroup(node_root, node_l, node_r, edge_l, edge_r, tree_label)
        
        # Highlighting the correspondence
        highlight_circle = Circle(radius=0.4, color=YELLOW).move_to(node_l.get_center())
        depth_label = Text("Depth Level 3", font_size=20, color=YELLOW).next_to(node_l, DOWN, buff=0.3)

        # --- Animations ---
        
        # 1. Show Title and Runs
        self.play(Write(title), Create(underline))
        self.play(Create(runs_group), run_time=2)
        self.wait(1)
        
        # 2. Point out Boundary and Calculate Node Power
        self.play(Create(boundary_dot))
        self.play(Create(arrow_to_power), Create(power_box), Write(power_text))
        self.wait(1.5)
        
        # 3. Transition to Tree Structure
        self.play(Create(tree_group))
        self.play(
            power_text.animate.set_color(WHITE),
            Create(highlight_circle),
            Write(depth_label)
        )
        self.wait(2.5)
        
        # 4. Final summary visual
        explanation = Text("Ensures optimal merge sequence", font_size=24, color=GOLD).to_edge(DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2)

        # Cleanup within duration limits
        self.play(
            FadeOut(runs_group),
            FadeOut(tree_group),
            FadeOut(power_box),
            FadeOut(power_text),
            FadeOut(explanation),
            FadeOut(highlight_circle),
            FadeOut(depth_label),
            FadeOut(boundary_dot),
            FadeOut(arrow_to_power),
            FadeOut(title),
            FadeOut(underline)
        )