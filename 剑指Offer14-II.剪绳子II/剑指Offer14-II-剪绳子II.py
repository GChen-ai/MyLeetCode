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
            return 3**(n//3-1)*4%1000000007
        elif res==2:
            return 3**(n//3)*2%1000000007
        else:
            return 3**(n//3)%1000000007