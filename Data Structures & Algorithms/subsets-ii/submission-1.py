class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subsets = []
        def dfs(i):
            if i == len(nums):
                res.append(subsets[:])
                return
            # pick
            subsets.append(nums[i])
            dfs(i+1)
            subsets.pop()
            # dont pick. first just skip duplicate indexes, so we call dfs on the next unique index
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
        dfs(0)
        return res

        