class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in num:
                return [num[difference], i]
            num[nums[i]] = i

        