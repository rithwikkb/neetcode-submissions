class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        def backtrack():
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for num in count:
                if count[num] > 0:
                    curr.append(num)
                    count[num] -= 1
                    backtrack()
                    curr.pop()
                    count[num] += 1
        backtrack()
        return res