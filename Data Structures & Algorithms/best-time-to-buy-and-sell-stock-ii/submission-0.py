class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # basically if we graph this up, we notice that if we add up all the positive slopes, that equals the max profit, so we basically just add up all the positive slopes in the code.
        res = 0
        for i in range(1,len(prices)): # start at 1 coz second day
            if prices[i] > prices[i-1]: # 5>1 so add 5-1 = 4, 6-3 = 3, 
                res += (prices[i] - prices[i-1])
        return res
        