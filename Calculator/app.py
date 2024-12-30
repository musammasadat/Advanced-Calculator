import math
import time 

class Calculator:
    def __init__(self):
        print("Calculator Started.")

    def calculate(self, expression):
        try:
            allowed_functions = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
            allowed_functions.update({"abs": abs, "round": round})

            result = eval(expression, {"__builtins__": None}, allowed_functions)
            return result
        except Exception as e:
            return f"Error: {str(e)}"

    def run(self):
        print("Welcome to the Calculator!")
        print("You can enter any mathematical expression.")
        print("Examples:")
        print(" - Addition: 3 + 5")
        print(" - Square root: sqrt(16)")
        print(" - Logarithm: log(8, 2)")
        print(" - Sine: sin(pi/2)")
        print(" - Type 'q' to exit.")
        
        while True:
            expression = input("\nEnter your expression: ")
            print("Please wait for a moment...")
            time.sleep(1)

            if expression.lower() == 'q':
                print("Calculator is shutting down.")
                break
            result = self.calculate(expression)
            print("Result:", result)


calculator = Calculator()
calculator.run()
