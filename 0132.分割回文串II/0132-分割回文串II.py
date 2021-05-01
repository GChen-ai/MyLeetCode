class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        def fun(s):
            return s==s[::-1]
        n=len(s)
        dp=[n]*n
        for i in range(n):
            if fun(s[:i+1]):
                dp[i]=0
                continue
            for j in range(i):
                if fun(s[j+1:i+1]):
                    dp[i]=min(dp[i],dp[j]+1)
        return dp[-1]