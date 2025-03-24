from game.logic import win_condition

board_horiz = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, "X", "X", "X", "X", None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
]

board_vert = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, "X", None, None, None],
    [None, None, None, "X", None, None, None],
    [None, None, None, "X", None, None, None],
    [None, None, None, "X", None, None, None],
    [None, None, None, None, None, None, None],
]

board_neg = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, "X", None, None, None, None],
    [None, None, None, "X", None, None, None],
    [None, None, None, None, "X", None, None],
    [None, None, None, None, None, "X", None],
    [None, None, None, None, None, None, None],
]

board_pos = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, "X", None, None],
    [None, None, None, "X", None, None, None],
    [None, None, "X", None, None, None, None],
    [None, "X", None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
]


def test_horizontal_win():
    result = win_condition(board_horiz, "X")
    assert result == True, f"Expected True but got {result} for {board_horiz}"


def test_vertical_win():
    result = win_condition(board_vert, "X")
    assert result == True, f"Expected True but got {result} for {board_vert}"


def test_diag_neg_win():
    result = win_condition(board_neg, "X")
    assert result == True, f"Expected True but got {result} for {board_neg}"


def test_diag_pos_win():
    result = win_condition(board_pos, "X")
    assert result == True, f"Expected True but got {result} for {board_pos}"
