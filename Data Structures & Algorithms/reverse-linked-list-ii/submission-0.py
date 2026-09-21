# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # first we traverse until the node before reversal and the first node to reverse
        # so we stop at the left node and the node before the left node
        leftprev, curr = dummy, head
        for i in range(left - 1):
            leftprev, curr = curr, curr.next
        prev = None
        # now we reverse the nodes in the window(we get length of the window to identify how many nodes to reverse)
        for i in range(right - left + 1):
            tmp = curr.next # store the next node in a temp value as we have to move to the next node once this is reversed
            curr.next = prev # set the next to the prev
            # moving the prev anc curr pointers
            prev = curr # and set prev to the curr
            curr = tmp # and curr to to the original next
        # After the loop, prev = first node of the reversed sublist (original right node), curr = first node after the reversed sublist
        # so for example, 
        # Original: 1 -> 2 -> 3 -> 4 -> 5
        # we reverse 2 -> 3 -> 4
        #
        # After reversing the window we get
        #
        # 1      4 -> 3 -> 2      5
        #  \_______________|
        #
        # leftprev.next still points to node 2 (the original left node) which is now the tail of the reversed sublist
        # Connect the tail of the reversed sublist (2) to the rest (5)
        # This must happen before changing leftprev.next as that original connection is necessary
        leftprev.next.next = curr
        # now connect the node before the reversed sublist (1) to the new head of the reversed sublist (4)
        leftprev.next = prev
        return dummy.next # as we have a dummy node dummy.next is head

        