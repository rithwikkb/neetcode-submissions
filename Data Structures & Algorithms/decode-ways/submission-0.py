class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i] is number of ways to decode the first i characters of s
        dp = [0] * (n+1)
        # 0 means its a empty string so the only way to decode is to do nothing so its 1
        dp[0] = 1
        # if it starts with 0 that means we cant decode at all so its 0, if not then we have 1 way to decode
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1
        for i in range(2, n+1):
            # get the last digit and the last 2 digits
            onedigit = int(s[i-1])
            twodigit = int(s[i-2:i])
            # if the last digit is valid, we can include it
            if onedigit >= 1:
                dp[i] += dp[i-1]
            # if the last two digits are valid, we can  also include it
            if 10 <= twodigit <= 26:
                dp[i] += dp[i-2]
        return dp[n]

        