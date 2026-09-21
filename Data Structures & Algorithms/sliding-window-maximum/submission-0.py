class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] 
        q = deque() # queue tracks the candidates for the maximum of the current window. the front is always ensured to be the max
        l = 0 # left poiner
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]: # this ensures that q[0] is always the max of the window, as we pop every element that is lower
                q.pop()
            q.append(r) # now we can append coz we are sure its the max
            if r - l + 1 > k: # now we check if the window size exceeds k, if it does we have to increment the left pointer
                if q[0] == l: # we remove if the element leaving the window is equal to the current max value
                    q.popleft()
                l += 1 # and we can just increment as usual
            if r >= k - 1: # finally we add our max value(front of queue) to the result array if if r >= k -1 coz the first valid window ends at k - 1 so we can safely append once thats fullfilled
                res.append(nums[q[0]])
        return res