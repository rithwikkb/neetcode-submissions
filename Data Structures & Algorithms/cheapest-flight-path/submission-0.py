class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijkstras algorithm
        adj = [[] for i in range(n)]
        # dist[u][b] is the minimum cost to reach u using exactly v flights
        # At most k stops means at most k+1 flights
        # We use k+2 columns because dist is is 0 indexed and we also store the starting state
        dist = [[float("inf")] * (k+2) for i in range(n)]
        # since its a directed graph we only append the one edge
        for u,v,cost in flights:
            adj[u].append((v,cost))      
        # from the source node for 0 flights the cost is 0  
        dist[src][0] = 0
        # set up the minheap cost starts with 0 and stops are -1 so that once we take the first flight it becomes 0
        minheap = [(0,src,-1)]
        while minheap:
            cost, node, stops = heapq.heappop(minheap)
            # if we reach the city then return the cheapest cost(minheap guarantees that)
            if node == dst:
                return cost
            # skip if we used the maximum number of stops
            # or we already reached this state with a cheaper cost
            if stops == k or dist[node][stops+1]<cost:
                continue
            for nei,w in adj[node]:
                # add the current weight to the cost and add 1 to the stops
                nextcost = cost + w
                nextstops = stops + 1
                # if this is a cheaper way to reach nei with this number of flights
                # update the distance and add it to the heap
                if dist[nei][nextstops+1] > nextcost:
                    dist[nei][nextstops+1] = nextcost
                    heapq.heappush(minheap,(nextcost, nei, nextstops))
        # if its not possible return -1
        return -1
        