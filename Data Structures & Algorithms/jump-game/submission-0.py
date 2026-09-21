class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # we go backwards from the target
        # the goal represents the leftmost index we currently know can reach the end
        # initially, the last index is our goal
        goal = len(nums) - 1
        # check each index from right to left, starting from the second last index
        for i in range(len(nums) - 2, -1, -1):
            # if we can jump from index i to the current goal, then i becomes our new goal.
            if i + nums[i] >= goal:
                goal = i

        # if the goal reaches index 0, we know the start can reach the end
        return goal == 0
        