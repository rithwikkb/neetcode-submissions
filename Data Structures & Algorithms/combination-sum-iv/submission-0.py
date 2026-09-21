class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 0 maps to 1 because there is one way to make sum 0(do nothing)
        # dp[i] is the number of ordered sequences using nums that sums to i
        dp = { 0 : 1 }
        for total in range(1, target + 1):
            dp[total] = 0
            for num in nums:
                dp[total] += dp.get(total - num, 0)
        return dp[target]
        