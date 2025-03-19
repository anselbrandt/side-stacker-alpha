size = 7


def select_next(valid_moves, window, player, partial):
    if len(window) == 4 and sum(player in tup for tup in window) >= partial:
        blocking_moves = [(i, j) for symbol, i, j in window if (i, j) in valid_moves]
        if len(blocking_moves):
            return blocking_moves


def partial_horiz(
    board,
    valid_moves,
    i,
    j,
    player,
    partial,
):
    window = [(board[i][j], i, j)]
    for x in range(1, 4):
        j2 = j + x
        if 0 <= i < size and 0 <= j2 < size:
            symbol = board[i][j2]
            if symbol == player or symbol == None:
                window.append((next, i, j2))
    return select_next(valid_moves, window, player, partial)


def partial_vert(
    board,
    valid_moves,
    i,
    j,
    player,
    partial,
):
    window = [(board[i][j], i, j)]
    for x in range(1, 4):
        i2 = i + x
        if 0 <= i2 < size and 0 <= j < size:
            symbol = board[i2][j]
            if symbol == player or symbol == None:
                window.append((symbol, i2, j))
    return select_next(valid_moves, window, player, partial)


def partial_diag_neg(
    board,
    valid_moves,
    i,
    j,
    player,
    partial,
):
    window = [(board[i][j], i, j)]
    for x in range(1, 4):
        i2, j2 = (i + x, j + x)
        if 0 <= i2 < size and 0 <= j2 < size:
            symbol = board[i2][j2]
            if symbol == player or symbol == None:
                window.append((symbol, i2, j2))
    return select_next(valid_moves, window, player, partial)


def partial_diag_pos(
    board,
    valid_moves,
    i,
    j,
    player,
    partial,
):
    window = [(board[i][j], i, j)]
    for x in range(1, 4):
        i2, j2 = (i + x, j - x)
        if 0 <= i2 < size and 0 <= j2 < size:
            symbol = board[i2][j2]
            if symbol == player or symbol == None:
                window.append((symbol, i2, j2))
    return select_next(valid_moves, window, player, partial)


def get_optimal(board, valid_moves, player, partial=2):
    moves = set()
    for i, row in enumerate(board):
        for j, symbol in enumerate(row):
            results = [
                partial_horiz(board, valid_moves, i, j, player, partial),
                partial_vert(board, valid_moves, i, j, player, partial),
                partial_diag_neg(board, valid_moves, i, j, player, partial),
                partial_diag_pos(board, valid_moves, i, j, player, partial),
            ]
            filtered = [result for result in results if result]
            for result in filtered:
                for move in result:
                    moves.add(move)
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
