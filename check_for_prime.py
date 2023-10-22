"""
Module: prime_checker

This module provides a function for checking whether a given number is prime or not. It uses
basic prime-checking techniques to determine the primality of a number.

Functions:
- check_is_prime(number): Check if a number is prime.

Usage:
You can use the 'check_is_prime' function to determine whether a specific number is prime or not.

Example:
from prime_checker import check_is_prime
is_prime = check_is_prime(17)
print(is_prime)  # Output: True
"""

def check_is_prime(number):
    """
    Check if a number is prime.

    This function determines whether a given number is a prime number by
    applying basic prime-checking techniques. It returns True if the number is prime
    and False if it is not.

    Args:
        number (int): The number to be checked for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    elif number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True
