class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in range(len(nums)):
            if nums[i] not in dic.keys():
                dic[nums[i]]=[i]
            else:
                dic[nums[i]].append(i)
        result=50000
        max_len=0
        for k in dic.keys():
            if max_len<len(dic[k]):
                max_len=len(dic[k])
                result=dic[k][-1]-dic[k][0]+1
            elif max_len==len(dic[k]):
                result=min(dic[k][-1]-dic[k][0]+1,result)
        return result