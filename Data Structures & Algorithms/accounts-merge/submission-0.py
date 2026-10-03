class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailtoid = {}
        emails = []
        emailtoacc = {}
        m = 0
        for accid, a in enumerate(accounts):
            for i in range(1, len(a)):
                email = a[i]
                if email in emailtoid:
                    continue
                emails.append(email)
                emailtoid[email] = m
                emailtoacc[m] = accid
                m += 1
  
        adj = [[] for i in range(m)]
        for a in accounts:
            for i in range(2, len(a)):
                id1 = emailtoid[a[i]]
                id2 = emailtoid[a[i-1]]
                adj[id1].append(id2)
                adj[id2].append(id1)
        emailgroup = defaultdict(list)
        visited = [False] * m
        def bfs(start,accid):
            q = deque([start])
            visited[start] = True
            while q:
                node = q.popleft()
                emailgroup[accid].append(emails[node])
                for n in adj[node]:
                    if not visited[n]:
                        visited[n] = True
                        q.append(n)
        for i in range(m):
            if not visited[i]:
                bfs(i,emailtoacc[i])
        res = []
        for i in emailgroup:
            name = accounts[i][0]
            res.append([name] + sorted(emailgroup[i]))  
        return res    