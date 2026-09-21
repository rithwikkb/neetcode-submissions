class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        adj = {tuple(i):[] for i in points}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1 = tuple(points[i])
                p2 = tuple(points[j])
                x1,y1 = p1
                x2,y2 = p2
                dist = abs(x1-x2) + abs(y1-y2)
                adj[p1].append((dist,p2))
                adj[p2].append((dist,p1))
        res = 0
        visited = set()
        start = tuple(points[0])
        minheap = [(0,start)]
        while len(visited) < len(points):
            cost, node = heapq.heappop(minheap)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for neicost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minheap,(neicost, nei))
        return res