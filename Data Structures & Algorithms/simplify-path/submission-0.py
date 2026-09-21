class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        # first split by "/" to get each path
        print(paths)

        for i in paths:
            # if the path is ".." that means it represents a previous directory, so we pop the top of the stack
            if i == "..":
                if stack:
                    stack.pop()
            elif i != "" and i != ".": # if it is not empty or not "." it is valid and we can append to the stack
                stack.append(i)
        return "/"+ "/".join(stack) # finally, in the final answer, we have to add back the "/" as required(with the beginning "/")
