class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r=len(matrix)-1
        c=0
        while r>=0 and c<len(matrix[0]):
            if matrix[r][c]>target:
                r-=1
            elif matrix[r][c]<target:
                c+=1
            else:
                return True
        return False