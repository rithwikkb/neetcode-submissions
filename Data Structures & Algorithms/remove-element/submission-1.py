class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        keep = []
        for i in nums:
            if i != val:
                keep.append(i)
            continue
        for i in range(len(keep)):
            nums[i] = keep[i]
        return len(keep)        