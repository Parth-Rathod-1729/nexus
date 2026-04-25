from manim import *

class Scene1(Scene):
    def construct(self):
        self.camera.background_color = "#282c34"

        # --- Part 1: Signal Weakening and Repeater ---
        title = Text("Signal Boosters: Repeaters and Hubs", font_size=50, color=WHITE).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 1. Network cable and initial strong signal
        cable_length = 10
        cable = Line(start=LEFT * cable_length / 2, end=RIGHT * cable_length / 2, color=BLUE_A)
        
        initial_signal = Dot(point=cable.get_left(), radius=0.2, color=GREEN)
        signal_text = Text("Strong Signal", font_size=24, color=GREEN).next_to(initial_signal, UP)

        self.play(Create(cable), Write(signal_text), Create(initial_signal))
        self.wait(0.5)

        explanation_text1 = Text("Signal weakens over distance...", font_size=30, color=YELLOW).to_edge(DOWN)
        self.play(Write(explanation_text1))

        # 2. Signal weakening animation
        weak_signal_dot = initial_signal.copy() # This dot will travel and weaken
        
        # Define custom updaters for color and radius to simulate weakening
        def signal_color_updater(m, alpha):
            # Interpolate color from GREEN to RED
            m.set_color(interpolate_color(GREEN, RED, alpha))

        def signal_radius_updater(m, alpha):
            # Interpolate radius from 0.2 to 0.05
            m.set_radius(interpolate(0.2, 0.05, alpha))

        self.play(
            FadeOut(signal_text), # Fade out initial strong signal text
            MoveAlongPath(weak_signal_dot, cable.copy().set_length(cable_length/2)), # Move to repeater position
            UpdateFromAlphaFunc(weak_signal_dot, signal_color_updater),
            UpdateFromAlphaFunc(weak_signal_dot, signal_radius_updater),
            run_time=2.5
        )
        self.wait(0.5)
        self.remove(explanation_text1)

        # 3. Repeater Introduction
        repeater_device = Rectangle(width=1.5, height=0.8, color=TEAL, fill_opacity=0.8).move_to(cable.get_center())
        repeater_label = Text("REPEATER", font_size=28, color=WHITE).move_to(repeater_device.get_center())
        repeater_ports_label = Text("2-Port Regenerator", font_size=20, color=WHITE).next_to(repeater_device, DOWN, buff=0.2)
        repeater_layer_label = Text("Physical Layer (Layer 1)", font_size=20, color=GOLD).next_to(repeater_device, UP, buff=0.2)

        repeater_group = VGroup(repeater_device, repeater_label, repeater_ports_label, repeater_layer_label)

        self.play(
            FadeOut(initial_signal), # Fade out the original static dot
            Create(repeater_device),
            Write(repeater_label),
            Write(repeater_ports_label),
            Write(repeater_layer_label)
        )
        self.wait(1)

        explanation_text2 = Text("Repeater regenerates weak signals.", font_size=30, color=YELLOW).to_edge(DOWN)
        explanation_text3 = Text("Extends network cable length.", font_size=30, color=YELLOW).next_to(explanation_text2, DOWN)
        self.play(Write(explanation_text2), Write(explanation_text3))

        # 4. Signal Regeneration
        # Ensure the weak signal dot is at the left edge of the repeater
        self.play(
            weak_signal_dot.animate.move_to(repeater_device.get_left()),
            run_time=0.5
        )

        # Create a strong dot at the repeater's exit
        strong_dot_at_exit = Dot(point=repeater_device.get_right(), radius=0.2, color=GREEN)

        # Transform the weak signal at the entrance to a strong signal at the exit
        self.play(
            Transform(weak_signal_dot, strong_dot_at_exit),
            run_time=0.5
        )

        # Move the regenerated strong signal to the end of the cable
        self.play(
            MoveAlongPath(weak_signal_dot, cable.copy().set_x(cable.get_right().x).set_length(cable_length/2)),
            run_time=2
        )
        self.remove(explanation_text2, explanation_text3)
        self.wait(1)

        # Fade out repeater scene elements
        self.play(
            FadeOut(cable, target_mode="horizontal"),
            FadeOut(weak_signal_dot),
            FadeOut(repeater_group),
            FadeOut(title)
        )
        self.wait(1)

        # --- Part 2: Hub in Star Topology ---
        title_hub = Text("Hubs: Multi-Port Repeaters", font_size=50, color=WHITE).to_edge(UP)
        self.play(Write(title_hub))
        self.wait(1)

        # 1. Hub Introduction
        hub_device = Rectangle(width=1.5, height=1.5, color=TEAL, fill_opacity=0.8)
        hub_label = Text("HUB", font_size=32, color=WHITE).move_to(hub_device.get_center())
        hub_multi_port_label = Text("Multi-Port Repeater", font_size=20, color=WHITE).next_to(hub_device, DOWN, buff=0.2)
        hub_layer_label = Text("Physical Layer (Layer 1)", font_size=20, color=GOLD).next_to(hub_device, UP, buff=0.2)

        hub_group = VGroup(hub_device, hub_label, hub_multi_port_label, hub_layer_label)

        self.play(Create(hub_device), Write(hub_label), Write(hub_multi_port_label), Write(hub_layer_label))
        self.wait(1)

        # 2. Star Topology Setup
        num_devices = 4
        devices = VGroup()
        device_labels = VGroup()
        device_cables = VGroup()

        # Positions for devices around the hub
        angles = [n * 2 * PI / num_devices + PI/4 for n in range(num_devices)] # Add PI/4 to rotate slightly
        radius_star = 3.5

        for i, angle in enumerate(angles):
            device_pos = hub_device.get_center() + radius_star * np.array([np.cos(angle), np.sin(angle), 0])
            device_square = Square(side_length=0.7, color=BLUE, fill_opacity=0.6).move_to(device_pos)
            device_text = Text(f"Device {i+1}", font_size=24, color=WHITE).next_to(device_square, direction=device_pos - hub_device.get_center(), buff=0.2)
            device_cable = Line(start=hub_device.get_center(), end=device_square.get_center(), color=BLUE_A)

            devices.add(device_square)
            device_labels.add(device_text)
            device_cables.add(device_cable)

        self.play(Create(devices), Write(device_labels), Create(device_cables))
        self.wait(1)

        # 3. Data Broadcast Animation
        explanation_hub1 = Text("Hub broadcasts data to ALL connected devices.", font_size=30, color=YELLOW).to_edge(DOWN)
        explanation_hub2 = Text("No filtering, no intelligence.", font_size=30, color=YELLOW).next_to(explanation_hub1, DOWN)
        self.play(Write(explanation_hub1), Write(explanation_hub2))
        self.wait(1)

        # Data from Device 1 to Hub
        sender_device_idx = 0 # Device 1
        sender_device = devices[sender_device_idx] 
        sender_cable = device_cables[sender_device_idx]

        data_packet_in = Dot(point=sender_device.get_center(), radius=0.15, color=GOLD)
        self.play(Create(data_packet_in))
        self.play(
            MoveAlongPath(data_packet_in, sender_cable),
            run_time=1.5
        )
        self.remove(data_packet_in) # Packet "absorbed" by the hub

        # Hub broadcasts the packet to all other devices
        broadcast_packets = VGroup()
        animations_broadcast = []

        for i in range(num_devices):
            # Only broadcast to devices other than the sender
            if i != sender_device_idx: 
                broadcast_packet = Dot(point=hub_device.get_center(), radius=0.15, color=GOLD)
                broadcast_packets.add(broadcast_packet)
                animations_broadcast.append(
                    MoveAlongPath(broadcast_packet, device_cables[i])
                )
                self.add(broadcast_packet) # Add each packet to scene for simultaneous animation

        self.play(*animations_broadcast, run_time=2)
        self.wait(0.5)

        self.play(FadeOut(broadcast_packets))
        self.wait(0.5)

        explanation_hub3 = Text("All ports share the same collision domain and bandwidth.", font_size=30, color=YELLOW).to_edge(DOWN)
        self.play(FadeOut(explanation_hub1, explanation_hub2), Write(explanation_hub3))
        self.wait(2)

        self.play(
            FadeOut(title_hub),
            FadeOut(hub_group),
            FadeOut(devices),
            FadeOut(device_labels),
            FadeOut(device_cables),
            FadeOut(explanation_hub3)
        )
        self.wait(1)