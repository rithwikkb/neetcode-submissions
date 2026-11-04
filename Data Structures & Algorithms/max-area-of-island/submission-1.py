class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        area = 0

        def dfs(r, c):
            res = 1
            stack = [(r,c)]
            grid[r][c] = 0
            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        stack.append((nr,nc))
                        res += 1
            return res
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    area = max(area, dfs(r,c))
        return area