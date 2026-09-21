class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1,i2 = 0, len(word1)
        j1,j2 = 0, len(word2)
        res = ""
        while i1 < i2 and j1 < j2:
            res += word1[i1]
            res += word2[j1]
            i1 += 1
            j1 += 1

        if i1 >= i2:
            res += word2[j1:]
        if j1 >= j2:
            res += word1[i1:]
        return res
        