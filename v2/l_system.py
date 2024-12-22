class LSystem:
    def __init__(self, axiom, rules, iterations):
        # Initialize the L-system with an axiom, rules, and number of iterations
        self.axiom = axiom
        self.rules = rules
        self.iterations = iterations

    def generate(self):
        # Generate the L-system string after applying rules for iterations
        current_string = self.axiom
        for _ in range(self.iterations):
            # Apply the rules to generate the new string
            current_string = "".join(self.rules.get(char, char) for char in current_string)
        return current_string
