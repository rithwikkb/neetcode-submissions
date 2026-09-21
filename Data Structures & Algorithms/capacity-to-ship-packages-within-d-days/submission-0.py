class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # minimum valid capacity is when all characters individually correspond to a different day, hence the max weight is the least weight capacity
        # maximum valid capacity is when there is just one day so the sum of the list is the least weight capacity.
        # so those are our min and max, aka left and right for the binary search
        l, r = max(weights), sum(weights) 
        def canship(cap): # this basically simulates shipping with our mid value. we greedily fill each day's ship
            ships, remainingcap = 1, cap # this is the number of ships and the remaining capacity
            for i in weights: # so we iterate the weights
                if remainingcap - i < 0: # we check if the ship can hold the weights, we do that by subtracting the capacity by the weight to see if theres weights remaining
                    ships += 1 # if theres no weights remaining we need a new ship so we add a new ship with a fresh capacity for that ship
                    remainingcap = cap 
                remainingcap -= i # we have to decrement the capacity after each iteration as we already used the current weight so our capacity reduces
            return ships <= days # if the number of ships we use is less than or equal to the number of days we have, we are good and can return true
        while l < r: 
            m = (l + r)//2 # get the middle value
            if canship(m): # basically we simulate shipping for the capacity, if it can be shipped within the specified days, we return true
                r = m # if its true that means that value works, and since we want least weight capacity, we can explore lesser values while also keeping this one as its correct
            else: # if we cant ship it means our capacity is too less so we explore greater values
                l = m + 1
        return l
        