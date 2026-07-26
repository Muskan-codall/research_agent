# calculator.py


def calculate(expression):
    """
    Performs calculations according to the BODMAS rule.
    """

    try:
        # Replace '^' with '**' for exponent operations.
        expression = expression.replace("^", "**")

        # Evaluate the mathematical expression.
        result = eval(expression)

        return f"Result = {result}"

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    except Exception:
        return "Error: Please enter a valid mathematical expression."
    