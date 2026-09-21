class Solution:

    def partition(self, s: str) -> List[List[str]]:
        """
        aab
        dfs(0)
        0,1,2
        c = s[0:1]
        c = a
        part = [a]
        dfs(1)
        1,2
        c = a
        part = [a,a]
        dfs(2)
        2
        s[2:3]
        c = b
        part = [a,a,b]
        dfs(3)
        3 == 3
        res = [[a,a,b]]
        return to the dfs(2) call
        after dfs(3) line pop
        part = [a,a]
        loop is done so go back to dfs(1) call
        after dfs(2) pop again
        part = [a]
        here theres still one more iteration
        j = 2
        c = [1:3]
        c = ab
        not palindrome, loop over, go back to dfs(0)
        after dfs(1) line, pop
        part = []
        now continue loop,
        j = 1
        c = [0:2]
        c = aa
        is a palindrone
        part = [aa]
        dfs(2)
        j = 2
        c = s[2:3]
        c = b
        part = [aa,b]
        dfs(3)
        3 == 3
        res = [[a,a,b],[aa,b]]
        return back in dfs(2)
        part.pop()
        part = [aa]
        j = 2 so loop done
        back to dfs(0)
        part.pop()
        part = []
        j = 2
        i = 0
        c = aab
        not palindrome
        since we're at dfs(0), we're done
        """

        """
        overview(way to think): start from index i, try all substrings starting from index i and check if they're a palindrome, if not, skip, if so, add it to out path and recurse the remaining parts of the string(excluding the palindrome part)
        """
        res, part = [], []

        def dfs(i):
            if i == len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                c = s[i:j+1]
                if c == c[::-1]:
                    part.append(c)
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res
