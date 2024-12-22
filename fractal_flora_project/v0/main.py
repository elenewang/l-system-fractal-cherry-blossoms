from l_system import LSystem
from turtle_drawer import TurtleDrawer

def main():
    # Define the L-system parameters
    axiom = "X"  # Starting string for the L-system
    rules = {
        "X": "F-[[X]+X]+F[+FX]-X",    # Rule for expanding 'X'
        "F": "FF"   # Rule for expanding 'F'
    }
    iterations = 5  # Number of iterations to apply the rules
    angle = 25       # Angle to turn the turtle
    initial_length = 10 # Initial length of the branches

    # Create an LSystem object and generate the L-system string
    l_system = LSystem(axiom, rules, iterations)
    # Generate the L-system string by applying the rules for the given number of iterations
    l_system_string = l_system.generate()

    # Create a TurtleDrawer object and draw the L-system
    drawer = TurtleDrawer(angle, initial_length)
    screen = drawer.setup_screen()
    drawer.draw_l_system(l_system_string)
    screen.mainloop()

if __name__ == "__main__":
    main()