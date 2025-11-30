"""Solution for Kattis problem."""
import sys

def absolute_difference(a, b):
    """
    Compute the absolute difference between two integers.

    Problem: https://open.kattis.com/problems/different

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Absolute difference |a - b|
    """
    return abs(a - b)





def main():
    """Read input in pairs and print the absolute difference."""
    data = sys.stdin.read().split()

    # process input in pairs
    for i in range(0, len(data), 2):
        a = int(data[i])
        b = int(data[i + 1])
        print(absolute_difference(a, b))


if __name__ == "__main__":
    main()
