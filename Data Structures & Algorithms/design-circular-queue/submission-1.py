class Node:
    def __init__(self,val):
        self.val, self.next, self.prev = val, None, None
class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left, self.right = Node(-1), Node(-1)
        self.left.next = self.right
        self.right.prev = self.left

        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
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
        # front is the leftmostnode
        return self.left.next.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # reat is the right mostnode
        return self.right.prev.val
        

    def isEmpty(self) -> bool:
        # dummy nodes connect each other
        return self.left.next == self.right
        

    def isFull(self) -> bool:
        # full means space is 0
        return self.space == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()