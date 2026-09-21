class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        target = sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False
        memo = {}
        def dfs(i, curr_sum):
            if curr_sum == target:
                return True

            if i == len(nums) or curr_sum > target:
                return False
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            take = dfs(i + 1, curr_sum + nums[i])
            skip = dfs(i + 1, curr_sum)
            memo[(i, curr_sum)] = take or skip
            return memo[(i, curr_sum)]
        return dfs(0,0)
        """
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]