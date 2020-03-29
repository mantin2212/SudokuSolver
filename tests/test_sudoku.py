import pytest

from sudoku_solver.exc import SudokuError
from sudoku_solver.sudoku import Sudoku


class TestSudoku(object):

    ### SUDOKU CELL ACCESS TESTS ###

    def test_cell_access(self, empty_sudoku):
        """Test sudoku object cell access."""
        assert empty_sudoku[0][0] == Sudoku.EMPTY_CELL

    def test_set_cell(self, empty_sudoku):
        """Test cell setting."""
        size = empty_sudoku.size

        for value in TestSudoku._sudoku_cell_valid_values(size):
            self._set_cell_test(empty_sudoku, value)

    @staticmethod
    def _sudoku_cell_valid_values(size):
        return list(range(1, size + 1)) + ["-"]

    @staticmethod
    def _set_cell_test(sudoku, value):
        """Changing sudoku cells should change corresponding values in the board."""
        sudoku[0][0] = value
        assert sudoku[0][0] == value
        assert sudoku.board[0][0] == value

    ### SUDOKU FUNCTIONS TESTS ###
    
    def test_get_row(self, empty_sudoku):
        """ Test sudoku row getter function """
        row = empty_sudoku.get_row(0)
        self._assert_list(row)

    def test_get_col(self, empty_sudoku):
        """ Test sudoku column getter function """
        col = empty_sudoku.get_col(0)
        self._assert_list(col)

    def test_get_block(self, empty_sudoku):
        """ Test sudoku block getter function """
        block = empty_sudoku.get_block(0, 0)
        self._assert_block(block)

    @staticmethod
    def _assert_list(val):
        """ Assert val is a list """
        return isinstance(val, list)

    @staticmethod
    def _assert_block(val):
        """ Assert val is a list of lists."""
        assert TestSudoku._assert_list(val)
        assert TestSudoku._assert_list(val[0])

    def test_is_legal(self, solved_sudoku, empty_sudoku, illegal_sudoku):
        """Test sudoku board is_legal function."""
        assert solved_sudoku.is_legal()
        assert empty_sudoku.is_legal()
        assert not illegal_sudoku.is_legal()

    def test_is_solved(self, solved_sudoku, empty_sudoku, illegal_sudoku):
        """Test sudoku board is_solved function."""
        assert solved_sudoku.is_solved()
        assert not empty_sudoku.is_solved()
        assert not illegal_sudoku.is_solved()

    def test_repr(self, empty_sudoku):
        """Assert that sudoku presentation is a valid non-empty string."""
        self._assert_non_empty_string(empty_sudoku.__repr__())

    @staticmethod
    def _assert_non_empty_string(repr_result):
        assert type(repr_result) == str
        assert repr_result

    def test_clone(self, empty_sudoku):
        """Clone changes should not effect original board."""
        original = empty_sudoku
        clone = original.clone()

        clone[0][0] = 1
        assert original[0][0] == Sudoku.EMPTY_CELL
