class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l=0
        n=len(matrix)
        while l<=n//2:
            r=n-l-1
            for i in range(l,r):
                temp=matrix[i][r]
                matrix[i][r]=matrix[l][i]
                matrix[l][i]=matrix[n-i-1][l]
                matrix[n-i-1][l]=matrix[r][n-i-1]
                matrix[r][n-i-1]=temp
            l+=1