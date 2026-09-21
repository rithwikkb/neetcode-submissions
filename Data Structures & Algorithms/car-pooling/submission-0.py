class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        minheap = [] # this contains [end, numpassengers]
        currpassengers = 0
        for numpass, start, end in trips:
            # if the least ending in the heap is less than or equal to the start time of our current iteration, we can drop those passengers off(pop from heap and remove from currpassengers)
            while minheap and minheap[0][0] <= start:
                currpassengers -= heapq.heappop(minheap)[1]
            # after that we can add current passengers and check the capacity
            heapq.heappush(minheap, [end, numpass])
            currpassengers += numpass
            if currpassengers > capacity:
                return False
            # and then push the current iterations end and number of passengers to the heap
        return True 

        