class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # edges contains the node along with the nodes its connected to along with the according weight to reach it
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((w,v))
        minheap = [(0, k)] # cost along with the node we are at(we are at k so 0 cost)
        res = 0
        visited = set() # track visited nodes so we dont explore twice
        while minheap:
            weight, node = heapq.heappop(minheap)
            # if we visited th  node then skip
            if node in visited:
                continue
            # the weight we pop is the minimum so we can set res to that
            visited.add(node)
            res = weight
            # go over the neighbors and if its not visited then add it to the heap but also add the neighbors weight do the current weight since thats the cost to reach the node
            for weight2, node2 in edges[node]:
                if node2 not in visited:
                    heapq.heappush(minheap, (weight + weight2, node2))
        # if we explored all nodes then the length of visited will be n if we didnt explore all nodes then its -1
        return res if len(visited) == n else -1
                
        