class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[1]*(n+1)
        if n==0:
            return dp[0]
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]%1000000007