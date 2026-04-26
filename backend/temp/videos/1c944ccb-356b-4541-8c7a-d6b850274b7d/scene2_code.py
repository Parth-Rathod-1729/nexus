from manim import *

class Scene2(Scene):
    def construct(self):
        # Header title
        title = Text("The Power of Boundaries", color=WHITE).scale(0.8).to_edge(UP)
        
        # Define two adjacent runs
        run_1 = Rectangle(width=3.2, height=1.5, color=TEAL, fill_opacity=0.5).shift(LEFT * 1.7 + DOWN * 1)
        run_2 = Rectangle(width=3.2, height=1.5, color=TEAL, fill_opacity=0.5).shift(RIGHT * 1.7 + DOWN * 1)
        label_1 = Text("Run A", font_size=28).move_to(run_1.get_center())
        label_2 = Text("Run B", font_size=28).move_to(run_2.get_center())
        runs_group = VGroup(run_1, run_2, label_1, label_2)
        
        # Boundary line between the two runs
        boundary = Line(start=UP * 2.0, end=DOWN * 2.0, color=BLUE, stroke_width=8)
        
        # Imaginary Green Balanced Binary Tree Structure
        node_top = Circle(radius=0.3, color=GREEN, fill_opacity=0.2).shift(UP * 2.5)
        node_l1 = Circle(radius=0.3, color=GREEN, fill_opacity=0.2).shift(UP * 1.0 + LEFT * 2.0)
        node_r1 = Circle(radius=0.3, color=GREEN, fill_opacity=0.2).shift(UP * 1.0 + RIGHT * 2.0)
        edge_l = Line(node_top.get_bottom(), node_l1.get_top(), color=GREEN).set_opacity(0.3)
        edge_r = Line(node_top.get_bottom(), node_r1.get_top(), color=GREEN).set_opacity(0.3)
        
        tree_viz = VGroup(node_top, node_l1, node_r1, edge_l, edge_r)
        
        # Power value label
        power_val = MathTex(r"\text{Power} = 3", color=YELLOW).scale(1.2).next_to(boundary, UP, buff=0.5)
        
        # --- Animation Sequence ---
        self.play(Write(title))
        self.play(Create(runs_group))
        self.wait(1)
        
        # Drop the boundary line
        self.play(Create(boundary))
        self.wait(0.5)
        
        # Fade in the imaginary tree
        self.play(FadeIn(tree_viz))
        
        # Indicate level with a marker
        level_marker = Dot(color=GOLD).move_to(node_top.get_center())
        self.play(FadeIn(level_marker))
        # Move marker down to simulate finding the power level
        self.play(level_marker.animate.move_to(node_l1.get_center()), run_time=1.5)
        
        # Final power display
        self.play(
            Write(power_val),
            boundary.animate.set_color(GOLD),
            tree_viz.animate.set_opacity(0.1)
        )
        
        # Highlight connection
        highlight_arrow = Arrow(start=power_val.get_bottom(), end=boundary.get_top(), color=YELLOW, buff=0.1)
        self.play(Create(highlight_arrow))
        
        self.wait(2)