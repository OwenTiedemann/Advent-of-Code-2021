def day_five():
    with open("inputfiles/dayfiveinput.txt") as f:
        lines = f.readlines()

    diagram = []
    for i in range(0, 1000):
        new = []
        for j in range(0, 1000):
            new.append(0)
        diagram.append(new)

    for line in lines:
        line = line.strip().split(" -> ")
        for i, coordinate in enumerate(line):
            line[i] = coordinate.split(",")

        line_start = line[0]
        line_end = line[1]

        line_start_x = int(line_start[0])
        line_start_y = int(line_start[1])
        line_end_x = int(line_end[0])
        line_end_y = int(line_end[1])

        temp = line_start_x

        if line_start_x > line_end_x:
            line_start_x = line_end_x
            line_end_x = temp

        temp = line_start_y

        if line_start_y > line_end_y:
            line_start_y = line_end_y
            line_end_y = temp

        if line_start_y == line_end_y:
            y = line_start_y
            if line_start_x == line_end_x:
                x = line_start_x
                diagram[y][x] += 1
            else:
                for x in range(line_start_x, line_end_x + 1):
                    diagram[y][x] += 1
        elif line_start_x == line_end_x:

            x = line_start_x
            for y in range(line_start_y, line_end_y + 1):
                diagram[y][x] += 1

    total = 0
    for line in diagram:
        for item in line:
            if item >= 2:
                total += 1

    print(total)


def day_five_part_two():
    with open("inputfiles/dayfiveinput.txt") as f:
        lines = f.readlines()

    diagram = []
    for i in range(0, 1000):
        new = []
        for j in range(0, 1000):
            new.append(0)
        diagram.append(new)

    for line in lines:
        line = line.strip().split(" -> ")
        for i, coordinate in enumerate(line):
            line[i] = coordinate.split(",")

        line_start = line[0]
        line_end = line[1]

        line_start_x = int(line_start[0])
        line_start_y = int(line_start[1])
        line_end_x = int(line_end[0])
        line_end_y = int(line_end[1])

        if line_start_y == line_end_y:
            temp = line_start_x

            if line_start_x > line_end_x:
                line_start_x = line_end_x
                line_end_x = temp

            temp = line_start_y

            if line_start_y > line_end_y:
                line_start_y = line_end_y
                line_end_y = temp
            y = line_start_y
            if line_start_x == line_end_x:
                x = line_start_x
                diagram[y][x] += 1
            else:
                for x in range(line_start_x, line_end_x + 1):
                    diagram[y][x] += 1
        elif line_start_x == line_end_x:
            temp = line_start_x

            if line_start_x > line_end_x:
                line_start_x = line_end_x
                line_end_x = temp

            temp = line_start_y

            if line_start_y > line_end_y:
                line_start_y = line_end_y
                line_end_y = temp
            x = line_start_x
            for y in range(line_start_y, line_end_y + 1):
                diagram[y][x] += 1
        else:
            # print(line_start_x, line_end_x)
            # print(line_start_y, line_start_y)
            if line_start_x > line_end_x:
                x_range = -1
                line_end_x -= 1
            else:
                x_range = 1
                line_end_x += 1
            if line_start_y > line_end_y:
                y_range = -1
                line_end_y -= 1
            else:
                y_range = 1
                line_end_y += 1
            for x, y in zip(range(line_start_x, line_end_x, x_range), range(line_start_y, line_end_y, y_range)):
                diagram[y][x] += 1

    total = 0
    for line in diagram:
        for item in line:
            if item >= 2:
                total += 1

    print(total)

if __name__ == '__main__':
    day_five()
    day_five_part_two()