import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def square(a):
    return a * a

def logarithm(a, base = 10):
    if a <= 0:
        raise ValueError("Logarithm argument must be positive")
    if base <= 0:
        raise ValueError("Logarithm base must be positive")
    if base == 1:
        raise ValueError("Logarithm base cannot be 1")
    return math.log(a, base)

def sin(a):
    return math.sin(a)

def cosine(a):
    return math.cos(a)

def percentage(value, percent):
    return (value * percent) / 100

def power(base, exponent):
    return base ** exponent