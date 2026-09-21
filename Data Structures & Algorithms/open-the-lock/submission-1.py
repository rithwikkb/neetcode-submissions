class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        q = deque()
        q.append(["0000", 0])
        visited = {"0000"}
        while q:
            for i in range(len(q)):
                node, turns = q.popleft()
                if node == target:
                    return turns
                # we have 4 indexes(4 wheels)
                for i in range(4):
                    # and for each wheel, we can either increment or decrement by 1
                    for change in [-1,1]:
                        # what we do is make the node a list
                        chars = list(node)
                        # and then add the number to the integer at that index. if it becomes -1 or 10 we do mod 10 to make it 9 and 0
                        chars[i] = str((int(chars[i]) + change) % 10)
                        # now we make it a string and then check if it is dead or if it is visited. if so, we skip
                        neighbor = "".join(chars)
                        if neighbor in dead or neighbor in visited:
                            continue
                        visited.add(neighbor)
                        q.append((neighbor, turns + 1)) 
            # after each iteration we can increment the number of turns   
        return -1    