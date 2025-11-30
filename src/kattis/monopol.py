def monopoly_probability(n, hotel_distances):
    """
    Compute the probability of landing on an opponent's hotel.
    
    Args:
        n (int): Number of opponent hotels
        hotel_distances (list): Distances to each hotel
        
    Returns:
        float: Probability that the sum of two dice equals one of the hotel distances
        
    Problem : https://open.kattis.com/problems/monopol  
    """
    # There are 6-sided dice
    sides = 6
    
    # Total number of possible outcomes when rolling two dice
    total_outcomes = sides * sides
    
    # Count the number of favorable outcomes
    favorable = 0
    for i in range(1, sides + 1):
        for j in range(1, sides + 1):
            if i + j in hotel_distances:
                favorable += 1
    
    # Probability = favorable outcomes / total outcomes
    return favorable / total_outcomes


def main():
    n = int(input())
    hotel_distances = list(map(int, input().split()))
    probability = monopoly_probability(n, hotel_distances)
    print(probability)


if __name__ == "__main__":
    main()
