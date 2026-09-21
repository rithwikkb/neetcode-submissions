class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        # make our dummy nodes
        self.left, self.right = Node(-1), Node(-1)
        # connect those nodes
        self.left.next = self.right
        self.right.prev = self.left
        # initialize space variable

        

    def enQueue(self, value: int) -> bool:
        if self.space == 0:
            return False
        # enquque means we make a new node and connect it to the right side
        curr = Node(value)
        curr.next, curr.prev = self.right, self.right.prev
        self.right.prev.next = curr
        self.right.prev = curr
        self.space -= 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        # front is left node
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # rear is right node
        return self.right.prev.val
        

    def isEmpty(self) -> bool:
        # if its empty then dummy nodes connect to each other
        return self.left.next == self.right
        

    def isFull(self) -> bool:
        # if full space is 0
        return self.space == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()