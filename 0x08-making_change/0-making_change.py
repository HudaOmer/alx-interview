def makeChange(coins, total):
    # Handle edge cases
    if total <= 0:
        return 0
    
    # Initialize the DP array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Fill the DP table
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Check the result
    return dp[total] if dp[total] != float('inf') else -1
