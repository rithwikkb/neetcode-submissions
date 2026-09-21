class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = {}
        for i in nums:
            frequency[i] = 1 + frequency.get(i,0)
        majority = len(nums) // 3
        majorkeys = []
        for key,val in frequency.items():
            if val > majority:
                majorkeys.append(key)
        return majorkeys
        