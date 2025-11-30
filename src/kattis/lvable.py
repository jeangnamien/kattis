"""Solution for Kattis problem."""


def lv_able(s):
    """
    Compute the minimum number of operations to make string "lv"-able.

    Problem: https://open.kattis.com/problems/lvable

    Args:
        s (str): Input string

    Returns:
        int: Minimum number of operations needed
    """
    # Case 1: Already contains "lv"
    if "lv" in s:
        return 0

    # Check presence of 'l' and 'v'
    has_l = "l" in s
    has_v = "v" in s

    # Case 2: Both letters present but not adjacent
    if has_l and has_v:
        return 1

    # Case 3: Only one of 'l' or 'v' is present
    if has_l or has_v:
        return 1

    # Case 4: Neither letter present
    return 2


def main():
    """Main function to read input and print output for Kattis."""
    _ = int(input())
    s = input().strip()
    print(lv_able(s))


if __name__ == "__main__":
    main()
