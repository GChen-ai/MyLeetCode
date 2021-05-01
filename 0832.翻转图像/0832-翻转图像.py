class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if A==[] or A[0]==[]:return A
        l=0
        r=len(A[0])-1
        for i in range(len(A)):
            while l<r:
                A[i][r],A[i][l]=A[i][l],A[i][r]
                A[i][l]=1-A[i][l]
                A[i][r]=1-A[i][r]
                l+=1
                r-=1
            if l==r:
                A[i][l]=1-A[i][l]
            l=0
            r=len(A[0])-1
        return A
                