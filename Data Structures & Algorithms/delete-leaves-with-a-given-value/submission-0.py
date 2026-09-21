# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [(root,False)]
        parents = {root:None}
        while stack:
            node, visited = stack.pop()
            if not node.left and not node.right:
                if node.val == target:
                    p = parents[node]
                    if not p:
                        return None
                    if p.left == node:
                        p.left = None
                    if p.right == node:
                        p.right = None
            elif not visited:
                stack.append((node,True))
                if node.left:
                    stack.append((node.left, False))
                    parents[node.left] = node
                if node.right:
                    stack.append((node.right,False))
                    parents[node.right] = node
        return root
                
        