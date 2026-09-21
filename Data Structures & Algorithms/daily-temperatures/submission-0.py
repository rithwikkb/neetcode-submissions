class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) # initialization of the result(this is specified in the question)
        stack = [] # we use this to store (temp, index)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stacktemp, stackindex = stack.pop()
                result[stackindex] = i - stackindex
            stack.append((temperatures[i],i))
        return result