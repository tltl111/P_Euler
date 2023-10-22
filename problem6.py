def sum_square_numbers(number):
    sum_number = 0

    for x in range(1, number + 1):
        sum_number += x * x

    return sum_number

def square_sum_numbers(number):
    sum_numbers = 0

    for x in range(1, number + 1):
        sum_numbers += x

    return sum_numbers * sum_numbers

def sum_square_difference(number):
    square_sum = square_sum_numbers(number)
    sum_square = sum_square_numbers(number)

    return square_sum - sum_square

print(sum_square_difference(100))
