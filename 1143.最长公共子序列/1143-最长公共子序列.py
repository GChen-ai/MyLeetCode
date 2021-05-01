class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if text1==None or len(text1)==None or text2==None or len(text2)==0:
            return 0
        dp=[[0]*(len(text2)+1) for i in range(len(text1)+1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
        return dp[-1][-1]