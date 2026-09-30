class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        # in xor same numbers cancel out resulting in 0
        for num in nums:
            res = num ^ res
        return res
        
        