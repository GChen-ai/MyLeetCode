class Solution:
    def majorityElement(self, nums):
        if nums==None or len(nums)==0:
            return []
        first=0
        second=0
        count1=0
        count2=0
        n=len(nums)
        result=[]
        for i in range(n):
            if nums[i]==first:
                count1+=1
            elif nums[i]==second:
                count2+=1
            elif count1==0:
                first=nums[i]
                count1=1
            elif count2==0:
                second=nums[i]
                count2=1
            else:
                count1-=1
                count2-=1
        count1=0
        count2=0
        for i in range(n):
            if nums[i]==first:
                count1+=1
            elif nums[i]==second:
                count2+=1
        if count1>n/3:
            result.append(first)
        if count2>n/3:
            result.append(second)
        return result