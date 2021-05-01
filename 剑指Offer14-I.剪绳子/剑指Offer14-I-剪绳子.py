class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 1
        if n==3:return 2
        res=n%3
        if res==1:
            return 3**(n//3-1)*4
        elif res==2:
            return 3**(n//3)*2
        else:
            return 3**(n//3)