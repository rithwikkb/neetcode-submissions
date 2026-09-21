class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # we use a queue since the indexes are appended in order so if we want to get the least index we have to pop from the left side and a queue does that efficiently
        D, R = deque(), deque()
        n = len(senate)
        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)
        # we want to remove the nearest neighbor, so we get the smallest index for the Ds and for the Rs, and compare to see which stays, if the index of r is less than d that means r goes first so r bans d, etc
        while D and R:
            dturn = D.popleft()
            rturn = R.popleft()
            # we do r + n to simulate the circular property. for example if the index is 0 then we make + n meaning right after the last element in the original array we would go here
            if rturn < dturn:
                R.append(rturn + n)
            else:
                D.append(dturn + n)
        return "Radiant" if R else "Dire"