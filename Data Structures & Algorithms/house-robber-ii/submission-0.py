class Solution:
    def rob(self, nums: List[int]) -> int:
        # because the houses are circular, a valid solution cannot contain both the first and last house, so we make 2 separate lists excluding the first house and the last house, and run the dp algorithm on both(same as house robber), whatever is greater is the answer
        if len(nums) < 2:
            return nums[0]
        lootskippinglast = self.helper(nums[:-1])
        lootskippingfirst = self.helper(nums[1:])
        return max(lootskippinglast, lootskippingfirst)
        
    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]
        