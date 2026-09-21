class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        window = {}
        for i in s1: # gets the count of each char in s1
            counts1[i] = counts1.get(i,0) + 1

        l = 0
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1

            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
            if window == counts1:
                return True
        return False
        


        
        
        