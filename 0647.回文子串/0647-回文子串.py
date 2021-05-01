class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[[0]*n for i in range(n)]
        count=0
        for i in range(n-1,-1,-1):
            dp[i][i]=1
            count+=1
            for j in range(i+1,n):
                if s[i]==s[j]:
                    if j-i<3:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i+1][j-1]
                if dp[i][j]:
                    count+=1
        return count