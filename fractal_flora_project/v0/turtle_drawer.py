import turtle
import random

class TurtleDrawer:
    def __init__(self, angle, initial_length):
        # Initialize the drawer with angle and initial branch length
        self.angle = angle
        self.initial_length = initial_length
        self.turtle = turtle.Turtle()
        self.stack = []  # Stack to save the turtle's state

    def setup_screen(self):
        # Set up the turtle graphics screen with specific dimensions and background color
        screen = turtle.Screen()
        screen.setup(800, 800)
        screen.bgcolor("white")
        screen.title("L-System Cherry Blossom Trunk")
        return screen

    def draw_branch(self, length, depth):
        # Draw a branch with a given length and depth
        if depth > 0:
            self.turtle.pensize(5)
            self.turtle.pendown()   # Put the pen down to start drawing
            self.turtle.pencolor("#8B4513")  # HEX code brown for the trunk
            # Add slight randomness to branch length for realism
            actual_length = length * (0.9 + random.random() * 0.2)
            self.turtle.forward(actual_length) # Move the turtle forward by the actual length

    def draw_l_system(self, instructions):
        # Draw the L-system based on the given instructions
        self.turtle.speed(0)  # Set the fastest speed to see the drawing process
        self.turtle.penup()   # Lift the pen to move without drawing
        self.turtle.goto(0, -300)   # Move the turtle to the starting position
        self.turtle.left(90)    # Turn the turtle to face upwards

        current_length = self.initial_length
        depth = 10   # Set the initial depth

        for cmd in instructions:
            if cmd == 'F':
                self.draw_branch(current_length, depth)   # Draw a branch
            elif cmd == '+':
                self.turtle.right(self.angle)  # Turn the turtle right by the specified angle
            elif cmd == '-':
                self.turtle.left(self.angle)   # Turn the turtle left by the specified angle
            elif cmd == '[':
                # Save the current state
                self.stack.append((self.turtle.position(), self.turtle.heading(), current_length, depth))
                current_length *= 0.7  # Reduce the branch length for the next level
                depth -= 1   # Decrease the depth
            elif cmd == ']':
                # Restore the saved state
                if self.stack:
                    pos, heading, current_length, depth = self.stack.pop()
                    self.turtle.penup()
                    self.turtle.goto(pos)   # Move the turtle to the saved position
                    self.turtle.setheading(heading)   # Set the turtle's heading to the saved heading