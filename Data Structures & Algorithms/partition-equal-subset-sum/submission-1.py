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
        n = len(nums)
        # dp[i][s]: can we make sum s using the first i elements? so upto index target hence we do target+1
        dp = [[False] * (target + 1) for i in range(n+1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            for s in range(target + 1):
                # same idea as top down but in reverse
                # dont take nums[i - 1]
                dp[i][s] = dp[i - 1][s]
                # take nums[i - 1]
                if s >= nums[i - 1]:
                    dp[i][s] = dp[i][s] or dp[i - 1][s - nums[i - 1]]

        return dp[n][target]

        