class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if intervals==None or len(intervals)==0:
            return 0
        intervals.sort(key=lambda x:x[1])
        '''result=[intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]==intervals[i-1][0]:
                continue
            result.append(intervals[i])
        dp=[1]*len(result)
        for i in range(len(result)):
            for j in range(i+1):
                if result[j][1]<=result[i][0]:
                    dp[i]=max(dp[i],dp[j]+1)
        return len(intervals)-max(dp)'''
        res=0
        right=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<right:
                res+=1
            else:
                right=intervals[i][1]
        return res