class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        l=0
        r=n-1
        count=0
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                k=mid
                while k<n and nums[k]==target:
                    count+=1
                    k+=1
                k=mid-1
                while k>=0 and nums[k]==target:
                    count+=1
                    k-=1
                break
        return count