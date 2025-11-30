import pytest
from kattis.thirteen_floors import thirteen_floors


class TestThirteenFloors:
    """Test cases for the thirteen_floors function."""
    
    def test_floors_below_13(self):
        """Test floors below 13 (no change in labeling)."""
        assert thirteen_floors(1) == 1
        assert thirteen_floors(5) == 5
        assert thirteen_floors(10) == 10
        assert thirteen_floors(12) == 12
    
    def test_floor_13_and_above(self):
        """Test floor 13 and above (skip 13 in labeling)."""
        assert thirteen_floors(13) == 14
        assert thirteen_floors(14) == 15
        assert thirteen_floors(15) == 16
        assert thirteen_floors(20) == 21
        assert thirteen_floors(100) == 101
    
    def test_boundary_cases(self):
        """Test boundary cases around floor 13."""
        assert thirteen_floors(11) == 11
        assert thirteen_floors(12) == 12
        assert thirteen_floors(13) == 14
        assert thirteen_floors(14) == 15
    
    def test_first_floor(self):
        """Test the first floor."""
        assert thirteen_floors(1) == 1
    
    def test_large_floor_numbers(self):
        """Test large floor numbers."""
        assert thirteen_floors(50) == 51
        assert thirteen_floors(99) == 100
        assert thirteen_floors(1000) == 1001


class TestKattisExamples:
    """Test cases from problem examples."""
    
    def test_example_floor_12(self):
        """Example: true floor 12 → label 12."""
        assert thirteen_floors(12) == 12
    
    def test_example_floor_13(self):
        """Example: true floor 13 → label 14."""
        assert thirteen_floors(13) == 14
    
    def test_example_floor_14(self):
        """Example: true floor 14 → label 15."""
        assert thirteen_floors(14) == 15


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])