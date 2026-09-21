class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            m = l + (r - l) // 2
            if m*m < x: # this means m is valid, coz it must be less than, so we can now set l = m + 1 and set res to m
                l = m + 1
                res = m
            elif m*m > x: # must be smaller, so r = m - 1
                r = m - 1
            else:
                return m # if it is equal we can just return m as exact square root
        return res
        