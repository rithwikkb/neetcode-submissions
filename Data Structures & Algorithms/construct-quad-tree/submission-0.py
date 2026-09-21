"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':


        def dfs(n,r, c):
            allsame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allsame = False
                        break
            if allsame:
                return Node(grid[r][c], True)
            mid = n//2
            topleft = dfs(mid, r, c)
            topright = dfs(mid, r, c + mid)
            bottomleft = dfs(mid, r + mid,c)
            bottomright = dfs(mid, r + mid,c+mid)
            return Node(0, False, topleft, topright, bottomleft, bottomright)
        return dfs(len(grid), 0, 0)
        