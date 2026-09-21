class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer approach as there are spaces and we can skip them accordingly in this approach
        left, right = 0, len(s) - 1 #starting index and ending index of the list

        while left < right:  #left must be less than right(as we are checking in order)
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while left < right and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower(): #not a palindrome
                return False
            left += 1
            right -= 1
        return True
            
        
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))