class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = [0] * (n+1)
        adj = [[] for i in range(n+1)]
        #[[],[2,3,4],[1],[1,4],[1,3,5],[4]]
        # indegree = [0,3,1,2,3,1]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        # (2,5)
        q = deque()
        for i in range(1,n+1):
            if indegree[i] == 1:
                q.append(i)
        # node = 2
        # indegree = [0,3,0,2,3,1]
        # indegree = [0,2,0,2,3,1]
        # node = 5
        # indegree = [0,2,0,2,3,5]
        # indegree = [0,2,0,2,2,0]
        # 
        while q:
            node = q.popleft()
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        # 
        for u,v in reversed(edges):
            if indegree[v] == 2 and indegree[u]:
                return [u,v]
        return []
        