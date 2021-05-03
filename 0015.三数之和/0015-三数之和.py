class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums==None or len(nums)==0:
            return []
        N=len(nums)
        nums.sort()
        result=[]
        for i in range(N):
            target=-nums[i]
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=N-1
            while l<r:
                if nums[l]+nums[r]==target:
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<N and nums[l]==nums[l-1]:
                        l+=1
                    while r>=0 and nums[r]==nums[r+1]:
                        r-=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    l+=1
        return result
                