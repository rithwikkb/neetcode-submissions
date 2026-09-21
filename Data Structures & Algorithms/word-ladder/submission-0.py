class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + "*" + w[j+1:]
                nei[pattern].append(w)
        visit = set()
        visit.add(beginWord)
        q = deque()
        q.append((beginWord,1))
        while q:
            word, res = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for neiword in nei[pattern]:
                    if neiword not in visit:
                        visit.add(neiword)
                        q.append((neiword,res+1))
        
        return 0
