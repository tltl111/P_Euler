"""
Module: SundayCounter

This module provides a function to count the number of Sundays that fell on the
first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000).
"""

def is_leap_year(year):
    """
    Check if a given year is a leap year.

    Parameters:
    - year (int): The year to be checked.

    Returns:
    - bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    return False

def count_sundays_on_first_of_month():
    """
    Count the number of Sundays that fell on the first of the month during the
    twentieth century (1 Jan 1901 to 31 Dec 2000).

    Returns:
    - int: The count of Sundays.
    """
    day = 2  # 0 represents Sunday, 1 represents Monday, and so on
    month = 1
    year = 1901

    sunday_count = 0

    while year <= 2000:
        # Check if the current day is a Sunday and the first of the month
        if day == 0:
            sunday_count += 1

        # Move to the next month
        if month in [1, 3, 5, 7, 8, 10, 12]:
            days_in_month = 31
        elif month in [4, 6, 9, 11]:
            days_in_month = 30
        elif is_leap_year(year):
            days_in_month = 29
        else:
            days_in_month = 28

        day = (day + days_in_month) % 7
        month += 1
        if month > 12:
            month = 1
            year += 1

    return sunday_count

RESULT = count_sundays_on_first_of_month()
print(RESULT)
