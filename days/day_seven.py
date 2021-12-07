import math
from numpy import median, mean, average


def day_seven():
    with open("inputfiles/dayseveninput.txt") as f:
        lines = f.readlines()

    crab_positions = list(map(int, lines[0].strip().split(",")))

    median_position = median(crab_positions)
    total = 0
    for position in crab_positions:
        fuel_used = abs(position - median_position)
        total += fuel_used

    print(total)


def day_seven_part_two():
    with open("inputfiles/dayseveninput.txt") as f:
        lines = f.readlines()

    crab_positions = list(map(int, lines[0].strip().split(",")))

    mean_position = average(crab_positions)
    rounded_mean = round(mean_position)
    total = 0
    for position in crab_positions:
        n = abs(position - rounded_mean)
        fuel_used = (math.pow(n, 2) + n) / 2
        total += fuel_used

    print(total)


if __name__ == '__main__':
    day_seven_part_two()
