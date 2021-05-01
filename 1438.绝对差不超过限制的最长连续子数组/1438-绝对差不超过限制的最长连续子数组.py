class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_n=[]
        min_n=[]
        result=0
        l=0
        for i in range(len(nums)):
            while max_n and nums[i]>max_n[-1]:
                max_n.pop()
            max_n.append(nums[i])
            while min_n and nums[i]<min_n[-1]:
                min_n.pop()
            min_n.append(nums[i])
            while max_n and min_n and max_n[0]-min_n[0]>limit:
                if nums[l]==max_n[0]:
                    max_n.pop(0)
                if nums[l]==min_n[0]:
                    min_n.pop(0)
                l+=1
            result=max(result,i-l+1)
        return result