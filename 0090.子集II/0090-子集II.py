class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(path,result,cur,nums):
            result.append(path[:])
            for i in range(cur,len(nums)):
                if i>cur and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(path,result,i+1,nums)
                path.pop()
        result=[]
        if nums==None or len(nums)==0:
            return result
        nums.sort()
        backtrack([],result,0,nums)
        return result