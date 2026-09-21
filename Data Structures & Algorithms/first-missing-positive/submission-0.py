class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        missing = 1
        for i in nums:
            if i > 0 and missing == i:
                missing += 1
        return missing
        