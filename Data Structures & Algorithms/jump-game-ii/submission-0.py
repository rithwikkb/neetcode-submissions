class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        goal = len(nums) - 1
        while goal > 0:
            for i in range(goal):
                if i + nums[i] >= goal:
                    goal = i
                    res += 1
                    break
        return res
