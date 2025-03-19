import statistics
from typing import List
from pydantic import BaseModel

from .logic import Board


class Stats(BaseModel):
    turns: List[int]
    ties: List[Board]
    x: List[Board]
    o: List[Board]
    vert: List[Board]
    horiz: List[Board]
    diag: List[Board]
    median: float


def get_stats(results) -> Stats:
    turns: List[int] = []
    ties = []
    x = []
    o = []
    vert = []
    horiz = []
    diag = []

    for result in results:
        player, turn, winning_condition, board = result
        if winning_condition == "tie":
            ties.append(board)
        if "diag_neg" in winning_condition:
            diag.append(board)
        if "diag_pos" in winning_condition:
            diag.append(board)
        if "horiz" in winning_condition:
            horiz.append(board)
        if "vert" in winning_condition:
            vert.append(board)
        if player == "X":
            x.append(board)
        if player == "O":
            o.append(board)
        turns.append(turn)

    median = statistics.median(turns)

    return Stats(
        turns=turns,
        ties=ties,
        x=x,
        o=o,
        vert=vert,
        horiz=horiz,
        diag=diag,
        median=median,
    )
