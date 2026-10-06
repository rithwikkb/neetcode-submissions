import heapq
class Solution:
    def mergeKLists(self, lists):
        heap = []
        # we add all the linked lists in lists to the min-heap, sorting by the value of the head, we also keep in mind the index of the linked list in the list so in cases where the value is the same it will first show the node with the smaller index
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        # building the final linked list. start with a dummy node for simplicity
        dummy = ListNode(0)
        curr = dummy
        while heap:
            #pop from the heap
            val, i, node = heapq.heappop(heap)
            # set the next node in our new linked list to the node we popped
            curr.next = node
            # and then shift curr to the node we just added
            curr = node
            # if there is a next node, then we add that to the heap so it will sort by the value
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
                