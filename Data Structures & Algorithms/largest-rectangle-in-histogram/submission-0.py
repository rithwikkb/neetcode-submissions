class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = [] # store indices
        heights.append(0) # sentinel val so we can assume that its the shorter bar on the right(calc the area of the remaining bars in the stack)
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]] > h:# if curr is less than the top we start popping
                height = heights[stack.pop()]
                # now we get the boundaries to calculate the area
                if stack:
                    width = i - stack[-1] - 1 # right boundary is the current bar(the one where we stop), left is top of the stack which is the smallest, -1 coz we arent including the curr element(the breaking point) in the height
                else:
                    width = i
                maxarea = max(maxarea, width * height)
            stack.append(i)
        return maxarea



        