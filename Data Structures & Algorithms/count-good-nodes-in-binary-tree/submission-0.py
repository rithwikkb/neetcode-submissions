# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # a node is a good node if it is greater than all the parents, which means we must get the max along that path and compare it with the curr val if it is greater than or equal to then its good node
        # to traverse we do a dfs from the root node
        if not root:
            return 0
        res = 0
        stack = [(root, root.val)]
        while stack:
            node, maxval = stack.pop()
            # if the value is greater than or equal to the max value we can increment res as its a good node
            if node.val >= maxval:
                res += 1
            # maxval is just the max node we have encountered so far
            maxval = max(maxval, node.val)
            # append the left and right nodes to the stack
            if node.left:
                stack.append((node.left, maxval))
            if node.right:
                stack.append((node.right, maxval))
        return res
            
        