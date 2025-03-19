from typing import List, Optional, Union
import pandas as pd
from IPython.display import display

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
