class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        profit = 0

        for i, v in enumerate(prices[1:]):
            if v > prices[i]:
                profit += v - prices[i]
        
        return profit