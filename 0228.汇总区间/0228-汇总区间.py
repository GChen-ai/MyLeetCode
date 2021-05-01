class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result=[]
        if nums==None or len(nums)==0:
            return result
        l=nums[0]
        if len(nums)==1:
            return [str(l)]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>1:
                if nums[i-1]==l:
                    result.append(str(l))
                else:
                    result.append(str(l)+'->'+str(nums[i-1]))
                if i==len(nums)-1:
                    result.append(str(nums[i]))
                l=nums[i]
            elif i==len(nums)-1:
                if nums[i]==l:
                    result.append(str(l))
                else:
                    result.append(str(l)+'->'+str(nums[i]))
        return result