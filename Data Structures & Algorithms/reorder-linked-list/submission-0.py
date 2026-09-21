# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        first, second = head, prev
        while second.next:
            # alternating merge in essence(rearraging pointers in alternating order)
            tmp1, tmp2 = first.next, second.next
            first.next = second
            first = tmp1
            second.next = first
            second = tmp2
