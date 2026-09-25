"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        # sort the intervals by start time(ascending order)
        intervals.sort(key=lambda i: i.start)
        rooms = []
        for interval in intervals:
            # if the earliest ending meeting is finished we can reuse that room
            if rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)
            # assign a room to this meeting(min heap contains the end times)
            heapq.heappush(rooms, interval.end)
        return len(rooms)