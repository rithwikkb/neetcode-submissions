# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0 # this is to keep track of the carry 
        while l1 or l2 or carry: # we do or carry because what if in the end we have 7+7 or something where we must add that 1 as well, so in the end even if l1 and l2 are done, if there is a carry we must include that
            # first we get the values for the node we are at
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0
            # add them up, which is val1+val2+carry(0 if no carry)
            val = v1 + v2 + carry
            carry = val // 10 # now we calculate the carry, if val>=10 the carry will be 1 and so on
            val = val % 10 # and if we have a carry we must only count the ones place digit
            curr.next = ListNode(val) # so we set curr.next to that value in a new node
            curr = curr.next # now move to the next node for our new linked list
            l1 = l1.next if l1 else None # and we also move to the next node for the other 2 linked lists
            l2 = l2.next if l2 else None
        return dummy.next 

        