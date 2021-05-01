class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=[0]*(len(nums))
        for i in range(len(nums)):
            if (n[nums[i]]!=0):return nums[i]
            n[nums[i]]+=1
        return -1