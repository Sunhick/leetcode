class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # DP
        # profit(i) = max{S(i) - min(S(i-1,i-2...1), Profit(i-1))}
        if not prices:
            return 0
            
        profit = 0
        cp = 999999
        for price in prices:
            if cp > price:
                cp = price
            if price - cp > profit:
                profit = price - cp
        return profit