class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]: # if this true it means this portion is sorted
                if nums[left] <= target and target < nums[mid]: # now we check if the target is less than mid and greater than or equal to left, if so we can decrement mid coz thats not the target
                    right = mid - 1
                else:
                    left = mid + 1 # if not then we can increment mid because its surely not in that sorted part
            else: # if not, that means the right half is sorted
                if nums[right] >= target and target > nums[mid]: # now we do the same thing for the right part, we check if its in between, if not we decrement mid
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        
        