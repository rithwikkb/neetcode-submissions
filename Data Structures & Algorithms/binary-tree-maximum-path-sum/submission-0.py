class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        [(-15,False)]
        node, visited = -15, False
        stack = [(-15, True),(20,False),(10,False)]
        stack = [(-15, True),(20,False),(10,True)]
        node, visited = 10, True
        stack = [(-15, True),(20,False)]
        left = 0
        right =0
        res = 10
        gain[10] = 10
        
        

        """
        if not root:
            return 0

        stack = [root]   # (node, visited)
        visited = set()
        gain = {}
        res = float("-inf")

        while stack:
            node = stack.pop()

            if not node:
                continue

            if node in visited:
                left = max(gain.get(node.left, 0), 0)
                right = max(gain.get(node.right, 0), 0)

                res = max(res, node.val + left + right)

                gain[node] = node.val + max(left, right)
            else:
                # left, right, node(since stack we do in opposite order)
                visited.add(node)
                stack.append(node)
                stack.append(node.right)
                stack.append(node.left)
        return res
        