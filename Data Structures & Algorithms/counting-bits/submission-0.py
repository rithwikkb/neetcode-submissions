class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for num in range(n+1):
            one = 0
            for i in range(32):
                if num & (1<<i):
                    one += 1
            result.append(one)
        return result

        