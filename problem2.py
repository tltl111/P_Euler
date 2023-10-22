fibonacci1 = 1
fibonacci2 = 2
sum_of_even = 2 # they wanted the initial first even number 2 aswell, so starting from 2 instead of 0

def adding_fib(fib1, fib2):
    return fib1 + fib2

while fibonacci2 <= 4000000:
    if adding_fib(fibonacci1, fibonacci2) % 2 == 0:
        sum_of_even += adding_fib(fibonacci1, fibonacci2)
    fibonacci1, fibonacci2 = fibonacci2, adding_fib(fibonacci1, fibonacci2)

print(sum_of_even)
