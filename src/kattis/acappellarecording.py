def acappella(n, d, pitches):
    """
    Compute the minimum number of recordings needed.
    
    Notes do NOT need to be consecutive; only the pitch difference matters.
    
    Problem :https://open.kattis.com/problems/acappellarecording
    """
    if n == 0:
        return 0

    pitches.sort()  # sort notes to pack greedily
    recordings = 0
    i = 0

    while i < n:
        # Start a new recording with the smallest remaining note
        recordings += 1
        start_pitch = pitches[i]

        # Include all notes within [start_pitch, start_pitch + d]
        i += 1
        while i < n and pitches[i] - start_pitch <= d:
            i += 1

    return recordings


# Wrapper to run the function from stdin
def main():
    n, d = map(int, input().split())
    pitches = [int(input()) for _ in range(n)]
    print(acappella(n, d, pitches))

if __name__ == "__main__":
    main()
