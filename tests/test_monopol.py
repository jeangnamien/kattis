import pytest
from kattis.monopol import monopoly_probability

class TestMonopolyProbability:
    """Test cases for the Monopoly dice probability problem."""
    
    def test_single_hotel(self):
        """Test with one hotel distance."""
        assert abs(monopoly_probability(1, [7]) - 6/36) < 1e-6  # 6 ways to roll 7
    
    def test_multiple_hotels(self):
        """Test with multiple hotel distances."""
        # Hotels at 2, 7, 11
        expected = (1 + 6 + 2) / 36  # 2:1, 7:6, 11:2
        assert abs(monopoly_probability(3, [2, 7, 11]) - expected) < 1e-6
    
    def test_all_distances(self):
        """Test with all possible sums."""
        hotel_distances = list(range(2, 13))  # All sums from 2 to 12
        assert abs(monopoly_probability(11, hotel_distances) - 1.0) < 1e-6  # All sums covered
    
    def test_no_hotels(self):
        """Test with zero hotels."""
        assert abs(monopoly_probability(0, []) - 0.0) < 1e-6
    
    def test_edge_cases(self):
        """Test edge cases like minimum and maximum sums."""
        assert abs(monopoly_probability(2, [2, 12]) - (1+1)/36) < 1e-6  # only 2 and 12 possible in one way each

    def test_random_case(self):
        """Random realistic case."""
        # Hotels at 3, 5, 6
        # 3 -> (1,2),(2,1) = 2 ways
        # 5 -> (1,4),(2,3),(3,2),(4,1) = 4 ways
        # 6 -> (1,5),(2,4),(3,3),(4,2),(5,1) = 5 ways
        expected = (2 + 4 + 5)/36
        assert abs(monopoly_probability(3, [3,5,6]) - expected) < 1e-6

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
