def count_coin_combinations(target, coins):
    """
    Count the number of coin combinations to make the target value using the given coins.
    """
    combinations = [0] * (target + 1) #creates a list of 0 zeros from index 0-200
    combinations[0] = 1 #So, setting combinations[0] to 1 at the beginning is like saying "We already have the exact amount of money we want with no coins, so there's one possibility." 
    #It's like a starting point for our calculations to count the combinations of coins.

    for coin in coins:
        for i in range(coin, target + 1):
            combinations[i] += combinations[i - coin]

    return combinations[target]


target_value = 200
coin_values = [1, 2, 5, 10, 20, 50, 100, 200]

combination_count = count_coin_combinations(target_value, coin_values)
print(combination_count)
