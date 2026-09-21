class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = {}
        for i in nums:
            frequency[i] = 1 + frequency.get(i,0)
        majority = len(nums) // 2
        for key,val in frequency.items():
            if val > majority:
                return key 
        