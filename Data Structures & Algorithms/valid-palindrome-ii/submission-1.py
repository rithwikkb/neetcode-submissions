class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                skipleft = s[i+1:j+1] # removes l
                skipright = s[i:j] # removes s 
                if skipleft == skipleft[::-1] or skipright == skipright[::-1]:
                    return True
                else:
                    return False
            i,j = i+1,j-1
        return True
        