class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        markInc=True
        markDec=True
        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                markDec=False
            if A[i]<A[i-1]:
                markInc=False
            if not markInc and not markDec:
                return False
        return True