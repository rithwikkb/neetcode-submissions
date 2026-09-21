class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        counts2 = {}
        for i in s1: # gets the count of each char in s1
            counts1[i] = counts1.get(i,0) + 1

        l = 0
        r = 0
        while r < len(s2): # now we do sliding window of len s1 on s2
            while (r-l) < len(s1) and r < len(s2): # we check if the length of r - l is less than s1(gap cant go beyond that)
                counts2[s2[r]] = counts2.get(s2[r],0) + 1 # during that time we add the counts of s2 chars to hashmap
                r += 1 # and increment r couuter
            if counts1 == counts2: # after that if counts1 equal to counts2 then its a permutation so return true
                return True
            counts2[s2[l]] -= 1 # now we must decrement that seen character by 1 from counts2
            if counts2[s2[l]] == 0: # and if it reaches 0 delete
                del counts2[s2[l]]
            l += 1 # now increment l by 1
        return False


        
        
        