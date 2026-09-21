# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def getKthNode(temp, k):
            k -= 1
            while temp and k > 0:
                temp = temp.next
                k -= 1
            return temp
        def reverseLinkedList(head):
            prev = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev
        temp = head
        prevLast = None

        while temp:
            kthNode = getKthNode(temp, k)

            # Not enough nodes left
            if kthNode is None:
                if prevLast:
                    prevLast.next = temp
                break

            nextNode = kthNode.next
            kthNode.next = None      # Cut the current group

            # Reverse this group
            newHead = reverseLinkedList(temp)

            if temp == head:
                head = newHead
            else:
                prevLast.next = newHead

            # temp is now the last node after reversal
            prevLast = temp

            # Move to the next group
            temp = nextNode

        return head

        
        