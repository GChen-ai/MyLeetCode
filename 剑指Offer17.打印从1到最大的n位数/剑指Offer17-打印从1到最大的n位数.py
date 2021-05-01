class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result=[]
        for i in range(1,10**n):
            result.append(i)
        return result