class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (nums==None or len(nums)==0): return False
        count=0
        for i in range(1,len(nums)):
            if (nums[i]<nums[i-1]):
                count+=1
                if (i==1 or nums[i]>=nums[i-2]):
                    nums[i-1]=nums[i]
                else:
                    nums[i]=nums[i-1]
        return count<=1