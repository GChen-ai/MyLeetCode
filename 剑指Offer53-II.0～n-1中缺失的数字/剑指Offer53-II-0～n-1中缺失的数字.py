class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)+1
        if n==1:
            return 0
        return (n-1)*n/2-sum(nums)