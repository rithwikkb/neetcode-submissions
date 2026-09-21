class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxprofit = []
        mincapital = [(c,p) for c, p in zip(capital, profits)]
        heapq.heapify(mincapital)
        # [(2,1),(3,3),(3,5),(4,2),(4,3)]
        # pop 2, 1
        # push -1
        # maxprofit = [-1]
        # w += 1
        # w = 3
        # [(3,3),(3,5),(4,2),(4,3)]
        # pop 3,3
        # push -3
        # pop 3,5
        # push -5
        # maxprofit = [-5, -3]
        # add 5
        # w = 8
        # [(4,2), (4,3)]
        # maxprofit = [-3]
        # maxprofit = [-3,-3,-2]
        #
        for i in range(k):
            while mincapital and mincapital[0][0] <= w:
                c, p = heapq.heappop(mincapital)
                heapq.heappush(maxprofit, -p)
            if not maxprofit:
                break
            w += -heapq.heappop(maxprofit)
        return w