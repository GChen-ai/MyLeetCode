class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            x=1/x
            n=-n
        result=1
        while n>0:
            if n%2==1:
                result*=x
                n-=1
            x*=x
            n=n//2
        return result