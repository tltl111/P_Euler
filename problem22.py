"""
Name Scoring Module

This module provides functions for calculating alphabetical values and total scores
based on a list of names sorted alphabetically.

Functions:
- alphabetical_value(name): Calculate the alphabetical value for a given name.
- calculate_total_score(sorted_names_list): Calculate the total score based on the
  alphabetical values and positions of names in a sorted list.
"""

def alphabetical_value(name):
    """
    Calculate the alphabetical value for a given name.

    Parameters:
    - name (str): The name for which to calculate the alphabetical value.

    Returns:
    - int: The alphabetical value of the name.
    """
    return sum(ord(char) - ord('A') + 1 for char in name)

def calculate_total_score(sorted_names_list):
    """
    Calculate the total score based on the alphabetical values and positions of names.

    Parameters:
    - sorted_names_list (list): A list of names sorted alphabetically.

    Returns:
    - int: The total score.
    """
    total = 0
    for index, name in enumerate(sorted_names_list):
        name_value = alphabetical_value(name)
        name_score = name_value * (index + 1)

        total += name_score

    return total

if __name__ == "__main__":
    with open('names.txt', 'r', encoding='utf-8') as file:
        names_line = file.readline()

    names = [name.strip('"') for name in names_line.split(',')]

    sorted_names = sorted(names)

    print(calculate_total_score(sorted_names))
