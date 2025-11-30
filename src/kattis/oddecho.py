def odd_echo():
    """
    Print every odd-indexed word from the input.
    
    Problem : https://open.kattis.com/problems/oddecho 
    """
    n = int(input())  # number of words
    words = [input().strip() for _ in range(n)]

    # Print words at positions 0, 2, 4, ... (1st, 3rd, 5th, ...)
    for i in range(0, n, 2):
        print(words[i])


if __name__ == "__main__":
    odd_echo()
