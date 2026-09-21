class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # same as search in rortated sorted array 1 but we have to skip duplicates, so our if condiitons check for strictly decreasing
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]: # if left is strictly less than mid then left portion is sorted
                if nums[left] <= target < nums[mid]: # we check if target is between left and mid
                    right = mid - 1 # if it is, we explore the left further
                else:
                    left = mid + 1 # if not, we discard and explore right
            elif nums[left] > nums[mid]: # if not then right portion is sorted
                if nums[mid] < target <= nums[right]: # we check if target is between mid and right
                    left = mid + 1 # if its in the range, we explore the right further
                else:
                    right = mid - 1 # if not we discard and explore the left
            else:
                left += 1 # if its a duplicate we skip by increasing left pointer
        return False

        