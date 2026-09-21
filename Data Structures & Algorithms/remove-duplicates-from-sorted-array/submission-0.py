class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        i = j = 0
        n = len(nums) # 5
        # [1,1,2,3,4]
        while j < n:
            nums[i] = nums[j]
            while j < n and nums[j] == nums[i]:
                j += 1
            i += 1
        return i
        """
        numsset = sorted(set(nums))
        nums[:len(numsset)] = numsset
        return len(numsset)