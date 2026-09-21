class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 # result variable
        count = {} # count hashmap containing each letter along with frequency
        start = 0 # left pointer at the start of the array
        maxfreq = 0 # the maximum frequent letter
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1 # updating the frequency of each letter
            maxfreq = max(maxfreq, count[s[i]]) # getting the most frequent letter(just the number of times)

            # now we check if the length of the window - the maximum frequency length is greater than k, if it is we should  start removing characters from the left, aka increasing the left pointer, because if it is greater that means it is beyond the limit of switches we have, so we should move our window
            while (i - start + 1) - maxfreq > k: 
                count[s[start]] -= 1
                start += 1
            res = max(res, i-start + 1) # now get the max window(all windows are max since we ensure that only the windoes which contain k characters without a frequent character are there, meaning its valid)
        return res
        