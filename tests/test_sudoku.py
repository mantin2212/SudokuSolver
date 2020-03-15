import pytest

from sudoku_solver.exc import SudokuError
from sudoku_solver.sudoku import Sudoku


class TestSudoku(object):

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

    def test_is_legal(self, solved_sudoku, empty_sudoku, illegal_sudoku):
        assert solved_sudoku.is_legal()
        assert empty_sudoku.is_legal()
        assert not illegal_sudoku.is_legal()
