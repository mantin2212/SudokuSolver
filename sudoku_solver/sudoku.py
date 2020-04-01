from itertools import chain, product
import numpy as np

from sudoku_solver.exc import BoardError
from sudoku_solver import utils


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

    def get_rows(self):
        """
        Return the board rows.
        :return: A list of all board rows.
        :rtype: list
        """
        return utils.copy_matrix(self.board)

    def get_cols(self):
        """
        Return the board columns.
        :return: A list of all board columns.
        :rtype: list
        """
        return np.transpose(self.board)

    def get_blocks(self):
        """
        Return the sudoku blocks from the board.
        :return: A list of the size*size blocks in the board.
        :rtype: list
        """
        block_positions = product(range(self.block_size), range(self.block_size))
        return [self._get_block(i, j) for i, j in block_positions]

    def _get_block(self, row_idx, col_idx):
        """
        Return a sudoku block from the board.
        :param int row_idx: The row-stripe index.
        :param int col_idx: The column-stripe index.
        :return: A size*size sub-board.
        :rtype: list
        """
        start_row = row_idx * self.block_size
        start_col = col_idx * self.block_size

        block_values = self._get_square(start_row, start_col)
        return utils.to_list(block_values)

    def _get_square(self, start_row, start_col):
        """
        Return selected square from the board.
        :param int start_row: The row index to start from.
        :param int start_col: The column index to start from.
        :return: The block_size*block_size square starting from the given coordinates.
        :rtype: list(list)
        """
        end_row = start_row + self.block_size
        end_col = start_col + self.block_size

        result = np.array(self.board)[start_row:end_row,
                                      start_col:end_col]
        return result.tolist()

    @staticmethod
    def _cell_options(board_size):
        options = [str(n) for n in range(1, board_size + 1)]
        return options + [Sudoku.EMPTY_CELL]

    def _cells_iterable(self):
        return chain.from_iterable(zip(self.board))

    def is_legal(self):
        """
        Checks if the sudoku board is legal.
        :return: True if board is legal, and false Otherwise.
        :rtype: bool
        """
        if not self._is_valid():
            return False

        self._check_rows()

        pass

    def _is_valid(self):
        """
        Check if board elements are valid.
        :return: True if board is valid, and False otherwise.
        """
        for cell in self._cells_iterable():
            if cell not in self._valid_elements:
                return False
        return True

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
        for cell in self._cells_iterable():
            if cell == self.EMPTY_CELL:
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
        new_board = utils.copy_matrix(self.board)
        return Sudoku(new_board, self.block_size)
