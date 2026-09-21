class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # [(-4,"b"), (-3,"a"),(-2,"c")]
        # count, char = -4, "b"
        # count = -3
        # res = b
        # heap = [(-3,"a"),(-3,"b"),(-2,"c")]
        # count = -3, char = a
        # res = ba
        # count = -2
        # heap  [(-3,"b"),(-2,"a"),(-2,"c")]
        # res = bab
        # heap = [(-2,"a"),(-2,"b"),(-2,"c")]
        # res = baba
        # heap = [(-2,"b"),(-2,"c"), (-1,"a")]
        # res = babab
        # heap = [(-2,"c"), (-1,"a"), (-2,"b")]
        # res = bababcabc
        res = ""
        maxheap = []
        for count, char in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if count !=0:
                heapq.heappush(maxheap,(count,char))
        while maxheap:
            count, char = heapq.heappop(maxheap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxheap:
                    break
                count2, char2 = heapq.heappop(maxheap)
                res += char2
                count2 += 1
                heapq.heappush(maxheap,(count,char))
                if count2:
                    heapq.heappush(maxheap,(count2,char2))
            else:
                res += char
                count += 1
                if count:
                    heapq.heappush(maxheap,(count,char))
        return res
        