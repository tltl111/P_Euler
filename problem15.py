"""
grid_routes Module

This module provides a function to calculate the number of possible routes
through a grid of given dimensions, moving only down and right at each step.
The grid is represented by 'size_down' (number of downward steps) and
'size_right' (number of rightward steps).

Functions:
    calculate_routes(size_down, size_right):
        Calculate the number of possible routes through the grid.

Example:
    If size_down = 3 and size_right = 3, the `calculate_routes` function will return 20,
    representing the number of routes through a 3x3 grid.

Note:
    The `calculate_routes` function uses combinatorics to calculate the routes.
"""
from math import factorial as f

def calculate_routes(size_down, size_right):
    """
    Calculate the number of possible routes through a grid.

    This function calculates the number of possible routes through a grid
    of given dimensions, moving only down and right at each step. The grid
    is represented by 'size_down' (number of downward steps) and 'size_right'
    (number of rightward steps).

    Parameters:
        size_down (int): The number of downward steps in the grid.
        size_right (int): The number of rightward steps in the grid.

    Returns:
        int: The total number of possible routes through the grid.

    Example:
        If size_down = 3 and size_right = 3, the function will return 20,
        representing the number of routes through a 3x3 grid.

    Note:
        The function uses combinatorics to calculate the routes.
    """
    routes = f(size_down + size_right) // (f(size_down) * f(size_right))
    return routes

print(calculate_routes(20, 20))
