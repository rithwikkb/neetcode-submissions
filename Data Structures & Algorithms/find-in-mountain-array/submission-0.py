class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        # find peak
        # since we're finding the peak, each number must have one greater and one less, which is why we search from 1 to len(arr) - 2
        l, r = 1, length - 2
        while l <= r:
            m = (l+r)//2
            # now get the mid
            # get the corresponding values. at mid, and the ones next to it
            left, mid, right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)
            # now we can compare, if mid is in the middle and right > mid and left < mid then that is increasing to search right
            if left < mid < right:
                l = m+1
            elif left > mid > right: # if decreaing search left, if not we found peak
                r = m - 1 
            else:
                break
        peak = m
        # search the ascending part(index 0 to the value before peak)
        l, r = 0, peak
        while l <= r:
            m = (l + r)//2
            val = mountainArr.get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m
        # now search the right part(descending)
        l, r = peak+1, length - 1
        while l <= r:
            m = (l+r)//2
            val = mountainArr.get(m)
            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m
        return -1

