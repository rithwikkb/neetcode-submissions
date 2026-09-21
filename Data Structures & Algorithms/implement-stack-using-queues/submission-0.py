class MyStack:
    # as we recall, queue operations are only popleft and append, so you can only remove from the left and add from the right
    # basically we use one queue and rotate the queue after each push so the newest element moves to front

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        # so we add x to the back of the queue
        self.q.append(x)
        for i in range(len(self.q) - 1): # after this we rotate the q by removing elements from the left and adding them to the right, moving x to the front, as we do it (size-1) times, ignoring x
            left = self.q.popleft()
            self.q.append(left)
       
        

    def pop(self) -> int:
        return self.q.popleft() # most recent element is in the front so popleft

    def top(self) -> int:
        return self.q[0] # first element is most recent so just get it by indexing

    def empty(self) -> bool:
        return len(self.q) == 0 # if the queue is empty aka length is 0 we return true
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()