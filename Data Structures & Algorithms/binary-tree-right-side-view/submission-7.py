# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        stack = [(1,0)]
        node, depth = 1, 0
        stack = []
        res = [1]
        stack = [(2,1), (3,1)]
        node, depth = 3, 1
        res = [1,3]
        stack = [(2,1), (5,2)]
        node, depth = 5, 2
        stack = [(2,1)]
        res = [1,3,5]
        """
        # first we explore rightmost( as those are first in right side view, and track depth)
        # then we can track left nodes and see if depth is more than current, if so we can add the left node
        if not root:
            return []
        res = []
        def dfs(node, depth):
            if not node:
                return
            # this if statement handles that, for example if the length of res is 3. that means we got 3 nodes on the right side meaning the depth is 2, so to append a left node it must have depth of 3
            if len(res) == depth:
                res.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        dfs(root,0)
        return res