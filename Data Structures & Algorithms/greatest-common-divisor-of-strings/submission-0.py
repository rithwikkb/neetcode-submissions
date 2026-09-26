class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if they arent the same when added up then no such string is possible
        if str1 + str2 != str2 + str1:
            return ""
        # now use math.gcd() to get the gcd of the lengths of str1 and str1
        g = math.gcd(len(str1), len(str2))
        # g is the length of the string that divides str1 and str2 so returning the first g characters from str1 will give that string
        return str1[:g]
        