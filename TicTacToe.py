# TicTacToe
# Created by Ethan Ratnofsky
# Started on Wednesday, December 22, 2021

"""is_uniform_and_nonnone
Returns True if all elements in the given list lst are the same and not None.
"""
def is_uniform_and_nonnone(lst: list) -> bool:
    if len(lst) == 0:
        return True

    if lst[0] is None:
        return False
    
    return all([element == lst[0] for element in lst])


class TicTacToe:
    def __init__(self, num_rows: int = 3, num_cols: int = 3) -> None:
        assert num_rows > 0 and num_cols > 0
        self.is_game_over = False
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = [[None for _ in range(num_cols)] for _ in range(num_cols)]  # num_rows x num_cols 2D array filled with None values
        self.current_turn = True  # X --> True, O --> False

    """__repr__
    Overload object representation method to print the current state of the board.
    """
    def __repr__(self) -> None:
        string = "\n"

        # Dynamic implementation (sustainable for all board sizes)
        for row_num in range(self.num_rows):
            if row_num > 0:
                # Prepend row partition for all rows except the first
                string += "---" + ("+---" * (self.num_cols - 1)) + "\n"

            for col_num in range(self.num_cols):
                if col_num > 0:
                    # Prepend column partition for column rows except the first
                    string += " |"
                
                mark = self.board[row_num][col_num]
                if mark:
                    string += " X"
                elif mark is False:
                    string += " O"
                else:
                    string += " -"
            string += "\n"

        # # Harcoded implementation (not sustainable for scalability)
        # string += f" {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}"
        # string += "---+---+---"
        # string += f" {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}"
        # string += "---+---+---"
        # string += f" {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}"

        string += "\n"
        return string

    """is_board_full
    Returns True if the board is filled; False otherwise.
    """
    def is_board_full(self) -> bool:
        # Checks for absense of None values in board
        return not any(any(mark is None for mark in row) for row in self.board)
    
    """check_is_won
    Determines whether a player has won; sets self.is_over to True if a player has won.
    """
    def check_is_won(self) -> None:
        rows = self.board
        any_rows_won = any([is_uniform_and_nonnone(row) for row in rows])

        columns = [[self.board[row_num][col_num] for row_num in range(self.num_rows)] for col_num in range(self.num_cols)]
        any_cols_won = any([is_uniform_and_nonnone(column) for column in columns])

        any_diagonals_won = False
        if self.num_rows == self.num_rows:
            first_diagonal = [self.board[i][i] for i in range(self.num_rows)]
            second_diagonal = [self.board[i][self.num_rows - 1 - i] for i in range(self.num_rows)]
            diagonals = [first_diagonal, second_diagonal]
            any_diagonals_won = any([is_uniform_and_nonnone(diagonal) for diagonal in diagonals])

        if any_rows_won or any_cols_won or any_diagonals_won:
            self.is_game_over = True
            return True
        else:
            return False

    """set
    Marks a position on the board with current player's marker.
    """
    def set(self, row_num: int, col_num: int, turn: bool) -> None:
        try:
            if self.board[row_num][col_num] is None:
                self.board[row_num][col_num] = turn
            else:
                print("Spot is non-empty.")
                raise IndexError
        except IndexError:
            print("Invalid board position.")
            raise IndexError
        return

    """start
    Begins a game of Tic-Tac-Toe.
    """
    def start(self) -> None:
        while not self.is_game_over:
            print()
            print(self)
            print()
            print(f"{'X' if self.current_turn else 'O'}'s Turn")
            print()

            is_valid_input = False
            while not is_valid_input:
                raw_in = input("Enter the next move in the form of \"[row_num] [col_num]\": ")
                if len(split_in := raw_in.split()) == 2 and all([arg.isnumeric() for arg in split_in]):
                    try:
                        self.set(int(split_in[0]), int(split_in[1]), self.current_turn)
                        is_valid_input = True
                    except IndexError:
                        pass

            if self.check_is_won():
                print()
                print(self)
                print(f"{'X' if self.current_turn else 'O'} won!")
            elif self.is_board_full():
                print()
                print(self)
                print("Tie game!")
                self.is_game_over = True

            self.current_turn = not self.current_turn

if __name__ == "__main__":
    TicTacToe().start()
