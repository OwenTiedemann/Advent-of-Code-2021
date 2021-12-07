import math

def binary_converter(list):
    list.reverse()
    sum = 0
    for i, value in enumerate(list):
        sum = sum + (value * math.pow(2, i))

    return sum

def day_three():
    with open("inputfiles/daythreeinput.txt") as f:
        lines = f.readlines()

    total_input = len(lines)
    sum = [0] * len(lines[0].strip())
    count = 0
    for line in lines:
        split = []
        split[:] = line.strip()
        for i, (value, sum_value) in enumerate(zip(split, sum)):
            count = count + 1
            sum_value = sum_value + int(value)
            sum[i] = sum_value

    gamma_rate = [0] * len(lines[0].strip())
    epsilon_rate = [0] * len(lines[0].strip())

    for i, average in enumerate(sum):
        if average <= total_input / 2:
            gamma_rate[i] = 0
            epsilon_rate[i] = 1
        else:
            gamma_rate[i] = 1
            epsilon_rate[i] = 0

    gamma_rate_decimal = binary_converter(gamma_rate)
    epsilon_rate_decimal = binary_converter(epsilon_rate)

    print(gamma_rate_decimal * epsilon_rate_decimal)


def day_three_part_two():
    with open("inputfiles/daythreeinput.txt") as f:
        lines = f.readlines()

    item_length = len(lines[0].strip())

    oxygen_generator_list = lines.copy()
    oxygen_generator_rating = 0
    for x in range(0, item_length):
        total = 0
        for line in oxygen_generator_list:
            split = []
            split[:] = line.strip()
            total = total + int(split[x])

        if total >= len(oxygen_generator_list) / 2:
            most_common_bit = 1
        else:
            most_common_bit = 0

        new_oxygen_generator_list = []
        for line in oxygen_generator_list:
            split = []
            split[:] = line.strip()

            if int(split[x]) == most_common_bit:
                new_oxygen_generator_list.append(line)

        if len(new_oxygen_generator_list) == 1:
            oxygen_generator_rating = int(new_oxygen_generator_list[0].strip())
            break
        else:
            oxygen_generator_list = new_oxygen_generator_list.copy()

    co2_scrubber_list = lines.copy()
    co2_scrubber_rating = 0
    for x in range(0, item_length):
        total = 0
        for line in co2_scrubber_list:
            split = []
            split[:] = line.strip()
            total = total + int(split[x])

        if total >= len(co2_scrubber_list) / 2:
            least_common_bit = 0
        else:
            least_common_bit = 1

        new_co2_scrubber_list = []
        for line in co2_scrubber_list:
            split = []
            split[:] = line.strip()

            if int(split[x]) == least_common_bit:
                new_co2_scrubber_list.append(line)

        if len(new_co2_scrubber_list) == 1:
            co2_scrubber_rating = int(new_co2_scrubber_list[0].strip())
            break
        else:
            co2_scrubber_list = new_co2_scrubber_list.copy()

    oxygen_generator_rating_decimal = binary_converter([int(a) for a in str(oxygen_generator_rating)])

    co2_scrubber_rating_decimal = binary_converter([int(a) for a in str(co2_scrubber_rating)])

    print(oxygen_generator_rating_decimal * co2_scrubber_rating_decimal)


if __name__ == '__main__':
    day_three()
    day_three_part_two()
