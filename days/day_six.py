def lanterfish(days_to_breed, days_left_to_model):
    days_to_breed = days_to_breed
    total = 1
    for x in range(days_left_to_model, 0, -1):
        if days_to_breed == 0:
            total += lanterfish(8, x - 1)
            days_to_breed = 6
        else:
            days_to_breed -= 1

    return total


def day_six():
    with open("inputfiles/daysixinput.txt") as f:
        lines = f.readlines()

    total = 0
    fish = list(map(int, lines[0].strip().split(",")))

    known_values = {}

    for fishy in fish:
        if fishy in known_values:
            total += known_values[fishy]
        else:
            value = lanterfish(fishy, 80)
            known_values[fishy] = value
            total += value

    print(total)


def day_six_part_two():
    with open("inputfiles/daysixinput.txt") as f:
        lines = f.readlines()

    fish = list(map(int, lines[0].strip().split(",")))

    fish_days = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for fishy in fish:
        fish_days[fishy] += 1

    for x in range(256):
        births = fish_days.pop(0)
        fish_days.append(births)
        fish_days[6] += births

    print(sum(fish_days))


if __name__ == '__main__':
    day_six()
    day_six_part_two()
