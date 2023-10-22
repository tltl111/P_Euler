"""
Module: prime_summation

This module contains functions for calculating the sum of prime numbers below a given limit.
It imports the 'check_is_prime' function from the 'check_for_prime'
module to check for prime numbers.

Functions:
- add_up_primes_below(number): Calculates the sum of prime numbers below a given limit.

Usage:
You can use the 'add_up_primes_below' function to find the
sum of prime numbers below a specified limit.

Example:
from prime_summation import add_up_primes_below
result = add_up_primes_below(2000000)
print(result)
"""
from check_for_prime import check_is_prime

MAX_NUMBER = 2000000
TEST_NUMBER = 10

def add_up_primes_below(number):
    """
    Calculate the sum of prime numbers below a given number.

    This function iterates through numbers from 0 to 'number - 1',
    checks if each number is prime using the 'check_is_prime' function,
    and accumulates the prime numbers' sum.

    Args:
        number (int): The upper limit (exclusive) for finding prime numbers.

    Returns:
        int: The sum of prime numbers below the given 'number'.
    """
    outcome = 0

    for x in range(number):
        if check_is_prime(x):
            outcome += x
        else:
            continue

    return outcome

print(add_up_primes_below(MAX_NUMBER))
