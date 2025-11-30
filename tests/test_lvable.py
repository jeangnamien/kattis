import pytest
from kattis.lvable import lv_able

def test_lv_present():
    # Contains "lv" as contiguous substring
    assert lv_able("lv") == 0
    assert lv_able("alveolar") == 0  # a-LV-eolar
    assert lv_able("solve") == 0     # so-LV-e
    assert lv_able("lvable") == 0    # LV-able

def test_both_letters():
    # Both letters present but not adjacent
    assert lv_able("vl") == 1
    assert lv_able("vale") == 1
    assert lv_able("love") == 1  # l-o-v-e (not adjacent)

def test_only_l_or_v():
    # Only 'l' or 'v' present
    assert lv_able("l") == 1
    assert lv_able("v") == 1
    assert lv_able("hello") == 1
    assert lv_able("very") == 1

def test_neither_l_nor_v():
    # Neither 'l' nor 'v' present
    assert lv_able("abc") == 2
    assert lv_able("python") == 2
    assert lv_able("xyz") == 2

def test_edge_cases():
    # Single character and minimal strings
    assert lv_able("a") == 2
    assert lv_able("lv") == 0
    assert lv_able("vl") == 1

def test_complex_cases():
    # Complex examples
    assert lv_able("lvable") == 0
    assert lv_able("able") == 1
    assert lv_able("avocado") == 1
    assert lv_able("strength") == 2