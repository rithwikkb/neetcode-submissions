class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        inf = 2147483647
        q = deque()
        visited = set()
        # put all treasure chests into the queue. they are all starting points for our BFS.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        steps = 0
        # we run only one bfs starting from all the treasure chests
        while q:
            # process everything at the current distance
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    # check if coordinates are in bounds, not visited, and not a wall
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != -1:
                        visited.add((nr, nc))

                        # if it's an inf room, replace it with the distance from the nearest treasure. we do steps + 1 here because we end up replacing it before we increment steps as a whole(that only happens once we cover the entire level)
                        grid[nr][nc] = steps + 1
                        q.append((nr, nc))

            steps += 1
        