import math
from numpy import median, mean, average


def binary_converter(list):
    list.reverse()
    sum = 0
    for i, value in enumerate(list):
        sum = sum + (value * math.pow(2, i))

    return sum


def day_one():
    with open('inputfiles/dayoneinput.txt') as f:
        lines = f.readlines()

    preceding_measurement = int(lines[0])
    times_increases = 0
    for line in lines:
        measurement = int(line)
        if measurement > preceding_measurement:
            times_increases = times_increases + 1

        preceding_measurement = measurement

    print(times_increases)


def day_one_part_two():
    with open('inputfiles/dayoneinput.txt') as f:
        lines = f.readlines()

    times_increases = 0
    sliding_window = []
    for line in lines:
        value = int(line)
        if len(sliding_window) == 3:
            preceding_measurement = sum(sliding_window)
            sliding_window.pop(0)
            sliding_window.append(value)
            measurement = sum(sliding_window)
            if measurement > preceding_measurement:
                times_increases = times_increases + 1
        else:
            sliding_window.append(int(line))

    print(times_increases)


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


class BingoBoard:
    def __init__(self):
        self.board = []
        self.checked_board = []
        self.bingo = {
            "row": [0, 0, 0, 0, 0],
            "col": [0, 0, 0, 0, 0]
        }

    def add_line(self, line):
        line = list(map(int, line))
        self.board.append(line.copy())
        self.checked_board.append(line.copy())

    def check_number(self, number):
        for i, line in enumerate(self.checked_board):
            for j, item in enumerate(line):
                if item == int(number):
                    self.checked_board[i][j] = "X"
                    self.update_bingo(i, j)

    def update_bingo(self, row_index, column_index):
        self.bingo["row"][row_index] += 1
        self.bingo["col"][column_index] += 1

    def check_bingo(self):
        return 5 in self.bingo["row"] or 5 in self.bingo["col"]


def day_four():
    with open("inputfiles/dayfourinput.txt") as f:
        lines = f.readlines()

    numbers = lines[0].strip().split(",")
    lines.pop(0)
    lines.pop(0)
    boards = []
    board = BingoBoard()
    for line in lines:

        if line == "\n":
            boards.append(board)
            board = BingoBoard()
        else:
            board_line = line.strip().split()
            board.add_line(board_line)

    final_number = 0
    for number in numbers:
        for board in boards:
            board.check_number(number)
            if board.check_bingo():
                break
        if board.check_bingo():
            final_number = int(number)
            break

    sum = 0
    for line in board.checked_board:
        for item in line:
            if item != "X":
                sum += item

    print(sum * final_number)


def day_four_part_two():
    with open("inputfiles/dayfourinput.txt") as f:
        lines = f.readlines()

    numbers = lines[0].strip().split(",")
    lines.pop(0)
    lines.pop(0)
    boards = []
    board = BingoBoard()
    for line in lines:

        if line == "\n":
            boards.append(board)
            board = BingoBoard()
        else:
            board_line = line.strip().split()
            board.add_line(board_line)

    final_number = 0
    new_board_list = []
    for number in numbers:
        for board in boards:
            board.check_number(number)
            if not board.check_bingo():
                new_board_list.append(board)
            else:
                if len(boards) == 1:
                    break
        if len(boards) == 1 and board.check_bingo():
            final_number = int(number)
            break

        boards = new_board_list.copy()
        new_board_list = []

    sum = 0
    for i, line in enumerate(board.checked_board):
        for item in line:
            if item != "X":
                sum += item

    print(sum * final_number)


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
        fuel_used = (math.pow(n, 2) + n)/2
        total += fuel_used

    print(total)


if __name__ == '__main__':
    day_seven_part_two()
