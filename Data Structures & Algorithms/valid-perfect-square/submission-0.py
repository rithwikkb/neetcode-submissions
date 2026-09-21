class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # binary search of possible answers to sqrt(num)
        l, r = 1, num
        while l <= r:
            m = (l + r) // 2
            if m * m == num:
                return True
            elif m * m < num:
                l = m + 1
            else:
                r = m - 1
        return False
        