class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sumArr=[0]
        self.nums=nums
        for i in range(len(self.nums)):
            self.sumArr.append(self.nums[i]+self.sumArr[-1])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumArr[j+1]-self.sumArr[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)