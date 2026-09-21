class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        result = 0
        for i in range(len(s)):
            while s[i] in charset:
                charset.discard(s[l])
                l += 1
            charset.add(s[i])
            result = max(result, i-l+1 )
        return result


        