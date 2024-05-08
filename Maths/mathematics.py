"""This module contains the basic mathematical operations."""
from numpy import isnan

def summation(a, b):
    """This function returns the sum of two numbers."""
    if isnan(a) or isnan(b):
        raise ValueError("Invalid input. Please provide two numbers.")
    else:
        return a + b

def subtraction(a, b):
    """This function returns the difference between two numbers."""
    if isnan(a) or isnan(b):
        raise ValueError("Invalid input. Please provide two numbers.")
    else:
        return a - b

def multiplication(a, b):
    """This function returns the product of two numbers."""
    if isnan(a) or isnan(b):
        raise ValueError("Invalid input. Please provide two numbers.")
    else:
        return a * b

def division(a, b):
    """This function returns the division of two numbers."""
    if isnan(a) or isnan(b):
        raise ValueError("Invalid input. Please provide two numbers.")
    elif b == 0:
        raise ValueError("Invalid input. Cannot divide by zero.")
    else:
        return a / b

def power(a, b):
    """This function returns the power of a number."""
    if isnan(a) or isnan(b):
        raise ValueError("Invalid input. Please provide two numbers.")
    else:
        return a ** b

def modulus(a, b):
    """This function returns the modulus of two numbers."""
    if isnan(a) or isnan(b):
        raise ValueError("Invalid input. Please provide two numbers.")
    elif b == 0:
        raise ValueError("Invalid input. Cannot divide by zero.")
    else:
        return a % b

def integer_division(a, b):
    """This function returns the integer division of two numbers."""
    if isnan(a) or isnan(b):
        raise ValueError("Invalid input. Please provide two numbers.")
    elif b == 0:
        raise ValueError("Invalid input. Cannot divide by zero.")
    else:
        return a // b
