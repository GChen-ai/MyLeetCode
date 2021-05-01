class Solution:
    def findKthLargest(self, nums, k):
        def partition(l,r):
            pivot=l
            while l<r:
                while l<r and nums[r]>=nums[pivot]:r-=1
                while l<r and nums[l]<=nums[pivot]:l+=1
                nums[l],nums[r]=nums[r],nums[l]
            nums[l],nums[pivot]=nums[pivot],nums[l]
            return l
        k=len(nums)-k #第k大=第len(nums)-k小
        if k>=len(nums):return nums[-1]
        
        l,r=0,len(nums)-1
        while True:
            idx=partition(l,r)
            if idx==k:
                return nums[idx]
            elif idx<k:
                l=idx+1
            else:
                r=idx-1

