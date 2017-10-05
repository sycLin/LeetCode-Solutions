class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # find the best selling point for each day
        bestSellingPoint = [float("-INF")]
        for i in range(len(prices)-2, -1, -1):
            bsp = max(prices[i+1], bestSellingPoint[0])
            bestSellingPoint.insert(0, bsp)
        # find the best profit for each day
        maxProfit = float("-INF")
        for i in range(len(prices)):
            profit = bestSellingPoint[i] - prices[i]
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit if maxProfit > 0 else 0
            
