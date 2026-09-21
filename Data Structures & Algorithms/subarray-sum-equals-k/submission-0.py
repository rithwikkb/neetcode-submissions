class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = 0
        res = 0
        prefix = {0:1}
        for i in nums:
            sums += i
            if (sums - k) in prefix:
                res += prefix[sums-k]
            prefix[sums] = prefix.get(sums,0) + 1
        return res        