from kattis.game_2048 import (
    game_2048,
    merge_line,
    move_left,
    move_right,
    move_up,
    move_down,
)


def test_merge_line():
    assert merge_line([2, 2, 0, 0]) == [4, 0, 0, 0]
    assert merge_line([2, 2, 2, 2]) == [4, 4, 0, 0]
    assert merge_line([0, 2, 0, 2]) == [4, 0, 0, 0]
    assert merge_line([2, 4, 4, 8]) == [2, 8, 8, 0]


def test_move_left():
    grid = [[2, 2, 0, 0], [2, 0, 2, 2], [0, 0, 0, 0], [2, 2, 2, 2]]
    expected = [[4, 0, 0, 0], [4, 2, 0, 0], [0, 0, 0, 0], [4, 4, 0, 0]]
    assert move_left(grid) == expected


def test_move_right():
    grid = [[2, 2, 0, 0], [2, 0, 2, 2], [0, 0, 0, 0], [2, 2, 2, 2]]
    expected = [[0, 0, 0, 4], [0, 0, 2, 4], [0, 0, 0, 0], [0, 0, 4, 4]]
    assert move_right(grid) == expected


def test_move_up():
    grid = [[2, 0, 2, 0], [2, 0, 2, 0], [0, 0, 0, 0], [2, 0, 2, 0]]
    expected = [[4, 0, 4, 0], [2, 0, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert move_up(grid) == expected


def test_move_down():
    grid = [[2, 0, 2, 0], [2, 0, 2, 0], [0, 0, 0, 0], [2, 0, 2, 0]]
    expected = [[0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 2, 0], [4, 0, 4, 0]]
    assert move_down(grid) == expected


def test_game_2048():
    grid = [[2, 2, 4, 0], [0, 4, 0, 4], [2, 0, 2, 0], [0, 0, 0, 0]]
    result = game_2048(grid, 0)  # move left
    expected = [[4, 4, 0, 0], [8, 0, 0, 0], [4, 0, 0, 0], [0, 0, 0, 0]]
    assert result == expected
