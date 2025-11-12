import math
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
def logarithm(a,b):
    if a <= 0 or a == 1:
        raise ValueError("logarithm domain error: base must be > 0 and != 1")
    if b <= 0:
        raise ValueError("logarithm domain error: x must be > 0")
    return math.log(a, b)
def exp(a,b):
    return a ** b