import itertools


def day_eight():
    with open("inputfiles/dayeightinput.txt") as f:
        lines = f.readlines()

    segments_per_number = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    unique_numbers = [1, 4, 7, 8]
    total = 0
    for line in lines:
        line = line.strip().split(" | ")
        signal_patterns = line[0].split()
        output_values = line[1].split()
        for value in output_values:
            if segments_per_number.index(len(value)) in unique_numbers:
                total += 1

    print(total)


def day_eight_part_two():
    with open("inputfiles/dayeightinput.txt") as f:
        lines = f.readlines()

    segments_per_number = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    unique_numbers = [1, 4, 7, 8]

    total = 0

    for line in lines:
        line = line.strip().split(" | ")
        signal_patterns = line[0].split()
        output_values = line[1].split()

        for w in itertools.permutations('abcdefg'):
            print(w)

        break

if __name__ == '__main__':
    day_eight_part_two()
