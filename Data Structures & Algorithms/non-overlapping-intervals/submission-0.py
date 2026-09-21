class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals = [[1,2],[1,4],[2,4]]
        # res = 0, prevend = 2
        # res = 1
        # prevend = min(2,4) = 2
        
        intervals.sort(key = lambda x: x[0])
        res = 0
        prevend = intervals[0][1]
        for i in range(1, len(intervals)):
            if prevend > intervals[i][0]:
                res += 1
                prevend = min(prevend, intervals[i][1])
            else:
                prevend = intervals[i][1]
        return res
        