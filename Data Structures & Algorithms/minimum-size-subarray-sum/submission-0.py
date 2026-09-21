class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        total = 0
        start = 0
        for end in range(len(nums)):
            total += nums[end]
            while total >= target:
                res = min(res, end - start + 1)
                total -= nums[start]
                start += 1
        if res == float('inf'):
            return 0
        else:
            return res
        