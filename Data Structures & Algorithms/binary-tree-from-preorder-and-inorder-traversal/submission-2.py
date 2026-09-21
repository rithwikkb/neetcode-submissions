# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # first element in preorder is always the root
        root = TreeNode(preorder[0])
        # find that element in inorder, which can divine it into left and right subtrees
        mid = inorder.index(preorder[0])
        # so 1:mid+1 is the left subteree for preorder, and :mid for inorder
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # right subtree is mid+1: for preorder and also mid+1: for inorder
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

        