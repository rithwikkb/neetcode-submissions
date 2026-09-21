class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixsum = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for row in range(len(matrix)):
            self.prefixsum[row][0] = matrix[row][0]
            for col in range(1, len(matrix[0])):
                self.prefixsum[row][col] = self.prefixsum[row][col-1] + matrix[row][col]
        # ex 1, we get [[3,3,4,8,10],[5,11,14,16,17],[1,3,3,4,9],[4,5,5,6,13],[1,1,4,4,9]]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        res = 0
        for row in range(row1,row2+1):
            if col1 > 0:
                res += self.prefixsum[row][col2] - self.prefixsum[row][col1 - 1] # so we get sum from col1 to col2, to do that we subtract the prefix sum upto col2 - the prefix sum upto col1-1(which is the part we wanna exclude)
            else:
                res += self.prefixsum[row][col2] # if col1 is 0 we can just directly get the sum at col2, because -1 would give us the end of the row which is wrong
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)