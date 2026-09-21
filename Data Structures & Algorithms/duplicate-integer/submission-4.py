class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(list(set(nums))) != len(nums):
            return True
        return False