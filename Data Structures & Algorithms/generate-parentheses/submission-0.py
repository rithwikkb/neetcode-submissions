class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def backtrack(opencount, closecount):
            if opencount == closecount == n:
                res.append("".join(curr))
                return
            if opencount < n:
                curr.append("(")
                backtrack(opencount+1, closecount) 
                curr.pop()
            if closecount < opencount:
                curr.append(")")
                backtrack(opencount, closecount+1)
                curr.pop()
        backtrack(0,0)
        return res 
