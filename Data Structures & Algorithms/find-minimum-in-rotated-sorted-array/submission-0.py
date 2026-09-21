class Solution:
    def findMin(self, nums: List[int]) -> int:
        # basically what we do is reduce search space until only min remains. minimum elment is first element of the rotated part
        l, r = 0, len(nums) - 1
        while l < r:  # we do l<r coz when l==r that means only one left which is the min
            m = (l + r)//2
            if nums[m] < nums[r]: # if mid is less than right, then right half is sorted so the min is either m or left or m, so we set r = m coz of that so we explore the left including m.
                r = m
            else: # if not, right half is not sorted so the rotation starts somewhere there, hence we explore the right further
                l = m + 1
        return nums[l]
        