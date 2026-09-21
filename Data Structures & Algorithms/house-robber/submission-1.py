class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # dp is the maximum amount we can rob from the first i+1 houses
        dp = [0] * (len(nums)) 
        dp[0] = nums[0]  # if there is 1 house you only rob that
        # if 2 houses you rob the one with more money
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # take the current house, since we cant take the last one, we look at the best solution upto i-2
            take = dp[i-2] + nums[i]
            # skip the current house, so just take the best solution upto i-1
            skip = dp[i-1]
            dp[i] = max(take, skip)
        return dp[len(nums) - 1]