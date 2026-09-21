class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # input is already sorted
        res = []
        for i in range(len(intervals)):
            # case 1: newinterval is before the interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # case 2: newinterval is after the interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # case 3: they merge
            else:
                # we take the minimum of the left end and the maximum of the right end. we just set to newInterval because we could possibly merge it again with the further intervals
                # so we just reassign the newInterval variable as long as we merge and once we stop merging then append to the result
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res

        
        