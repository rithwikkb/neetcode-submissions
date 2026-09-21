class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        minheap = [[0,0,0]] # contains difference, r, and c
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        # we use a visited hashset so we dont explore the same position multiple times
        visited = set()
        while minheap:
            diff, r, c = heapq.heappop(minheap) 
            if (r,c) in visited:
                continue
            visited.add((r,c))
            # once we reach the bottom right position, we can just return diff(the one we popped is the minimum diff as we use a minheap)
            if (r,c) == (rows-1,cols-1):
                return diff
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # if the new coordinates are in bounds and not visited, we calculate the new difference and push to the heap
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    # difference is the difference between neighbor position and current position, but we have to add the max difference so we get the max difference in a path
                    newdiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                    # the heap contains all those max differences for each path, so in the end we return the minimum out of those
                    heapq.heappush(minheap,[newdiff,nr,nc])