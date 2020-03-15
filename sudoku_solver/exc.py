

class SudokuError(Exception):
    """Error in the sudoku puzzle"""
    pass


class BoardError(SudokuError):
    """Sudoku board error."""
    pass
