"""
This module provides functions to process numbers and
find the number with the largest chain of iterations.

The functions in this module are as follows:
- process_odd(number): Process an odd number by multiplying it by 3 and adding 1.
- process_even(number): Process an even number by dividing it by 2.
- process_number(number): Process a number by applying different operations
based on whether it's even or odd, until the number becomes 1.
- largests_chain(): Find the number with the largest chain of iterations among numbers
from 2 to 999,999.

Usage:
To find the number with the largest chain, simply call the largests_chain() function.

Example:
largest_chain_number = largests_chain()
print(f"The number with the largest chain is {largest_chain_number}.")
"""

def process_odd(number):
    """
    Process an odd number by multiplying it by 3 and adding 1.

    Parameters:
    number (int): The input odd number to be processed.

    Returns:
    int: The result of the operation on the input number.
    """
    return number * 3 + 1

def process_even(number):
    """
    Process an even number by dividing it by 2.

    Parameters:
    number (int): The input even number to be processed.

    Returns:
    float: The result of the operation on the input number (a float
    because division can result in a non-integer).
    """
    return number / 2

def process_number(number):
    """
    Process a number by applying different operations based on whether it's even
    or odd, until the number becomes 1.

    Parameters:
    number (int): The input number to be processed.

    Returns:
    int: The number of iterations required to reach 1.
    """
    iteration = 0

    while number > 1:
        iteration += 1
        if number % 2 == 0:
            number = process_even(number)
        else:
            number = process_odd(number)

    return iteration + 1

def largests_chain():
    """
    Find the number with the largest chain of iterations among numbers from 2 to 999,999.

    Returns:
    int: The number with the largest chain.
    """
    chain = 0
    number = 2
    largest_chain_number = 0

    while number < 1000000:
        chain_length = process_number(number)
        number += 1
        print(number)
        if chain_length > chain:
            chain = chain_length
            largest_chain_number = number - 1

    return largest_chain_number

print(largests_chain())
