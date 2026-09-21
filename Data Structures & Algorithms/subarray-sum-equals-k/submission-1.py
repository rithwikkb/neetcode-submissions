class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = 0
        res = 0
        prefix = {0:1}
        for i in nums:
            sums += i
           
            res += prefix.get(sums-k,0)
            prefix[sums] = prefix.get(sums,0) + 1
        return res        