class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if (nums==None or len(nums)==0):return 0
        count=len(nums)+1
        num_sum=0
        left=0
        right=0
        while(right<len(nums)):
            num_sum+=nums[right]
            if num_sum>=target and left<=right:
                while (num_sum>=target):
                    count=min(count,right-left+1)
                    num_sum-=nums[left]
                    left+=1
            right+=1
        if (count==len(nums)+1):count=0
        return count