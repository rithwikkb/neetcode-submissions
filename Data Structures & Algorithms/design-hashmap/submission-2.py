class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]
        
    def hash(self, key: int) -> int:
        return key % len(self.map) # we got buckets from 0 to 1000 where there's linked lists for each. %1000 is to group then basically, so 5, 1005, 2005, etc are in a bucket.
    def put(self, key: int, value: int) -> None:
        curr = self.map[self.hash(key)] # this is to get the bucket we're searching
        while curr.next: # now we keep on traversing the linked list till we find the key, if we find the same key we replace the value with the one we're adding
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next # this is to just move to the next node
        curr.next = ListNode(key,value) # if it doesn't already exist, we add it to the linked list
        

    def get(self, key: int) -> int:
        curr = self.map[self.hash(key)] # get the curr bucket by hashing
        while curr.next: # while the next value exists
            if curr.next.key == key: # we check if the key matches
                return curr.next.val # if so we return the val
            curr = curr.next # then we move to the next node
        return -1
        
    def remove(self, key: int) -> None:
        curr = self.map[self.hash(key)] # get the bucket by hashing
        while curr.next: # while the next node exists
            if curr.next.key == key: # check if the key matches
                curr.next = curr.next.next # if it does we just said next to the value after the curr node, essentially removing it
                return # once we remove we return
            curr = curr.next
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)