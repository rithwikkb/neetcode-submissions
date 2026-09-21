# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == key:
            return self.helper(root)
        dummy = root
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
        return dummy
    def helper(self, root: Optional[TreeNode]):
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        rightchild = root.right
        lastright = self.findlastright(root.left)
        lastright.right = rightchild
        return root.left
    def findlastright(self, root: Optional[TreeNode]):
        while root.right:
            root = root.right
        return root
