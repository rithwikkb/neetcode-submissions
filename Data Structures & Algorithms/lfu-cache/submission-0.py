class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def length(self):
        return self.size

    def pushright(self, node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node      # <-- Missing line

        self.size += 1

    def pop(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        node.prev = None
        node.next = None
        self.size -= 1

    def popleft(self):
        if self.length() == 0:
            return None

        node = self.left.next
        self.pop(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfucnt = 0
        self.nodemap = {}                  # key -> node
        self.listmap = defaultdict(LinkedList)  # freq -> DLL

    def counter(self, node):
        cnt = node.freq
        self.listmap[cnt].pop(node)

        if cnt == self.lfucnt and self.listmap[cnt].length() == 0:
            self.lfucnt += 1

        node.freq += 1
        self.listmap[node.freq].pushright(node)

    def get(self, key: int) -> int:
        if key not in self.nodemap:
            return -1

        node = self.nodemap[key]
        self.counter(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.nodemap:
            node = self.nodemap[key]
            node.val = value
            self.counter(node)
            return

        if len(self.nodemap) == self.cap:
            node = self.listmap[self.lfucnt].popleft()
            del self.nodemap[node.key]

        node = Node(key, value)
        self.nodemap[key] = node
        self.lfucnt = 1
        self.listmap[self.lfucnt].pushright(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)