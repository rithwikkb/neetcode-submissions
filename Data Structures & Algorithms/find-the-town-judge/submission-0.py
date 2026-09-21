class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # outgoing = {1:1,4:3,2:3}
        # incoming = {3:3}       
        incoming = {}
        outgoing = {}
        for src, dst in trust:
            outgoing[src] = outgoing.get(src,0) + 1
            incoming[dst] = incoming.get(dst,0) + 1
        for i in range(1,n+1):
            if outgoing.get(i,0) == 0 and incoming.get(i,0) == n - 1:
                return i
        return -1
        
        