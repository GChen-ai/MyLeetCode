class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        p1=0
        p2=0
        p3=0
        dp=[1]*n
        for i in range(1,n):
            dp[i]=min(dp[p1]*2,min(dp[p2]*3,dp[p3]*5))
            if dp[i]==dp[p1]*2:
                p1+=1
            if dp[i]==dp[p2]*3:
                p2+=1
            if dp[i]==dp[p3]*5:
                p3+=1
        return dp[-1]