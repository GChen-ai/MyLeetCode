class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums==None or len(nums)==0:
            return False
        l=0
        r=len(nums)-1
        while r>l and nums[0]==nums[r]:
            r-=1
        right=nums[r]
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            if nums[mid]>=nums[0]:
                if nums[0]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=right:
                    l=mid+1
                else:
                    r=mid-1
        return False