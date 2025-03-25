size = 7


def row_valid(row, i):
    empty = [j for j, value in enumerate(row) if (value == 0)]
    if all(value != 0 for value in row):
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

    for i in range(size):
        for j in range(size):
            if board[i][j] == player:
                for di, dj in directions:
                    if check_direction(board, i, j, di, dj, player):
                        return True

    return False
