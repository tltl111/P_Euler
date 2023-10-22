# from math import sqrt


# def find_pythagorean_awnser(num1, num2):
#     return num1 ** 2 + num2 ** 2

# def check_if_outcome_natural_number(number):
#     is_natural_number = False

#     for x in range(number):
#         if x**2 == number:
#             is_natural_number = True

#     return is_natural_number

# def calculate_number3(num1, num2):
#     num3 = find_pythagorean_awnser(num1, num2)

#     if check_if_outcome_natural_number(num3):
#         num3_sqrt = sqrt(num3)
#         return num3_sqrt
#     else:
#         return 0

# def find_product(number):
#     number1 = 1
#     number2 = 1
#     for _ in range(300):
#         for _ in range(400):
#             number3 = calculate_number3(number1, number2)
#             print(f"number 1: {number1}, number 2: {number2}")
#             if number3 == 0:
#                 number1 += 1
#             else:
#                 outcome = number1 + number2 + number3
#                 if outcome == number:
#                     return number1, number2, number3
#                 else:
#                     number1 += 1
#         number2 += 1
#         number1 = 1

# print(find_product(1000))

for a in range(1, 500):
    for b in range(1, 500):
        for c in range(1, 500):
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                print(a, b, c)