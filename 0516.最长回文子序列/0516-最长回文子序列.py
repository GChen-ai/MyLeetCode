class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s==None or len(s)==0:
            return 0
        n=len(s)
        dp=[[0]*n for i in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i]=1
            for j in range(i+1,n):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1]