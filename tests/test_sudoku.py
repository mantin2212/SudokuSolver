from sudoku_solver.sudoku import Sudoku


class TestSudoku(object):

    ### SUDOKU FUNCTIONS TESTS ###
    
    def test_get_row(self, empty_sudoku):
        """ Test sudoku row getter function """
        rows = empty_sudoku.get_rows()

        assert len(rows) == empty_sudoku.size
        self._assert_list(rows[0])

    def test_get_col(self, empty_sudoku):
        """ Test sudoku column getter function """
        cols = empty_sudoku.get_cols()

        assert len(cols) == empty_sudoku.size
        self._assert_list(cols[0])

    def test_get_block(self, empty_sudoku):
        """ Test sudoku block getter function """
        blocks = empty_sudoku.get_blocks()

        assert len(blocks) == empty_sudoku.size
        self._assert_list(blocks[0])

    @staticmethod
    def _assert_list(val):
        """ Assert val is a list """
        return isinstance(val, list)

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

        clone.board[0][0] = 1
        assert original.board[0][0] == Sudoku.EMPTY_CELL
