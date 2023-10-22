multiples_of_3_or_5 = 0

for x in range(1, 1000):
    if x % 3 == 0 or x % 5 == 0:
        multiples_of_3_or_5 += x

print(multiples_of_3_or_5)