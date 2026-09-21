class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        # {}
        stack = ["JFK"]
        res = []

        while stack:
            while adj[stack[-1]]:
                stack.append(adj[stack[-1]].pop())
            res.append(stack.pop())
        return res[::-1]
        