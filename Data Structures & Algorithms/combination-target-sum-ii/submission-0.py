class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        curr = []
        def dfs(i, total):
            if total == target:
                res.append(curr[:])
                return
            if i == len(candidates) or total > target:
                return
            # choice 1: reuse
            curr.append(candidates[i])
            dfs(i+1, total + candidates[i])
            curr.pop()

            # choice 2: skip but also skip duplicates with while loop
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, total)
        dfs(0,0)
        return res
        