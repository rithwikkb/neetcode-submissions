class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        island = 0

        def dfs(r, c):
            stack = [(r,c)]
            grid[r][c] = "0"
            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        stack.append((nr,nc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": #
                    island += 1
                    dfs(r,c)
        return island