def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception:
        return "Ivalid mathematical expression"

    