class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:return False
        while n>1:
            pre=n
            if n%2==0:n/=2
            if n%3==0:n/=3
            if n%5==0:n/=5
            if pre==n:return False
        return True