# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            n1, n2 = curr.val, curr.next.val
            # gcd node points to the original next node, curr points to the gcd node
            curr.next = ListNode(math.gcd(n1, n2), curr.next)
            # now since we have the extra node in between we must step twice
            curr = curr.next.next
        return head
        