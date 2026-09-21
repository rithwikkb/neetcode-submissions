class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.left, self.right = Node(0, 0), Node(0, 0)  # Dummy head/tail
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def pop_left(self):
        lru = self.left.next
        self.remove(lru)
        return lru

class LRUCache(DoublyLinkedList):
    def __init__(self, capacity: int):
        super().__init__()
        self.cap = capacity
        self.cache = {}  # Map from key to node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.pop_left()
            del self.cache[lru.key]

