class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result=0
        while n>0:
            res=n%2
            if res==1:
                result+=1
            n=n//2
        return result