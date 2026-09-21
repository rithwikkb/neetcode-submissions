class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # check if it the number of cards are divisible by the groupsize
        if len(hand) % groupSize != 0:
            return False
        # now get the frequencies of all the cards
        count = {}
        for i in hand:
            count[i] = 1 + count.get(i,0)
        # minheap contains the unique values which is basically the keys of the hashmap
        minheap = list(count.keys())
        heapq.heapify(minheap)
        while minheap:
            # we get the minimum value in the heap
            first = minheap[0]
            # now check for the consecutive sequence starting from first
            for i in range(first, first + groupSize):
                # if i does not exist in count it means we dont have any cards left so we can return False
                if i not in count:
                    return False
                count[i] -= 1
                #if the count is 0, we pop from the heap
                if count[i] == 0:
                    # if we want to pop a value that is not the minimum value, then we return False
                    if i != minheap[0]:
                        return False
                    del count[i]
                    heapq.heappop(minheap)
        return True
