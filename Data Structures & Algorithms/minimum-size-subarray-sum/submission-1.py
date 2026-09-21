class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf') # we set it to inf at first since we are calculating min, if we set to 0 then min will always give 0 not the minimum size
        total = 0 # total is the current total for the window
        start = 0 # start is our left pointer
        for end in range(len(nums)):
            total += nums[end] # we first add the curr number to the total
            while total >= target: # now we check if the total is greater than or equal to target. if it is, we check the length of the window if its the least we set to min, then we increment the left pointer to try new possibilities(while removing the left value from total as we wont use it)
                res = min(res, end - start + 1)
                total -= nums[start]
                start += 1
        if res == float('inf'):
            return 0 # we return 0 if theres no such subarray(float('inf') stays as it is)
        else:
            return res
        