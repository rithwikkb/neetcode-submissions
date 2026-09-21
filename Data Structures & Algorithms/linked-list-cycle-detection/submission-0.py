# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow pointer approach. we have 2 pointer: fast, and slow
        # fast moves 2 steps at a time and slow moves 1 step at a time
        # we are looking for a cycle, which means at some point, the fast pointer will lap the slow pointer, meaning they will meet at the same node inside the cycle.
        # so if the slow and fast pointers are equal at some point, then there is a cycle. if not then fast will keep on going till end and loop stops so return false
        # Time complexity O(n) as we traverse the whole linked list, but O(1) space as we arent using extra memory
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False
        