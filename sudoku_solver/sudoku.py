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
        return np.transpose(self.board).tolist()

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

    def _get_stripe(self, stripe_idx):
        start_row = stripe_idx * self.block_size
        end_row = (stripe_idx + 1) * self.block_size

        return self.get_rows()[start_row:end_row]

    @staticmethod
    def _cell_options(board_size):
        options = tuple(range(1, board_size + 1))
        return options + (Sudoku.EMPTY_CELL,)

    def _cells_iterable(self):
        return utils.to_list(self.board)

    def _is_valid(self):
        """
        Check if board elements are valid.
        :return: True if board is valid, and False otherwise.
        """
        for cell in self._cells_iterable():
            if cell not in self._valid_elements:
                return False
        return True

    def is_legal(self):
        """
        Checks if the sudoku board is legal.
        :return: True if board is legal, and false Otherwise.
        :rtype: bool
        """
        if not self._is_valid():
            return False

        if not self._check_all(self.get_rows()):
            return False

        if not self._check_all(self.get_cols()):
            return False

        if not self._check_all(self.get_blocks()):
            return False

        return True

    def _check_all(self, groups):
        """
        Check if all given sudoku groups are legal.
        :param list groups: List of sudoku groups to check.
        :rtype: bool
        """
        for group in groups:
            if not self._check_group(group):
                return False
        return True

    @staticmethod
    def _check_group(group):
        """
        Check if sudoku "board group" is legal.
        Sudoku group is considered illegal if it contains the same number twice.
        :rtype: bool
        """
        filled_cells = Sudoku._filter_empty(group)
        return utils.is_unique(filled_cells)

    @staticmethod
    def _filter_empty(lst):
        """
        Filter empty cells from list.
        :return: List of the non-empty cells.
        :rtype: list
        """
        return [cell for cell in lst if cell is not Sudoku.EMPTY_CELL]

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
        """
        Get a nice display of the sudoku board.
        :return: Representation of the sudoku board.
        :rtype: str
        """
        result = ""
        space_char = "-"

        result += self._repr_space_line(space_char)

        for i in range(self.block_size):
            result += self._stripe_repr(i)
            result += self._repr_space_line(space_char)

        return result

    def _repr_space_line(self, space_char):
        line = [space_char] * self._get_repr_line_length()
        return "".join(line) + "\n"

    def _get_repr_line_length(self):
        return 2 * self.size + 1

    def _repr_stripe(self, stripe_idx):
        stripe_rows = self._get_stripe(stripe_idx)
        result = ""

        for row in stripe_rows:
            result += self._repr_one_row(row)

        return result

    def _repr_one_row(self, row):
        result = ""

    def _stripe_repr(self, stripe_idx):
        return ""

    def clone(self):
        """
        Clone the sudoku board and return the new one.
        :return: A similar sudoku board puzzle.
        :rtype: Sudoku
        """
        new_board = utils.copy_matrix(self.board)
        return Sudoku(new_board, self.block_size)
