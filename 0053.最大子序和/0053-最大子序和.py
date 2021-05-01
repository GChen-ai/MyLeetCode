class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            pre=max(nums[i],pre+nums[i])
            result=max(result,pre)
        return result