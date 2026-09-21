class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # very similar to Capacity to Ship Packages Within D Days
        l, r = max(nums), sum(nums) # least possible is the max of the array, most possible is the sum of the array. this is the answer space(the range of answers which is monotonic)
        # basically we do a binary search on the sorted answer space, so for the answer we are trying, we basically simulate filling up each subarray till the answer is reached, and then continue to make a new subarray until its reached, and so on till the end of the nums list, and we count the subarrays and see how it compares to k
        def cansplit(mid):
            subarray, currsum = 1, 0 # we track the number subarrays and the current sum
            for i in nums: # now we iterate the array
                if currsum + i > mid: # we check if the current sum + the weight exceeds the capacity which is mid
                    subarray += 1 # if it exceeds we need a new subarray so we increment
                    currsum = i # i becomes the start of the new subarray
                else:
                    currsum += i # if its within limits we can just add it to the current sum
            return subarray <= k # if the number of subarrays is less than or equal to the limit k we can return true
            
        # since the answer space is monotonic we can just do a binary search instead of a linear search
        while l < r:
            mid = (l + r)//2
            if cansplit(mid):
                r = mid # so basically if it is possible to do it within k subarrays, we can say that m is a possible solution but also explore lesser values since we want the minimum
            else: 
                l = mid + 1 # if its not possible to do it within k subarrays we need to explore greater values
        return l

        