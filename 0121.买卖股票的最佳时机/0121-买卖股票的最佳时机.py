class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices==None or len(prices)==0:
            return 0
        result=0
        temp=0
        for i in range(1,len(prices)):
            temp+=prices[i]-prices[i-1]
            temp=max(temp,0)
            result=max(temp,result)
        return result