class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if (nums==None or len(nums)==0 or len(nums)<k): return 0
        med=sum(nums[:k])
        result=med
        for i in range(k,len(nums)):
            med+=nums[i]-nums[i-k]
            result=max(result,med)
        return result*1.0/k