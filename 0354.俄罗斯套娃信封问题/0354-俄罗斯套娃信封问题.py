class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        N=len(envelopes)
        dp=[1]*N
        result=1
        for i in range(1,N):
            for j in range(i):
                if envelopes[j][1]<envelopes[i][1]:
                    dp[i]=max(dp[i],dp[j]+1)
            result=max(result,dp[i])
        return result