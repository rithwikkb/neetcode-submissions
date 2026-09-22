class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build the adjacency list(undirected graph)
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        def bfs(node):
            q = deque([node])
            visited.add(node)
            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        res = 0
        # nodes from 0 to n-1
        for i in range(n):
            if i not in visited:
                # if we run bfs then the nodes in that component get added to visited, meaning we wont run bfs from those nodes again, guaranteeing that its a connected component
                bfs(i)
                res += 1
        return res


        