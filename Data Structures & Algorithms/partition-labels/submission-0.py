class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        {x:3, y:4, z:7, b:9, i:10, s:11, l:12}
        """
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        res = []
        start = end = 0
        # end = 3, i = 0, continue
        # end = 4, i = 1
        # end = 4, i = 2
        # end = 4, i = 3
        # end = 4, i = 4
        # i == end, so res.append(4 - 0 + 1)
        # res = [5]
        # start = 5
        # end = 7, i = 5
        # end = 9, i = 6
        # end = 9, i = 7,
        # end = 9, i = 8
        # end = 9, i = 9
        #. i == end, so res.append(9-5+1)
        # res = [5,5]
        # start = 10
        # end = 10, i = 10
        # res = [5,5,1]
        # start = 11
        # end = 11, i = 11,
        # res = [5,5,1,1]
        # start = 12
        # end = 12, i = 12
        # res = [5,5,1,1,1]
        # start = 13
        # break,
        # return [5,5,1,1,1]
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                res.append(i - start + 1)
                start = i + 1
        return res

        
        