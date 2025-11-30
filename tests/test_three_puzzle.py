from kattis.three_puzzle import three_puzzle


class TestThreePuzzle:
    """Test cases for the three_puzzle function."""

    def test_already_solved(self):
        """Test when puzzle is already in goal state."""
        assert three_puzzle("123-") == 0

    def test_one_move(self):
        """Test puzzles that require exactly 1 move."""
        assert three_puzzle("12-3") == 1  # Swap - and 3
        assert three_puzzle("1-32") == 1  # Swap - and 2

    def test_various_configurations(self):
        """Test various solvable configurations."""
        assert three_puzzle("12-3") == 1
        assert three_puzzle("1-32") == 1  # Changed from 2 to 1


class TestKattisExamples:
    """Test cases based on Kattis examples."""

    def test_goal_state(self):
        """Test the goal state explicitly."""
        assert three_puzzle("123-") == 0

    def test_simple_swap(self):
        """Test simple adjacent swaps."""
        assert three_puzzle("12-3") == 1
