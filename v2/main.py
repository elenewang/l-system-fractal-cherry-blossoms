from l_system import LSystem
from turtle_drawer import TurtleDrawer
from wind_animator import WindAnimator

def main():
    # Define the L-system parameters
    axiom = "X"  # Starting string for the L-system
    rules = {
        "X": "F-[[X]+X]+F[+FX]-XP",    # Added P for flowers
        "F": "FF",   # Rule for expanding 'F'
        "P": "P"  # Flower symbol
    }
    iterations = 5  # Number of iterations to apply the rules
    angle = 25       # Angle to turn the turtle
    initial_length = 10 # Initial length of the branches

    # Create an LSystem object and generate the L-system string
    l_system = LSystem(axiom, rules, iterations)
    l_system_string = l_system.generate()

    # Create a WindAnimator object and start the wind animation
    wind_animator = WindAnimator()
    wind_animator.start()

    # Create a TurtleDrawer object and draw the L-system
    drawer = TurtleDrawer(angle, initial_length,wind_animator)
    screen = drawer.setup_screen()
    drawer.draw_l_system(l_system_string)
    screen.mainloop()

if __name__ == "__main__":
    main()