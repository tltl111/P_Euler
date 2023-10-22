def is_palindrome(number):
    return str(number) == str(number)[::-1]

def find_largest_palindrome():
    largest_palin = 0

    for i in range(100, 1000):
        for j in range(i, 1000):
            number_sum = i * j
            if number_sum < largest_palin:
                break
            if is_palindrome(number_sum):
                largest_palin = number_sum

    return largest_palin

largest_palindrome = find_largest_palindrome()
print(largest_palindrome)
