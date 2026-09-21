class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # something can occur upto len(nums) times, 

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # make a list of values, where the index is the count, and a list occurs which lists the numbers which have a certain count 
        for num, cnt in count.items():
            freq[cnt].append(num)
        print(count)
        print(freq)
        res = []
        for i in range(len(freq)-1, 0, -1): # we stop at index 1 because nothing will be there in the 0 index always
            for num in freq[i]:  # now we check the inner list for each frequency( we go backwards as we want the top k)
                res.append(num) #we append to the result
                print(res)
                if len(res) == k: #we check if the length of the current result is equal to k. If it is, then that means that is the top k frequent elements
                    return res

        

