class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = [False] * len(matrix), [False] * len(matrix[0])
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0
    
        
        