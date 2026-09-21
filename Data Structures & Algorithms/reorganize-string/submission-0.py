class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = []
        for char, cnt in count.items():
            heapq.heappush(maxheap, [-cnt, char])
        prev = None
        res = ""
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            cnt, char = heapq.heappop(maxheap)
            res += char
            cnt += 1
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res