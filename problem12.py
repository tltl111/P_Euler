import math

def count_divisors(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2
    if sqrt_n * sqrt_n == n:
        count -= 1
    return count

def required_devisors(num):
    n = 1
    while True:
        triangular = (n * (n + 1)) // 2
        if count_divisors(triangular) >= num:
            return triangular
        n += 1

result = required_devisors(501)
print(result)
