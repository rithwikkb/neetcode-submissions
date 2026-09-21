class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        backtrack([])
        path = [1]
        backtrack([1])
        path = [1,2]
        backtrack([1,2])
        path = [1,2,3]
        backtrack([1,2,3])
        path = [1,2]
        path = [1]
        path = [1,3]
        """
        res = []
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for n in nums:
                if n in path:
                    continue
                path.append(n)
                backtrack(path)
                path.pop()
        backtrack([])
        return res

        