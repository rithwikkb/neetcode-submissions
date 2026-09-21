class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        nums.sort(reverse = True)
        if total % k != 0:
            return False
        target = total // k
        sides =[0] * k
        def backtrack(i):
            if i == len(nums):
                return True
            for j in range(k):
                if sides[j] + nums[i] <= target:
                    sides[j] += nums[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= nums[i]
                if sides[j] == 0:
                    break
            return False
        return backtrack(0)
