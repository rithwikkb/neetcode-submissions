class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def bfs():
            # we first set up the queue and add the "O"s at the border to the queue. we start our bfs from the border "O"s
            q = deque()
            for r in range(rows):
                for c in range(cols):
                    if (r == 0 or r == rows -1 or c == 0 or c == cols - 1) and board[r][c] == "O":
                        q.append((r,c))
            # now we run the bfs from the border "O"s and replace the "O"s in the path to T, meaning they are valid and dont have to be replaced
            while q:
                r, c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            q.append((nr,nc))
        bfs()
        # now we have X, O, and T. "O" means its surrounded and can be replaced with X, T means the path contains a border "O" and can be a O so we change it O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"