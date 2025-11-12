"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.") # raise ZeroDivisionError if a == 0
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Log base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm input must be positive.")
    return math.log(b, a) # use math library + raise ValueError

def exp(a, b):
    return math.pow(a, b)



