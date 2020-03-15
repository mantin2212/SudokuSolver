import pytest

from sudoku_solver.exc import SudokuError
from sudoku_solver.sudoku import Sudoku


class TestSudoku(object):

    def test_cell_access(self, empty_sudoku):
        """Test sudoku object cell access."""
        assert empty_sudoku[0][0] == Sudoku.EMPTY_CELL

    def test_set_cell(self, empty_sudoku):
        empty_sudoku[0][0] = '1'

    def test_cell_invalid_strings(self, empty_sudoku):
        """Sudoku should raise error when setting invalid value to a cell"""
        with pytest.raises(SudokuError):
            empty_sudoku[0][0] = '1234'

        with pytest.raises(SudokuError):
            empty_sudoku[0][0] = '-1'

        with pytest.raises(SudokuError):
            empty_sudoku[0][0] = 1

    def test_is_legal(self, solved_sudoku, empty_sudoku, illegal_sudoku):
        assert solved_sudoku.is_legal()
        assert empty_sudoku.is_solved()
        assert not illegal_sudoku.is_legal()
