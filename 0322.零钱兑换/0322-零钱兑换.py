class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if coins==[] or len(coins)==0:
            return -1
        if amount==0:
            return 0
        dp=[[0]*(amount+1) for i in range(len(coins)+1)]
        for i in range(amount+1):
            dp[0][i]=float('inf')
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-coins[i-1]]+1)
                else:
                    dp[i][j]=dp[i-1][j]
        if dp[-1][-1]==0 or dp[-1][-1]==float('inf'):
            return -1
        else:
            return dp[-1][-1]