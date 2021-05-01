class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result=0
        if prices==None or len(prices)<=1:
            return 0
        temp=0
        for i in range(1,len(prices)):
            result+=max(0,prices[i]-prices[i-1])
        return result