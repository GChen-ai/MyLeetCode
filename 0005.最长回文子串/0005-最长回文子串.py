class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s==None or len(s)==0:
            return ''
        n=len(s)
        dp=[[0]*n for i in range(n)]
        result=s[0]
        for i in range(n-1,-1,-1):
            dp[i][i]=1
            for j in range(i+1,n):
                if s[i]==s[j]:
                    if j-i<3:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i+1][j-1]
                if dp[i][j] and j-i+1>len(result):
                    result=s[i:j+1]
        return result