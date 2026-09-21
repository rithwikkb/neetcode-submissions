class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer approach(O(n) solution as we would iterate the array once)
        l, r = 0, len(height) - 1
        result = 0 # maximum amount of water value

        while l < r:
            
            currentarea =  min(height[l], height[r]) * (r - l) # get the current area
            result = max(currentarea, result)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return result
