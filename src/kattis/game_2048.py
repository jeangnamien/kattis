"""Solution for Kattis problem."""


def merge_line(line):
    """
    Merge a single line according to 2048 rules.

    Args:
        line (list): A list of 4 integers representing a row/column

    Returns:
        list: The merged line

    Problem : https://open.kattis.com/problems/2048
    """
    # Remove zeros
    non_zero = [num for num in line if num != 0]

    merged = []
    skip = False

    for i, value in enumerate(non_zero):
        if skip:
            skip = False
            continue
        if i + 1 < len(non_zero) and value == non_zero[i + 1]:
            # Merge two tiles
            merged.append(value * 2)
            skip = True
        else:
            merged.append(value)

    # Pad with zeros
    while len(merged) < 4:
        merged.append(0)

    return merged


def move_left(grid):
    """Move all tiles left."""
    return [merge_line(row) for row in grid]


def move_right(grid):
    """Move all tiles right."""
    return [merge_line(row[::-1])[::-1] for row in grid]


def move_up(grid):
    """Move all tiles up."""
    # Transpose grid
    transposed = [[grid[r][c] for r in range(4)] for c in range(4)]
    moved = move_left(transposed)
    # Transpose back
    return [[moved[c][r] for c in range(4)] for r in range(4)]


def move_down(grid):
    """Move all tiles down."""
    transposed = [[grid[r][c] for r in range(4)] for c in range(4)]
    moved = move_right(transposed)
    return [[moved[c][r] for c in range(4)] for r in range(4)]


def game_2048(grid, direction):
    """
    Execute a move in the 2048 game.

    Args:
        grid (list): 4x4 grid
        direction (int): 0=left, 1=up, 2=right, 3=down

    Returns:
        list: New grid after move
    """
    if direction == 0:
        return move_left(grid)
    if direction == 1:
        return move_up(grid)
    if direction == 2:
        return move_right(grid)
    if direction == 3:
        return move_down(grid)
    return grid  # invalid direction


def main():
    """Read input and print output."""
    grid = [list(map(int, input().split())) for _ in range(4)]
    direction = int(input())
    result = game_2048(grid, direction)
    for row in result:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
