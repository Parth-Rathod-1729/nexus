from manim import *

class Scene1(Scene):
    def construct(self):
        # Title and Concept
        title = Text("The Basic Boosters: Repeaters and Hubs", font_size=50, color=BLUE).to_edge(UP)
        concept = Text("Signal regeneration and broadcast in local networks.", font_size=36, color=YELLOW).next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(concept))
        self.wait(1)

        # Part 1: Repeater
        repeater_intro_text = Text(
            "Repeaters regenerate weak signals on the same network.",
            font_size=32, color=WHITE
        ).next_to(concept, DOWN, buff=1).to_edge(LEFT, buff=0.5)

        self.play(Write(repeater_intro_text))
        self.wait(0.5)

        # --- Signal Weakening ---
        cable_length = 6
        cable_segment1 = Line(ORIGIN, RIGHT * cable_length, color=WHITE).next_to(repeater_intro_text, DOWN, buff=1).align_to(LEFT, repeater_intro_text)
        
        signal_start_point = cable_segment1.get_left() + RIGHT * 0.5
        signal_end_point = cable_segment1.get_right() - RIGHT * 0.5

        data_packet = Square(side_length=0.4, fill_opacity=1, color=GREEN).move_to(signal_start_point)
        data_label = Text("Data", font_size=20, color=BLACK).move_to(data_packet)
        initial_signal = VGroup(data_packet, data_label)

        self.play(Create(cable_segment1))
        self.play(Create(initial_signal))
        self.wait(0.5)

        weak_signal = initial_signal.copy()
        weak_signal_path = Line(signal_start_point, signal_end_point)

        # Animate signal traveling and weakening
        self.play(
            MoveAlongPath(weak_signal, weak_signal_path),
            weak_signal[0].animate.set(width=0.2, height=0.2, fill_opacity=0.5), # Shrink and fade packet
            weak_signal[1].animate.scale(0.5).set_color(GRAY), # Shrink and fade label
            run_time=2
        )
        self.remove(initial_signal) # Remove the original, strong signal before it travels.
        self.wait(0.5)

        # --- Repeater Appears ---
        repeater_box = Rectangle(width=2, height=1.2, color=BLUE_B, fill_opacity=0.8).next_to(cable_segment1, RIGHT, buff=0.5)
        repeater_text = Text("REPEATER", font_size=24, color=WHITE).move_to(repeater_box)
        repeater_port1 = Dot(color=YELLOW).next_to(repeater_box, LEFT, buff=0)
        repeater_port2 = Dot(color=YELLOW).next_to(repeater_box, RIGHT, buff=0)
        
        repeater_device = VGroup(repeater_box, repeater_text, repeater_port1, repeater_port2)

        self.play(Create(repeater_device))
        self.wait(0.5)

        # --- Signal Regeneration ---
        # Move weak signal into repeater
        self.play(weak_signal.animate.move_to(repeater_box.get_center()), run_time=0.5)
        self.play(FadeOut(weak_signal))

        regeneration_pulse = Circle(radius=0.3, color=TEAL, fill_opacity=0.5).move_to(repeater_box.get_center())
        regen_label = Text("REGENERATE", font_size=20, color=WHITE).move_to(regeneration_pulse)
        self.play(Create(VGroup(regeneration_pulse, regen_label)))
        self.play(FadeOut(VGroup(regeneration_pulse, regen_label)), run_time=0.8)
        self.wait(0.5)

        # --- Regenerated Signal ---
        cable_segment2 = Line(repeater_box.get_right(), repeater_box.get_right() + RIGHT * cable_length, color=WHITE)
        regenerated_packet = Square(side_length=0.4, fill_opacity=1, color=GREEN).move_to(repeater_box.get_right())
        regen_data_label = Text("Data", font_size=20, color=BLACK).move_to(regenerated_packet)
        regenerated_signal = VGroup(regenerated_packet, regen_data_label)

        self.play(Create(cable_segment2))
        self.play(Create(regenerated_signal))
        self.play(
            regenerated_signal.animate.move_to(cable_segment2.get_right()),
            run_time=1.5
        )
        self.wait(0.5)

        repeater_info1 = Text("Physical Layer", font_size=28, color=GOLD).next_to(repeater_box, UP, buff=0.5)
        repeater_info2 = Text("2-port device", font_size=28, color=GOLD).next_to(repeater_box, DOWN, buff=0.5)
        self.play(Write(repeater_info1), Write(repeater_info2))
        self.wait(2)

        self.play(
            FadeOut(VGroup(repeater_intro_text, cable_segment1, cable_segment2,
                          repeater_device, regenerated_signal, repeater_info1, repeater_info2))
        )
        self.wait(1)

        # Part 2: Hub
        hub_intro_text = Text(
            "Hubs are multi-port repeaters: They broadcast to all devices.",
            font_size=32, color=WHITE
        ).next_to(concept, DOWN, buff=1).to_edge(LEFT, buff=0.5)

        self.play(Transform(repeater_intro_text, hub_intro_text)) # Reuse repeater_intro_text variable
        self.wait(0.5)

        # --- Hub and Devices ---
        hub_box = Rectangle(width=2, height=2, color=RED_B, fill_opacity=0.8).move_to(ORIGIN)
        hub_text = Text("HUB", font_size=30, color=WHITE).move_to(hub_box)
        hub = VGroup(hub_box, hub_text)
        hub.next_to(repeater_intro_text, DOWN, buff=1)

        self.play(Create(hub))
        self.wait(0.5)

        num_devices = 4
        device_spacing = 3
        devices = VGroup()
        connection_lines = VGroup()
        hub_ports = VGroup()

        device_positions = [
            hub.get_center() + LEFT * device_spacing,
            hub.get_center() + RIGHT * device_spacing,
            hub.get_center() + UP * device_spacing,
            hub.get_center() + DOWN * device_spacing
        ]

        for i in range(num_devices):
            device_box = Square(side_length=0.8, color=GREEN, fill_opacity=0.7).move_to(device_positions[i])
            device_label = Text(f"PC{i+1}", font_size=20, color=BLACK).move_to(device_box)
            devices.add(VGroup(device_box, device_label))

            port_point = hub_box.get_boundary_point(device_positions[i] - hub.get_center())
            hub_port = Dot(color=YELLOW).move_to(port_point)
            hub_ports.add(hub_port)

            line = Line(device_box.get_center(), hub_port.get_center(), color=WHITE)
            connection_lines.add(line)
        
        # Adjust positioning for aesthetic
        devices[0].shift(DOWN * 0.5)
        devices[1].shift(DOWN * 0.5)
        devices[2].shift(RIGHT * 0.5)
        devices[3].shift(RIGHT * 0.5)

        connection_lines = VGroup()
        for i in range(num_devices):
            line = Line(devices[i][0].get_center(), hub_ports[i].get_center(), color=WHITE)
            connection_lines.add(line)


        self.play(Create(devices), Create(connection_lines), Create(hub_ports))
        self.wait(1)

        # --- Data Packet Arrival and Broadcast ---
        source_device_index = 0 # PC1 sends data
        packet_color = GOLD
        packet_size = 0.3

        incoming_packet = Square(side_length=packet_size, fill_opacity=1, color=packet_color).move_to(devices[source_device_index][0].get_center())
        self.play(Create(incoming_packet))
        self.wait(0.5)

        # Packet travels to hub
        # Corrected: Use .animate.move_to() when moving to a coordinate
        self.play(incoming_packet.animate.move_to(hub_ports[source_device_index].get_center()), run_time=1)
        self.play(FadeOut(incoming_packet)) # Packet "enters" the hub

        # Broadcast from hub to all other devices
        outgoing_packets = VGroup()
        animations = []
        for i in range(num_devices):
            if i != source_device_index:
                outgoing_packet = Square(side_length=packet_size, fill_opacity=1, color=packet_color).move_to(hub_ports[i].get_center())
                outgoing_packets.add(outgoing_packet)
                animations.append(Create(outgoing_packet))
                # Corrected: Use .animate.move_to() when moving to a coordinate
                animations.append(outgoing_packet.animate.move_to(devices[i][0].get_center()))
        
        self.play(*animations, run_time=1.5)
        self.wait(0.5)

        hub_info1 = Text("Multi-port Repeater", font_size=28, color=GOLD).next_to(hub_box, UP, buff=0.5)
        hub_info2 = Text("Broadcasts to ALL connected devices", font_size=28, color=GOLD).next_to(hub_box, DOWN, buff=0.5)
        hub_info3 = Text("No filtering (no intelligence)", font_size=28, color=WHITE).next_to(hub_info2, DOWN, buff=0.2)
        hub_info4 = Text("Acts like a Logical Bus", font_size=28, color=WHITE).next_to(hub_info3, DOWN, buff=0.2)

        self.play(Write(hub_info1))
        self.play(Write(hub_info2))
        self.play(Write(hub_info3))
        self.play(Write(hub_info4))
        self.wait(3)

        self.play(
            FadeOut(title),
            FadeOut(concept),
            FadeOut(repeater_intro_text), # This now holds hub_intro_text
            FadeOut(hub),
            FadeOut(devices),
            FadeOut(connection_lines),
            FadeOut(hub_ports),
            FadeOut(outgoing_packets),
            FadeOut(hub_info1),
            FadeOut(hub_info2),
            FadeOut(hub_info3),
            FadeOut(hub_info4)
        )
        self.wait(1)