class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        A, B = nums1, nums2
        half = total//2
        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1
        while True:
            # we binary search the smaller array coz that takes less time
            i = (l+r)//2 # we guess the cut basically
            # left size of A = (i+1), left size of b = (j+1) a+b = half so thats why -2
            j = half - i - 2 # j is the cut on the bigger array
            # these 4 are the four numbers around the cuts. conditions are for edge case handling and check if the index is within bounds
            Aleft = A[i] if i >= 0 else float("-infinity") # index must be greater than or equal to 0
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity") # right index must be less than the length of A
            Bleft = B[j] if j >= 0 else float("-infinity") # same goes for B
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            # this means the correct cut is found, basically in our 2 cuts the elements in the  left must be less than the elements in the right across A and B
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total%2 == 1:
                    return min(Aright, Bright)
                else: 
                    return (max(Aleft,Bleft) + min(Aright,Bright))/2
            elif Aleft > Bright: # if Aleft is greater than a right that means left is too big so we must try lower values
                r = i - 1
            else:
                l = i + 1 # if it is too small then we must try bigger values
        

            