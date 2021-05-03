class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        if nums==None or len(nums)==0:
            return result
        N=len(nums)
        nums.sort()
        for i in range(N):
            target1=target-nums[i]
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,N):
                target2=target1-nums[j]
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l=j+1
                r=N-1
                while l<r:
                    if nums[l]+nums[r]==target2:
                        result.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<N and nums[l]==nums[l-1]:
                            l+=1
                        while r>=0 and nums[r]==nums[r+1]:
                            r-=1
                    elif nums[l]+nums[r]<target2:
                        l+=1
                    else:
                        r-=1
        return result