class Solution:
    def numSquares(self, n: int) -> int:
        """
        n = 13
        dp = [13,13,13,13,13,13,13,13,13,13,13,13,13,13]
        dp = [0,13,13,13,13,13,13,13,13,13,13,13,13,13]
        
        """
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]
        