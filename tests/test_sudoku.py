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
        for value in range(1, size + 1):
            self._set_cell_test(empty_sudoku, value)

    @staticmethod
    def _set_cell_test(sudoku, value):
        """Changing sudoku cells should change corresponding values in the board."""
        sudoku[0][0] = value
        assert sudoku[0][0] == value
        assert sudoku.board[0][0] == value

    def test_cell_invalid_values(self, empty_sudoku):
        """Sudoku should raise error when setting invalid value to a cell"""
        with pytest.raises(SudokuError):
            empty_sudoku[0][0] = '1234'

        with pytest.raises(SudokuError):
            empty_sudoku[0][0] = '-1'

        with pytest.raises(SudokuError):
            empty_sudoku[0][0] = 1

    ### SUDOKU FUNCTIONS TESTS ###

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
