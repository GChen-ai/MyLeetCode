class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        dp=[0]*(n+1)
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]%1000000007