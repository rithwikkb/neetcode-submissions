class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        curr = []
        def backtrack(i):
            if len(curr) == len(digits):
                res.append("".join(curr[:]))
                return
            for c in digitToChar[digits[i]]:
                curr.append(c)
                backtrack(i+1)
                curr.pop()
        if digits:
            backtrack(0)
        return res        