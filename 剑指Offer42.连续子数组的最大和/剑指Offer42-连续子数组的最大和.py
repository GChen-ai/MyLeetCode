class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==None or len(nums)==0:
            return 0
        dp=[0]*len(nums)
        dp[0]=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            result=max(result,dp[i])
        return result