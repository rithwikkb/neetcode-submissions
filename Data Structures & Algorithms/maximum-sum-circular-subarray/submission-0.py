class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 2 cases: we wrap around or we dont wrap around, so we basically get the max for both cases and whatever is higher thats the solution
        globalmax, globalmin = nums[0], nums[0]
        currmax, currmin = 0, 0
        total = 0
        for n in nums:
            currmax = max(currmax+n, n)
            currmin = min(currmin+n,n)
            globalmax = max(globalmax, currmax)
            globalmin = min(globalmin, currmin)
            total += n
        # total - globalmin wont work in cases where we global min is sum of the original array, since it would give 0
        # if globalmax is positive that means there is at least one positive subarray, meaning the array is not all negative values. in such cases, the maximum subarray is simply the largest number in the array, which is globalmax
        # globalmin is the minimum-sum contiguous subarray in the normal (non circular) array if the maximum subarray wraps around we can view it as the entire array with that minimum sum subarray removed so total - globalmin gives the maximum wrapping subarray sum
        return max(globalmax, total - globalmin) if globalmax > 0 else globalmax