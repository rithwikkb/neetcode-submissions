class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberset = set(nums) # remove all the duplicates
        longest = 0 # result
        for num in numberset: # iterate through the set
            if (num - 1) not in numberset: # check if the previous number is not in the set, if it is not, it means that num is the start of a sequence
                length = 1 # we set length to 1 as we already have one number
                while (num + length) in numberset: # now we check if the next consecutive number is in the set, if it is, we increment length by 1
                    length += 1
                longest = max(length, longest) # finally, we set out longest concequence, to the maximum of the length of the current sequence found and that of the current longest sequence
        return longest


        