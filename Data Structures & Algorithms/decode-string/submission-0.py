class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        #stack: "2,[,a,3,[,b"
        # substr = "b", stack = "2,[,a,3"
        # k = 3
        # stack = "2,[,a,bbb"
        # substr = bbb
        # stack = "2,[,a"
        # substring = abbb
        # stack = "2,["
        # stack = "2"
        # stack = "abbbabbbc"

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*substring)
        return "".join(stack)

        