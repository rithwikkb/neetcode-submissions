class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i, eqn in enumerate(equations):
            a, b = eqn
            adj[a].append((b,values[i])) # so we track a/b and also b/a which is why we get the inverse
            adj[b].append((a,1/values[i]))
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            
            q = deque()
            visited = set()
            q.append((src, 1))
            visited.add(src)
            while q:
                node,w = q.popleft()
                # if we reached the target then we return the weight
                if node == target:
                    return w
                for n, wei in adj[node]:
                    if n not in visited:
                        # weight must be multiple since a/b times b/c is a/c so this represents that
                        q.append((n, w * wei))
                        visited.add(n)
            return -1
        res = []
        for i, j in queries:
            res.append(bfs(i,j))
        return res
  