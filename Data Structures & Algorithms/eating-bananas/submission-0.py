class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # 0 to the max eating rate which is just the max value in the pile
        res = r # our res is currently set to r as thats the max eating rate
        while l <= r: # binary search
            m = (l+r) // 2 # mid value
            time = 0
            for i in piles: # this is to get the time basically for each pile based off our m
                time += math.ceil(float(i)/m) # so for [1,4,3,2] and m = 2, itll give 1 + 2+2+1 = 6
            if time <= h: # now that we have the time, we compare it h, if its less than or equal to, we can set it to res, and decrement r, coz now we can only find a time that is lower than that
                res = m
                r = m - 1
            else: # if not, we have to increment l, coz the time has to be greater than m
                l = m + 1
        return res