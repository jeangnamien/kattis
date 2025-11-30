def thirteen_floors(floor: int) -> int:
    """
    Return the labeled floor number, skipping floor 13.
    
    Problem: https://open.kattis.com/problems/13floors
    
    Args:
        floor (int): True floor number (1-based)
        
    Returns:
        int: Labeled floor number
    """
    # Floors 1-12 remain the same; 13 and above are incremented
    return floor if floor < 13 else floor + 1


def main():
    """Read input and print labeled floor."""
    floor = int(input())
    print(thirteen_floors(floor))


if __name__ == "__main__":
    main()
