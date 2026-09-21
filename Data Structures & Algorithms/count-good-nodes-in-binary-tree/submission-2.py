# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # a node is a good node if it is greater than all the parents, which means we must get the max along that path and compare it with the curr val if it is greater than or equal to then its good node
        if not root:
            return 0
        res = 0
        # stack should keep track of the node and the maxval in that path
        stack = [(root, root.val)]
        while stack:
            node, maxval = stack.pop()
            if node.val >= maxval:
                res += 1
            maxval = max(maxval, node.val)
            if node.left:
                stack.append((node.left, maxval))
            if node.right:
                stack.append((node.right, maxval))
        return res
