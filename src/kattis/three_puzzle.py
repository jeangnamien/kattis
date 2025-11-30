"""Solution for Kattis problem."""

from collections import deque


def three_puzzle(grid):
    """
    Find the minimum number of moves to solve a 3-puzzle (2x2 sliding puzzle).

    Problem: https://open.kattis.com/problems/3puzzle

    Uses BFS to find the shortest path from initial state to goal state.
    Goal state: "123-" (tiles 1,2,3 and empty space in row-major order)

    Args:
        grid (str): The initial puzzle state as a 4-character string

    Returns:
        int: Minimum number of moves to solve the puzzle
    """
    goal = "123-"

    if grid == goal:
        return 0

    # BFS setup
    queue = deque([(grid, 0)])  # (state, steps)
    visited = {grid}

    # Possible moves: (row_delta, col_delta)
    # For a 2x2 grid with positions: 0 1
    #                                2 3
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right  # left  # down  # up

    # Helper function to convert position index to (row, col)
    def idx_to_pos(idx):
        return (idx // 2, idx % 2)

    # Helper function to convert (row, col) to position index
    def pos_to_idx(row, col):
        return row * 2 + col

    while queue:
        state, steps = queue.popleft()  # ← Changé de moves à steps

        # Find the empty space position
        empty_idx = state.index("-")
        empty_row, empty_col = idx_to_pos(empty_idx)

        # Try all possible moves
        for dr, dc in directions:
            new_row, new_col = empty_row + dr, empty_col + dc

            # Check if move is valid (within bounds)
            if 0 <= new_row < 2 and 0 <= new_col < 2:
                # Calculate the tile position that will be swapped with empty space
                tile_idx = pos_to_idx(new_row, new_col)

                # Create new state by swapping empty space with tile
                state_list = list(state)
                state_list[empty_idx], state_list[tile_idx] = (
                    state_list[tile_idx],
                    state_list[empty_idx],
                )
                new_state = "".join(state_list)

                # Check if we reached the goal
                if new_state == goal:
                    return steps + 1  # ← Changé de moves à steps

                # Add to queue if not visited
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))  # ← Changé de moves à steps

    # Should never reach here for a solvable puzzle
    return -1


def main():
    """Main function to read input and print output."""
    # Read 2 lines of input, each with 2 characters
    line1 = input().strip()
    line2 = input().strip()

    # Combine into a single string representing the grid
    grid = line1 + line2

    result = three_puzzle(grid)
    print(result)


if __name__ == "__main__":
    main()
