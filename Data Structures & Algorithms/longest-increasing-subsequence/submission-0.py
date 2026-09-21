class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # lis[i] is the longest increasing subsequence starting at index i. initialize all to 1. worst case all will be 1 if everything is decreasing.
        lis = [1] * len(nums)
        # go backwards 
        for i in range(len(nums) - 1, -1, -1):
            # for index i iterate over all the values after that 
            for j in range(i+1, len(nums)):
                # this means it is increasing(left value is less than the right), meaning we can add 1 to lis[j] the right value
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
        return max(lis)
        