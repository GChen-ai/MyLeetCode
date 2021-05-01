class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums==None or len(nums)==0:
            return ''
        nums=[str(x) for x in nums]
        compare=lambda x,y:1 if x+y<y+x else -1
        nums.sort(cmp=compare)
        result=''.join(nums)
        if result[0]=='0':
            return '0'
        return result
