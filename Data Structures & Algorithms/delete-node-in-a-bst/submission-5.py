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
        curr = root
        # find the node with same value
        while curr:
            if key < curr.val:
                if curr.left and curr.left.val == key:
                    curr.left = self.helper(curr.left)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = self.helper(curr.right)
                    break
                else:
                    curr = curr.right
        return root
    def helper(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if only one of left or right exists return the opposite
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # now for the case where left and right are there. basically cut the left part and and go to the rightmost left node(greatest), and attach the right node to that as it is bound to be greater
        attachright = root.right
        lastright = self.findlastright(root.left)
        lastright.right = attachright
        return root.left
    def findlastright(self, root):
        while root.right:
            root = root.right
        return root