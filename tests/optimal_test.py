from game.engine import get_optimal
from game.logic import valid

board_horiz = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    ["O", "X", "X", None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
]

optimal_horiz = [(2, 3)]

board_vert = [
    ["O", None, None, None, None, None, None],
    ["O", "X", None, None, None, None, None],
    ["O", "X", None, None, None, None, None],
    ["O", None, None, None, None, None, None],
    ["O", None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
]

optimal_vert = [(0, 1), (4, 1), (3, 1)]

board_neg = [
    [None, None, None, None, None, None, None],
    ["O", "X", None, None, None, None, None],
    ["O", "O", "X", None, None, None, None],
    ["O", "O", "O", None, None, None, None],
    ["O", "O", "O", "O", None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
]

optimal_neg = [(4, 4), (3, 3), (0, 0)]

board_pos = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    ["O", "O", "O", "O", None, None, None],
    ["O", "O", "O", "X", None, None, None],
    ["O", "O", "X", None, None, None, None],
    ["O", "X", None, None, None, None, None],
    [None, None, None, None, None, None, None],
]

optimal_pos = [(2, 4), (6, 0)]


def test_horizontal_optimal():
    valid_moves = valid(board_horiz)
    result = get_optimal(board_horiz, valid_moves, "X", partial=2)
    assert result == optimal_horiz, f"Expected {optimal_horiz}, but got {result}"


def test_vertical_optimal():
    valid_moves = valid(board_vert)
    result = get_optimal(board_vert, valid_moves, "X", partial=2)
    assert result == optimal_vert, f"Expected {optimal_vert}, but got {result}"


def test_diag_neg_optimal():
    valid_moves = valid(board_neg)
    result = get_optimal(board_neg, valid_moves, "X", partial=2)
    assert result == optimal_neg, f"Expected {optimal_neg}, but got {result}"


def test_diag_pos_optimal():
    valid_moves = valid(board_pos)
    result = get_optimal(board_pos, valid_moves, "X", partial=2)
    assert result == optimal_pos, f"Expected {optimal_pos}, but got {result}"
