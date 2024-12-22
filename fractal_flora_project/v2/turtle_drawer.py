import turtle
import random
import time

class TurtleDrawer:
    def __init__(self, angle, initial_length, wind_animator):
        # Initialize the drawer with angle and initial branch length
        self.angle = angle
        self.initial_length = initial_length
        self.wind_animator = wind_animator
        self.turtle = turtle.Turtle()
        self.stack = []  # Stack to save the turtle's state
        self.flower_colors = ["#FF69B4", "#FF1493", "#FFB6C1", "#FFC0CB", "#FF69B4"]

    def setup_screen(self):
        # Set up the turtle graphics screen with specific dimensions and background color
        screen = turtle.Screen()
        screen.tracer(0)  # Turn off animation for manual updating
        screen.setup(800, 800)
        screen.bgcolor("white")
        screen.title("L-System Tree with Windy Cherry Blossoms")
        return screen

    def apply_wind_effect(self, length, angle, depth):
        """Apply wind effect to branch angles based on length and depth."""
        wind_factor = self.wind_animator.wind_strength * (length / 10) * (1 / (depth + 1))
        return angle + wind_factor * self.wind_animator.wind_direction

    def draw_branch(self, length, depth):
        # Draw a branch with a given length and depth
        if depth > 0:
            # Apply wind effect
            current_angle = self.apply_wind_effect(length, self.turtle.heading(), depth)
            self.turtle.setheading(current_angle)

            self.turtle.pensize(5)
            self.turtle.pendown()  # Put the pen down to start drawing
            self.turtle.pencolor("#8B4513")  # HEX code brown for the trunk
            # Add slight randomness to branch length for realism
            actual_length = length * (0.9 + random.random() * 0.2)
            self.turtle.forward(actual_length)  # Move the turtle forward by the actual length

    def draw_flower(self, size):
        # Draw a simple flower with petals
        original_heading = self.turtle.heading()  # Save the current heading of the turtle

        # Draw flower center
        self.turtle.pendown()  # Put the pen down to start drawing
        self.turtle.fillcolor("#660b26")  # Set the fill color to dark pink for the flower center
        self.turtle.begin_fill()  # Start filling the shape
        self.turtle.circle(size * 1.5)  # Draw the center of the flower as a circle
        self.turtle.end_fill()  # End filling the shape

        # Draw petals
        self.turtle.pencolor(random.choice(self.flower_colors))  # Set the pen color to a random flower color
        for _ in range(5):  # Draw 5 petals
            self.turtle.fillcolor(random.choice(self.flower_colors))  # Set the fill color to a random flower color
            self.turtle.begin_fill()  # Start filling the petal
            self.turtle.circle(size * 3, 60)  # Draw the first half of the petal
            self.turtle.left(120)  # Turn left to draw the second half of the petal
            self.turtle.circle(size * 3, 60)  # Draw the second half of the petal
            self.turtle.left(120)  # Turn left to complete the petal
            self.turtle.end_fill()  # End filling the petal
            self.turtle.left(72)  # Turn left to position for the next petal (360/5 = 72 degrees)

        self.turtle.penup()  # Lift the pen to stop drawing
        self.turtle.setheading(original_heading)  # Restore the original heading of the turtle

    def draw_l_system(self, instructions):
        # Draw the L-system based on the given instructions
        self.turtle.speed(0)  # Set the fastest speed to see the drawing process
        self.turtle.penup()  # Lift the pen to move without drawing
        self.turtle.goto(0, -300)  # Move the turtle to the starting position
        self.turtle.left(90)  # Turn the turtle to face upwards

        # interrupt the animation gracefully when the user presses command+'r'
        def stop_animation():
            self.wind_animator.is_animated = False
            turtle.bye()

        screen = turtle.Screen()
        screen.listen()
        screen.onkey(stop_animation, "r")

        while self.wind_animator.is_animated:
            self.turtle.clear()
            self.stack = []
            self.turtle.penup()
            self.turtle.goto(0, -300)
            self.turtle.setheading(90)
            current_length = self.initial_length
            depth = 10

            for cmd in instructions:
                if cmd == 'F':
                    self.draw_branch(current_length, depth)  # Draw a branch
                elif cmd == '+':
                    self.turtle.right(self.angle)  # Turn the turtle right by the specified angle
                elif cmd == '-':
                    self.turtle.left(self.angle)  # Turn the turtle left by the specified angle
                elif cmd == '[':
                    # Save the current state
                    self.stack.append((self.turtle.position(), self.turtle.heading(), current_length, depth))
                    current_length *= 0.7  # Reduce the branch length for the next level
                    depth -= 1  # Decrease the depth
                elif cmd == ']':
                    # Restore the saved state
                    if self.stack:
                        pos, heading, current_length, depth = self.stack.pop()
                        self.turtle.penup()
                        self.turtle.goto(pos)  # Move the turtle to the saved position
                        self.turtle.setheading(heading)  # Set the turtle's heading to the saved heading
                elif cmd == 'P':
                    self.draw_flower(current_length * 0.5)  # Draw a flower

            turtle.update()
            time.sleep(0.016)  # Maintain ~60 FPS