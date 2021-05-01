class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==None or len(matrix)==0:
            return False
        i=len(matrix)-1
        j=0
        while (i>=0 and j<len(matrix[0])):
            if matrix[i][j]>target:
                i-=1
            elif matrix[i][j]<target:
                j+=1
            else:
                return True
        return False