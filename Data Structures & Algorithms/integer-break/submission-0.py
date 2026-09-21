class Solution:
    def integerBreak(self, n: int) -> int:
        # dp = [0,0,0,0,0]
        # dp[1] = 1
        # dp = [0,1,0,0,0]
        # dp = [0,1,2,0,0]
        # dp[2] = max(dp[2], dp[1] * dp[1])
        # dp = [0,1,2,0,0]
        # dp = [0,1,2,3,0]
        # dp[i] is the maximum product you can get by breaking i into at least two positive integers
        dp = [0] * (n + 1)
        dp[1] = 1

        for num in range(2, n + 1):
            # this is to ensure that the target number is not included in the product
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                # now from 1 to num - 1 check all the combinations of products and see if its greater than dp[num] if it is then include that instead
                dp[num] = max(dp[num], dp[i] * dp[num - i])

        return dp[n]