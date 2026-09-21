class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # 1 character in the middle
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                # moving outwards
                l -= 1
                r += 1
            # 2 characters in the middle
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                # moving outwards
                l -= 1
                r += 1
        return res
        