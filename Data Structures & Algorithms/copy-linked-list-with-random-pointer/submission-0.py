"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocopy = {None:None} # edge case when curr.next is None
        curr = head
        # one iteration is to create the nodes in the copy and basically add them to a hashmap(we copy just the values). this is coz of the random pointer coz it can point anywhere so we should create the nodes first
        while curr:
            copy = Node(curr.val)
            oldtocopy[curr] = copy
            curr = curr.next
        # now we do another iteration and use the map to connect the next and random pointers for the copied nodes. now its guaranted that no node is duplicated coz we already copied them in the previous iteration
        curr = head
        while curr:
            copy = oldtocopy[curr]
            copy.next = oldtocopy[curr.next]
            copy.random = oldtocopy[curr.random]
            curr = curr.next
        return oldtocopy[head]    