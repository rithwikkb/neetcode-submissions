class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i, total):
            if total == target:
                res.append(curr[:])
                return
            # if you reach the end of the array or the total is more than the target, you backtrack
            if i == len(nums) or total > target:
                return
            # include the number, stays at same index because we can reuse
            curr.append(nums[i])
            dfs(i, total + nums[i])
            curr.pop()
            # skip so we move to next index(dont reuse)
            dfs(i+1, total)
        dfs(0,0)
        return res