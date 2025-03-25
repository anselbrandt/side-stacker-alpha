from copy import deepcopy
from mcts_meta import GameMeta
from mcts_logic import valid, win_condition


class GameState:
    def __init__(self):
        self.board = [[0] * GameMeta.COLS for _ in range(GameMeta.ROWS)]
        self.to_play = GameMeta.PLAYERS["one"]
        self.last_played = None

    def get_board(self):
        return deepcopy(self.board)

    def move(self, pos):
        row, col = pos
        self.board[row][col] = self.to_play
        self.last_played = self.to_play
        self.to_play = (
            GameMeta.PLAYERS["two"]
            if self.to_play == GameMeta.PLAYERS["one"]
            else GameMeta.PLAYERS["one"]
        )

    def get_legal_moves(self):
        return valid(self.board)

    def check_win(self):
        previous_player = (
            GameMeta.PLAYERS["two"]
            if self.to_play == GameMeta.PLAYERS["one"]
            else GameMeta.PLAYERS["one"]
        )
        if self.last_played != None and win_condition(self.board, previous_player):
            return True
        return False

    def game_over(self):
        if self.check_win() or len(self.get_legal_moves()) == 0:
            return True
        else:
            return False

    def get_outcome(self):
        if len(self.get_legal_moves()) == 0 and self.check_win() == False:
            return GameMeta.OUTCOMES["draw"]

        return (
            GameMeta.OUTCOMES["one"]
            if self.check_win() == GameMeta.PLAYERS["one"]
            else GameMeta.OUTCOMES["two"]
        )

    def print(self):
        print("=============================")

        for row in range(GameMeta.ROWS):
            for col in range(GameMeta.COLS):
                print(
                    "| {} ".format(
                        "X"
                        if self.board[row][col] == 1
                        else "O" if self.board[row][col] == 2 else " "
                    ),
                    end="",
                )
            print("|")

        print("=============================")
