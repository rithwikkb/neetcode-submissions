class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        # we set up the adjacency list
        adj = [[] for _ in range(n)]
        # degree contains the number of edges connected to a node
        degree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        # first we make a queue and initialize it with the leaf nodes
        leaves = deque()
        # if its a leaf node it only has one edge connected to it
        for node in range(n):
            if degree[node] == 1:
                leaves.append(node)
        # if there are 2 or less nodes remaining then thats our solution, because in cases where we got even number of nodes we can have 2 options for middle values, but for odd cases we can have 1 option for a middle value
        while n > 2:
            # now we go over all the leaf nodes and pop them
            for i in range(len(leaves)):
                leaf = leaves.popleft()
                n -= 1
                # for each neighbor, decrement its remaining degree
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    # and after that if its 1 that means its a leaf node so we can append to the queue
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        # whatever we have remaining in the queue is our result
        return list(leaves)      