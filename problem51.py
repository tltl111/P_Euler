from check_for_prime import check_is_prime

REPLACE_NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def create_digits_list():
    digits_list = [5, 6, 7, 8, 3]

    return digits_list

def create_prime_list(number_list):
    prime_list = []

    for _, replacement in enumerate(REPLACE_NUMBERS):
        number_list[2], number_list[3] = replacement, replacement
        new_number = int(''.join(map(str, number_list)))
        if check_is_prime(new_number):
            prime_list.append(new_number)

    return prime_list

def get_lowest_prime_from_list(number_list):
    prime_list = create_prime_list(number_list)

    return min(prime_list)

print(get_lowest_prime_from_list(create_digits_list()))
