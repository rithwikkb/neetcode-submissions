class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = 0
        num = x
        while num:
            res = (res * 10) + (num % 10) # append to res by adding it to the next digit (times 10)
            num //= 10 # remove last digit from num

        return res == x
        