class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] is minimum coins needed to make the amount i, initialize with a large number(amount+1 since you cant have that much)
        dp = [0] * (amount + 1)
        for i in range(1, amount+1):
            dp[i] = float('inf')
            for c in coins:
                if c <= i and dp[i - c] != float('inf'):
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != float('inf') else -1