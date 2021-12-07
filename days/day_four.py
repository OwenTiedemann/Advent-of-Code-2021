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


if __name__ == '__main__':
    day_four()
    day_four_part_two()
