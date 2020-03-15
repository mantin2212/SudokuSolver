import pytest

from sudoku_solver.sudoku import Sudoku


@pytest.fixture(scope="module")
def solved_sudoku():
    """A fully solved sudoku board."""
    board = [[1, 2, 3, 4],
             [3, 4, 1, 2],
             [2, 3, 4, 1],
             [4, 1, 2, 3]]
    return Sudoku(board, 2)


@pytest.fixture(scope="module")
def empty_sudoku():
    """An empty sudoku board"""
    board = [["-"] * 4] * 4
    return Sudoku(board, 2)


@pytest.fixture(scope="module")
def illegal_sudoku(solved_sudoku):
    """An illegal sudoku board"""
    illegal_sudoku = solved_sudoku.clone()
    # Two equal cells in the same row.
    illegal_sudoku[0][0] = illegal_sudoku[0][1]
    return illegal_sudoku
