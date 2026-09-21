class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pendingtasks = []
        availabletasks = []
        for i, (enqueueTime, processingTime) in enumerate(tasks):
            heapq.heappush(pendingtasks, (enqueueTime, processingTime, i))
        time = 0
        res = []
        while pendingtasks or availabletasks:
            while pendingtasks and pendingtasks[0][0] <= time:
                enqueueTime, processingTime, i = heapq.heappop(pendingtasks)
                heapq.heappush(availabletasks, (processingTime, i))
            # if the heap is empty it means the cpu is idle so we can skip to the next enqueue time of the next pending task and then continue
            if not availabletasks:
                time = pendingtasks[0][0]
                continue
            processingtime, i = heapq.heappop(availabletasks)
            time += processingtime
            res.append(i)
        return res
