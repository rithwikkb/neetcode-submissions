class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # to get the number( as it is in front of '#')
            i = j + 1 # increment i by 1 so we reach the first letter of the world
            j = i + length # add the length so that we reach the end of the word
            res.append(s[i:j]) # now we can get the word and append it
            i = j # we set i to the current j so we can continue the same step for the next word
            
        return res
        

