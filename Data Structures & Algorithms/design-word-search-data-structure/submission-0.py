class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.word = True
        

    def search(self, word: str) -> bool:
        stack = [(0, self.root)]

        while stack:
            j, curr = stack.pop()
            if j == len(word):
                if curr.word:
                    return True
                continue

            c = word[j]

            if c == ".":
                # Try every possible next character
                for child in curr.children.values():
                    stack.append((j + 1, child))

            else:
                # Follow the exact character path
                if c in curr.children:
                    stack.append((j + 1, curr.children[c]))

        return False
