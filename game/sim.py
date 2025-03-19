from typing import List, Optional, Union

from .logic import Board, new_board, win_condition

from IPython.display import display
import pandas as pd

LikelihooddBoard = List[List[Optional[Union[str, float]]]]

likelihood_board = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    ["O", None, None, None, None, None, None],
    ["X", None, None, None, None, None, None],
    ["O", None, None, None, None, None, None],
    [None, None, None, None, None, None, 23.67],
    [None, None, None, None, None, 85.43, 45.6],
]


def display_likelihood(board: LikelihooddBoard):
    df = pd.DataFrame(board).replace({None: ""}).fillna("")
    df = df.apply(
        lambda x: x.map(
            lambda val: f"{val:.2f}" if isinstance(val, (int, float)) else val
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


def game_updater(board: Board = new_board(), moves=[]):
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
