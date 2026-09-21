class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols, w  = len(board), len(board[0]), len(word)
        if rows == 1 and cols == 1:
            return board[0][0] == word
        def dfs(r,c,index):
            if index == w:
                return True
            if word[index] != board[r][c]:
                return False
            char = board[r][c]
            board[r][c] = '0'
            for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr, nc = r + i, c + j
                if 0 <= nr < rows and 0 <= nc < cols:
                    if dfs(nr,nc,index+1):
                        return True
            board[r][c] = char
            return False


        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
        