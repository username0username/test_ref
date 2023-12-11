def plus(a, b):
    validate(a,b)
    return a + b

def minus(a, b):
    validate(a,b)
    return a - b

def multiply(a, b):
    validate(a,b)
    return a * b

def divide(a, b):
    validate(a,b)
    if b == 0:
        raise ValueError("Нельзя делить на 0")
    return a / b

def validate(a,b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Аргументы должны быть числами")