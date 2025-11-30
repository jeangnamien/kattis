import pytest
from kattis.acappellarecording import acappella

def test_sample_cases():
    # Sample case from problem statement
    assert acappella(6, 0, [3,1,4,1,5,9]) == 5
    assert acappella(3, 3, [1,2,3]) == 1
    assert acappella(3, 1, [1,2,3]) == 2
    assert acappella(5, 0, [1,1,1,1,1]) == 1
    assert acappella(0, 10, []) == 0
