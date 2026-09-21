class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valuetoindex = {}
        for i,a in enumerate(nums): #enumerate so we get both the index and value at once
            val = target - a #remainder once we subtract the target
            if val in valuetoindex:
                return [valuetoindex[val],i]
            
            valuetoindex[a] = i


        