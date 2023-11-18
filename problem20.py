"""
factorial_sum_digits module

This module provides a function to calculate the factorial of a number and then find
the sum of its digits.

Functions:
    - sum_digits_factorial(number): Calculates the factorial of the given number and
      returns the sum of its digits.
"""

from math import factorial

def sum_digits_factorial(number):
    """
    Calculate the sum of digits of the factorial of a number.

    Parameters:
        number (int): The number for which to calculate the factorial.

    Returns:
        int: The sum of the digits of the factorial of the given number.
    """
    fact = factorial(number)
    fact_str = str(fact)
    digit_sum = 0

    for digit_char in fact_str:
        digit_sum += int(digit_char)

    return digit_sum

print(sum_digits_factorial(100))
