# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node helps handle edge case where the head itself is removed
        dummy = ListNode(0) # create the node
        dummy.next = head # create the connection
        fast, slow = dummy, dummy # we set our fast and slow pointers to dummy now
        # we move fast pointer n steps ahead to create a gap of n between fast and slow
        for i in range(n): 
            fast = fast.next
        # now we move both pointers until fast reaches the last node
        # so, slow will now be one node before the target node
        while fast.next: 
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next # now that slow is at the node before the target node, changing the pointers will remove the target node
        return dummy.next # we return dummy.next because dummy.next is the head of the linked list