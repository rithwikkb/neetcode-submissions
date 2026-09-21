import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # heap sort, since a heap is sorted we can just use heapify to convert the list to a heap and then pop everything using heappop
        heapq.heapify(nums)
        return [heapq.heappop(nums) for i in range(len(nums))]