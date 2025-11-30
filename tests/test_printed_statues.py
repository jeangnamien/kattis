import math
from kattis.printed_statues import printed_statues


class TestPrintedStatues:
    """Test the printed_statues function."""

    def test_small_numbers(self):
        """Test small values of n."""
        assert printed_statues(1) == 1
        assert printed_statues(2) == 2
        assert printed_statues(3) == 3
        assert printed_statues(4) == 3
        assert printed_statues(5) == 4

    def test_powers_of_two(self):
        """Test powers of 2 to check doubling behavior."""
        assert printed_statues(2) == 2
        assert printed_statues(4) == 3
        assert printed_statues(8) == 4
        assert printed_statues(16) == 5
        assert printed_statues(32) == 6

    def test_large_numbers(self):
        """Test larger numbers to verify formula."""
        assert printed_statues(100) == math.ceil(math.log2(100)) + 1
        assert printed_statues(1000) == math.ceil(math.log2(1000)) + 1
        assert printed_statues(10000) == math.ceil(math.log2(10000)) + 1

    def test_formula_matches(self):
        """Check that printed_statues matches formula for 1..100."""
        for n in range(1, 101):
            expected = math.ceil(math.log2(n)) + 1
            assert printed_statues(n) == expected, f"Failed for n={n}"
