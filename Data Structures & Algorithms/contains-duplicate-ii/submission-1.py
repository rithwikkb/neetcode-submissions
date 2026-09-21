class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        start = 0
        for end in range(len(nums)):
            if end - start > k: # if the difference is greater than 3, we remove as invalid. if not, we continue
                window.remove(nums[start])
                start += 1
            if nums[end] in window: # so now since difference is always less than 3, if it is a duplicate(alr in the set), return true
                return True
            window.add(nums[end]) # add the number to the window
        return False # if not return false as no duplicate

        