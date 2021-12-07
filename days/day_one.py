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


if __name__ == '__main__':
    day_one()
    day_one_part_two()
