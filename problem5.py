run = True
i = 1

def check_evenly_divisible(number, divisible_by):
    evenly_divisible = False
    number_list = [x for x in range(1, divisible_by + 1)]

    for i in number_list:
        if number % i == 0:
            evenly_divisible = True
        else:
            return False

    return evenly_divisible

while run:
    first_encounter = check_evenly_divisible(i, 20)
    if first_encounter == False:
        i += 1
        continue
    else:
        print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {i}")
        run = False
