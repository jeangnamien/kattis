from kattis.different import absolute_difference


def test_basic_cases():
    # simple examples
    assert absolute_difference(5, 3) == 2
    assert absolute_difference(3, 5) == 2
    assert absolute_difference(0, 0) == 0
    assert absolute_difference(123, 123) == 0
    assert absolute_difference(100, 0) == 100
