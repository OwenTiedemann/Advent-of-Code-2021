def day_two():
    with open('inputfiles/daytwoinput.txt') as f:
        lines = f.readlines()

    horizontal_position = 0
    depth = 0

    for line in lines:

        line = line.strip().split(" ")

        direction = line[0]
        length = int(line[1])

        if direction == "forward":
            horizontal_position = horizontal_position + length
        elif direction == "down":
            depth = depth + length
        elif direction == "up":
            depth = depth - length

    print(horizontal_position * depth)


def day_two_part_two():
    with open('inputfiles/daytwoinput.txt') as f:
        lines = f.readlines()

    horizontal_position = 0
    depth = 0
    aim = 0

    for line in lines:

        line = line.strip().split(" ")

        direction = line[0]
        length = int(line[1])

        if direction == "forward":
            horizontal_position = horizontal_position + length
            depth = depth + (aim * length)
        elif direction == "down":
            aim = aim + length
        elif direction == "up":
            aim = aim - length

    print(horizontal_position * depth)


if __name__ == '__main__':
    day_two()
    day_two_part_two()
