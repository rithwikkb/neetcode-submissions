class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        """
        tempval = []
        tempzero = []
        for i in nums:
            if i != 0:
                tempval.append(i)
            else:
                tempzero.append(i)
        index = 0
        for i in range(len(nums)):
            if i < len(tempval):
                nums[i] = tempval[i]
            else:
                nums[i] = tempzero[index]
                index += 1
            
        
        