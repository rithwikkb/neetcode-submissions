class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # we want to minimize the maximum height in the path, so we be greedy and choose the smallest neighbors
        minheap = [[grid[0][0],0,0]] # [time(max height in a path), r, c]
        n = len(grid)
        # check if we visited the coordinate before
        visited = set()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        visited.add((0,0))
        while minheap:
            t, r, c = heapq.heappop(minheap)
            # bottom right coordinates are (n-1,n-1) once we reach we return t
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # we check if nr and nc are in bounds and not visited
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr,nc))
                    # we add the max of the current grid's time and the one before, this means that it only contains the max time in the path
                    heapq.heappush(minheap, [max(t, grid[nr][nc]), nr, nc])