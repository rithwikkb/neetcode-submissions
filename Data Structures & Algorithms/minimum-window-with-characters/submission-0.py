class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countt = {}
        window = {}
        for i in t: # get occurrences of string t put in countt hashmap
            countt[i] = countt.get(i,0) + 1  
        have = 0 # satisfied chars 
        need = len(countt) # how much we need(distinct chars in t)
        res =  [-1, -1] # res is left and right pointers of the resulting substring
        reslen = float('inf') # len is the length of that substring
        l = 0 # left pointer
        for r in range(len(s)):
            c = s[r] # first we get the curr char
            window[c] = window.get(c, 0) + 1 # add that to the window
            if c in countt and window[c] == countt[c]: # we check if its in countt and if the occurrence is the same, if so, we add to have
                have += 1
            while have == need: # once have is equal to need(like we have 3 chars and 3 are in t)
                if (r - l + 1) < reslen: # now we can check if the substr is less than the reslen
                    res = [l,r] # if so we can set res to our curr left and right pointers
                    reslen = r - l + 1 # and ser reslen to r-l+1
                window[s[l]] -= 1 # now we can decrement from the left
                if s[l] in countt and window.get(s[l], 0) < countt[s[l]]: # if the left pointer is in count and if the frequency of it in window is less than that of t
                    have -= 1 # we have less chars in that case
                l += 1 # since we moved left pointer we increment
        l, r = res # our final res list is the pointers of our substr
        return s[l:r + 1] if reslen != float('inf') else ""