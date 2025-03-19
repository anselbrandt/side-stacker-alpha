from typing import List, Optional

size = 7

Board = List[List[Optional[str]]]


def new_board() -> Board:
    board: Board = [[None for j in range(size)] for i in range(size)]
    return board


def row_valid(row, i):
    empty = [j for j, value in enumerate(row) if (value == None)]
    if all(value is not None for value in row):
        return []
    return list(set([(i, empty[0]), (i, empty[-1])]))


def valid(board):
    return [cell for i, row in enumerate(board) for cell in row_valid(row, i)]


def check_direction(board, i, j, di, dj, symbol):
    for x in range(4):
        i2, j2 = i + x * di, j + x * dj
        if not (0 <= i2 < size and 0 <= j2 < size) or board[i2][j2] != symbol:
            return False
    return True


def win_condition(board, player):
    directions = [(-1, -1), (-1, 1), (0, 1), (1, 0)]
    labels = ["diag_neg", "diag_pos", "horiz", "vert"]

    for i in range(size):
        for j in range(size):
            if board[i][j] == player:
                for (di, dj), label in zip(directions, labels):
                    if check_direction(board, i, j, di, dj, player):
                        return label

    return False


def next_player(symbol):
    next_player = "O"
    if symbol == "O":
        next_player = "X"
    return next_player
