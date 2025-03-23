from math import sqrt

from .logic import Board, new_board, win_condition

from IPython.display import display
import pandas as pd

likelihood_board = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    ["O", None, None, None, None, None, None],
    ["X", None, None, None, None, None, None],
    ["O", None, None, None, None, None, None],
    [None, None, None, None, None, None, 23.67],
    [None, None, None, None, None, 85.43, 45.6],
]


def game_updater(board: Board | None = None, moves=[]):
    if board is None:
        board = new_board()
    turn = 1
    player = "X"
    curr_board = board
    win = False

    for move in moves:
        i, j = move
        curr_board[i][j] = player
        if player == "X":
            player = "O"
        else:
            player = "X"
        if player == "X":
            turn += 1
    winning_condition = win_condition(curr_board, player)
    if winning_condition:
        win = winning_condition

    return (board, turn, player, win)


def get_stats(outcome):
    x, o, tie = outcome
    total = x + o + tie
    x_prob = x / total
    o_prob = o / total
    tie_prob = tie / total
    median = x_prob - o_prob
    variance = (
        ((0 - median) ** 2 * tie_prob)
        + ((1 - median) ** 2 * x_prob)
        + ((-1 - median) ** 2 * o_prob)
    )
    std_dev = sqrt(variance)
    return median


def get_stats_board(likelihood_board):
    result = [
        [get_stats(item) if isinstance(item, tuple) else item for item in row]
        for row in likelihood_board
    ]
    return result


def get_expected_values(likelihood_board: Board, initial_player):
    result = get_stats_board(likelihood_board)

    top_result = [
        (round(value, 3), i, j)
        for i, row in enumerate(result)
        for j, value in enumerate(row)
        if isinstance(value, float)
    ]
    reverse = True if initial_player == "X" else False
    return sorted(top_result, reverse=reverse)


def display_likelihood(board: Board):
    stats_board = [
        [get_stats(item) if isinstance(item, tuple) else item for item in row]
        for row in board
    ]
    df = pd.DataFrame(stats_board).replace({None: ""}).fillna("")
    df = df.apply(
        lambda x: x.map(
            lambda val: (f"{val:.3f}" if isinstance(val, (int, float)) else val)
        )
    )

    def style_table(df):
        return (
            df.style.set_properties(
                **{
                    "border": "1px solid black",
                    "text-align": "center",
                    "width": "30px",
                    "height": "30px",
                    "background-color": "white",
                }
            )
            .hide(axis="index")
            .hide(axis="columns")
        )

    display(style_table(df))
