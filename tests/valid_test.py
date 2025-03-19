from game.logic import valid

board = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
]

valid_moves = [
    (0, 6),
    (0, 0),
    (1, 0),
    (1, 6),
    (2, 0),
    (2, 6),
    (3, 6),
    (3, 0),
    (4, 6),
    (4, 0),
    (5, 0),
    (5, 6),
    (6, 6),
    (6, 0),
]


def test_returns_valid_moves():
    result = valid(board)
    assert result == valid_moves, f"Expected {valid_moves}, but got {result}"
