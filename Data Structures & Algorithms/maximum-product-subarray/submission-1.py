class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        leftproduct, rightproduct = 1, 1
        for i in range(len(nums)):
            if leftproduct == 0:
                leftproduct = 1
            if rightproduct == 0:
                rightproduct = 1
            leftproduct *= nums[i]
            rightproduct *= nums[len(nums) - 1 - i]
            res = max(res, max(leftproduct, rightproduct))
            
        return res
        