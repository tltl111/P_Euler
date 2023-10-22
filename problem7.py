# def check_is_prime(number):
#     is_prime = True
#     for x in range(2, number):
#         if number % x == 0:
#             is_prime = False

#     return is_prime

# def list_prime_number(number):
#     prime_amount = 1
#     number_to_check = 3
#     while prime_amount < number:
#         if check_is_prime(number_to_check) == True:
#             prime_amount += 1
#             number_to_check += 1
#         else:
#             number_to_check += 1
#             continue
#     print(f"the {number}'th prime number is the number {number_to_check - 1}")

# list_prime_number(10001)

def check_is_prime(number):
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

def list_prime_number(number):
    if number == 1:
        print("The 1st prime number is 2")
    else:
        prime_amount = 1
        number_to_check = 3
        while prime_amount < number:
            if check_is_prime(number_to_check):
                prime_amount += 1
            number_to_check += 2  # Increment by 2 to check only odd numbers (except 2)
        print(f"The {number}th prime number is {number_to_check - 2}")

list_prime_number(10001)