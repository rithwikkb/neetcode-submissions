import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minnum = min(nums)
        maxnum = max(nums)
        bucket = [0] * (maxnum - minnum + 1)
        for i in nums:
            bucket[i - minnum] += 1
        res = []
        for i, cnt in enumerate(bucket):
            while cnt > 0:
                res.append(i + minnum)
                cnt -= 1
        return res