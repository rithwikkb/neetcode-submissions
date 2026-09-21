class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # its a tree if has no cycles and is fully connected
        # tree with n nodes can have at most n - 1 edges so if its more then by default its not a tree
        if len(edges) > n - 1:
            return False
        # build the adjacency list using the connections(undirected graph)
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        # contains the current node and its parent, start from 0, set parent to -1 since there is no parent
        q = deque([(0, -1)]) 
        # root is 0 start from 0
        visited.add(0)
        while q:
            node, parent = q.popleft()
            # check neighbors
            for i in adj[node]:
                # if we encounter the parent, then we skip because we dont want to go back
                if i == parent:
                    continue
                # if its visited then there is a cycle so return False
                if i in visited:
                    return False
                # add to visited
                visited.add(i)
                # append the node along with the parent
                q.append((i, node))
        # return true only if all the nodes are visited(meaning fully connected)
        return len(visited) == n
        