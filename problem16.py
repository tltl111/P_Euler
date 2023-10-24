def calculate_power(number, power):
    result = pow(number, power)
    return result

def calculate_sum(number):
    number_str = str(number)
    number_list = [int(x) for x in number_str]

    summed_number = sum(number_list)

    return summed_number


number_power = calculate_power(2, 1000)
number_sum = calculate_sum(number_power)
print(number_sum)