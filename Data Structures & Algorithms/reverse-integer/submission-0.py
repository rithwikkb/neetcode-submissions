class Solution:
    def reverse(self, x: int) -> int:
        org = x
        sign = "-" if str(x)[0] == "-" else "+"
        x = abs(x) 
        res = str(x)[::-1]
        if sign == "-":
            res = "-" + res
        if int(res) < -2**31 or int(res)>(2**31-1):
            return 0
        return int(res)