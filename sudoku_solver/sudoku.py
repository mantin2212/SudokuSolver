from string import digits
from copy import copy

from sudoku_solver.exc import BoardError


class Sudoku(object):
    """ Sudoku puzzle."""

    EMPTY_CELL = "-"

    def __init__(self, board, block_size):
        """
        Initialize sudoku puzzle instance.
        :param board: The sudoku board.
        :type board: list(list(int))
        :param block_size: Sudoku block size.
        """
        self.board = board
        self.size = len(board)
        self.block_size = block_size

        if self.size != block_size * block_size:
            raise BoardError("Board size must be block_size^2.")

        self._valid_elements = Sudoku._cell_options(self.size)

    @staticmethod
    def _cell_options(board_size):
        options = [str(n) for n in range(1, board_size + 1)]
        return options + [Sudoku.EMPTY_CELL]

    def __getitem__(self, index):
        """
        Access sudoku board contents by key.
        :param index: Desired row index from the board.
        :type index: int
        :return: The selected line from the board.
        :rtype: list
        """
        return self.board[index]

    def is_legal(self):
        """
        Checks if the sudoku board is legal.
        :return: True if board is legal, and false Otherwise.
        :rtype: bool
        """
        # TODO Check board.
        pass

    def is_solved(self):
        """
        Checks if the puzzle is solved.
        :return: True if board is validly filled, and False otherwise.
        :rtype: bool
        """
        # Asserting board is valid.
        if not self.is_legal():
            return False

        # Asserting board is filled.
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == self.EMPTY_CELL:
                    return False

        return True

    def __repr__(self):
        # TODO Nicely print the board
        pass

    def clone(self):
        """
        Clone the sudoku board and return the new one.
        :return: A similar sudoku board puzzle.
        :rtype: Sudoku
        """
        new_board = Sudoku._copy_board(self.board)
        return Sudoku(new_board, self.block_size)

    @staticmethod
    def _copy_board(board):
        return [copy(line) for line in board]
