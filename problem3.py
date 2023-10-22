number_to_solve = 600851475143

def largest_prime(number):
    factor = 2
    while factor * factor <= number:
        if number % factor == 0:
            number //= factor
        else:
            factor += 1
    return number

Largest_prime_factor = largest_prime(number_to_solve)

print(Largest_prime_factor)
