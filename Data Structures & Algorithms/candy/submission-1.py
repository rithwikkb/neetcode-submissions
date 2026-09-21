class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # initialize with 1 because all children get 1 candy by default
        arr = [1] * n
        # basically we do 2 passes. left to right, and right to left. because a rating can be higher from the left side or the right side
        for i in range(1,n):
            # if the next child has higher rating than previous child, then the number of candies the ith child has should be 1 greater than the (i-1)th child
            if ratings[i-1] < ratings[i]:
                arr[i] = arr[i-1] + 1 
        # right to left
        for i in range(n - 2, -1, -1):

            if ratings[i+1] < ratings[i]:
                arr[i] = max(arr[i],arr[i+1] + 1)
        return sum(arr)


        