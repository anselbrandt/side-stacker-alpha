size = 7

DIRECTIONS = [
    (0, 1),  # Horizontal
    (1, 0),  # Vertical
    (1, 1),  # Diagonal \
    (1, -1),  # Diagonal /
]


def find_blocking_moves(board, valid_moves, i, j, player, partial):
    moves = set()

    for di, dj in DIRECTIONS:
        window = [(board[i][j], i, j)]

        for x in range(1, 4):
            i2, j2 = i + di * x, j + dj * x

            if 0 <= i2 < size and 0 <= j2 < size:
                symbol = board[i2][j2]
                if symbol == player or symbol is None:
                    window.append((symbol, i2, j2))

        if (
            len(window) == 4
            and sum(1 for sym, _, _ in window if sym == player) >= partial
        ):
            moves.update((i, j) for sym, i, j in window if (i, j) in valid_moves)

    return moves


def get_optimal(board, valid_moves, player, partial=3):
    moves = set()

    for i, row in enumerate(board):
        for j, symbol in enumerate(row):
            moves.update(find_blocking_moves(board, valid_moves, i, j, player, partial))

    return list(moves)


def get_central(valid_moves, tolerance=0):
    i1 = 2 - tolerance
    i2 = 4 + tolerance
    central = [(i, j) for i, j in valid_moves if i1 < i < i2]
    return central


def filter_central(valid_moves, tolerance=0):
    central = get_central(valid_moves, tolerance)
    if len(central):
        return central
    else:
        return valid_moves
