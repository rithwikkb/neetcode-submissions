class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # basically in bucket sort we make a list where each index is representing the frequency and the numbers that have that frequency are placed in that index as a list
        # for example if we have [1,2,3,4] as nums
        # then our list will be [[],[1,2,3,4],[],[],[]] as we see we make the list upto index len(nums) as the best case is that everything is the same so itll have frequecncy len(nums)
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        # count basically contains the frequency for each number in the list
        for i in nums:
            count[i] = count.get(i,0) + 1
        # and the list basically contains all the numbers appearing at a certain frequency, where basically each index indicates the frequency, so index 1 is 1 time, 2 is 2 times, etc
        for num,cnt in count.items(): 
            freq[cnt].append(num)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        