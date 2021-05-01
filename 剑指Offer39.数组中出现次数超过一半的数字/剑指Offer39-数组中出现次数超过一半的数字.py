class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        num=0
        for i in range(len(nums)):
            if (count==0):
                num=nums[i]
                count+=1
            else:
                if (nums[i]==num):
                    count+=1
                else:
                    count-=1
        return num