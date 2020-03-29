import pytest

from sudoku_solver.sudoku import Sudoku


@pytest.fixture()
def solved_sudoku():
    """A fully solved sudoku board."""
    board = [[1, 2, 3, 4],
             [3, 4, 1, 2],
             [2, 3, 4, 1],
             [4, 1, 2, 3]]
    return Sudoku(board, 2)


@pytest.fixture()
def empty_sudoku():
    """An empty sudoku board"""
    board = [["-"] * 4] * 4
    return Sudoku(board, 2)


@pytest.fixture()
def illegal_sudoku():
    """Illegal sudoku board."""
    board = [[1, 1, 3, 4],
             [3, 4, 1, 2],
             [2, 3, 4, 1],
             [4, 1, 2, 3]]
    return Sudoku(board, 2)
