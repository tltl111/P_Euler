"""
This module contains functions to find and calculate the sum of amicable numbers.

Functions:
- sum_of_divisors(n): Calculate the sum of proper divisors for a given number.
- find_amicable_numbers(limit): Find all amicable numbers below a specified limit.
"""

def sum_of_divisors(n):
    """
    Calculate the sum of proper divisors for a given number.

    Parameters:
    - n (int): The number for which to calculate the sum of divisors.

    Returns:
    - int: The sum of proper divisors for the given number.
    """
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def find_amicable_numbers(limit):
    """
    Find all amicable numbers below a specified limit.

    Parameters:
    - limit (int): The upper limit for finding amicable numbers.

    Returns:
    - set: A set containing all amicable numbers below the specified limit.
    """
    amicable_numbers = set()

    for a in range(2, limit):
        b = sum_of_divisors(a)
        if b > a and sum_of_divisors(b) == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)

    return amicable_numbers

print(sum(find_amicable_numbers(10000)))
