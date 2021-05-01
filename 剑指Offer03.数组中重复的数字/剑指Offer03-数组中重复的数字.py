class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==None or len(nums)<=1:
            return 0
        for i in range(len(nums)):
            while nums[i]!=i:
                print(nums[i])
                if nums[i]==nums[nums[i]]:
                    return nums[i]
                temp=nums[i]
                nums[i]=nums[nums[i]]
                nums[temp]=temp
        return -1