class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices==None or len(prices)<=1:
            return 0
        firstBuy=float('inf')
        firstSale=0
        secondBuy=float('inf')
        secondSale=0
        for i in range(len(prices)):
            firstBuy=min(firstBuy,prices[i])
            firstSale=max(firstSale,prices[i]-firstBuy)
            secondBuy=min(secondBuy,prices[i]-firstSale)
            secondSale=max(secondSale,prices[i]-secondBuy)
        return secondSale