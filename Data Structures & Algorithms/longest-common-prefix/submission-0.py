class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # [0,1,2]
        #0, continues
        # 1, continues
        # 2, g != t(bag, bat) so we return s[:2] which is ba(index 0,1)
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
        