"""Solution for Kattis problem."""

import math


def printed_statues(n: int) -> int:
    """
    Minimum days to print at least n statues using exponential printer growth.

    Args:
        n (int): Number of statues (1 ≤ n ≤ 10000)

    Returns:
        int: Minimum number of days

    Problem : https://open.kattis.com/problems/3dprinter
    """
    if n == 1:
        return 1
    # Days to get enough printers + 1 day to print all statues
    return math.ceil(math.log2(n)) + 1


def main():
    """Read input and print result."""
    n = int(input())
    print(printed_statues(n))


if __name__ == "__main__":
    main()
