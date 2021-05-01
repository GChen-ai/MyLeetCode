class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix=matrix
        self.sumMatrix=None
        if matrix==None or len(matrix)==0 or matrix[0]==None or len(matrix[0])==0:
            return
        self.sumMatrix=[[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        for i in range(1,len(self.sumMatrix)):
            for j in range(1,len(self.sumMatrix[0])):
                self.sumMatrix[i][j]=self.sumMatrix[i-1][j]+self.sumMatrix[i][j-1]+self.matrix[i-1][j-1]-self.sumMatrix[i-1][j-1]
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.sumMatrix==None:
            return
        return self.sumMatrix[row2+1][col2+1]-self.sumMatrix[row1][col2+1]-self.sumMatrix[row2+1][col1]+self.sumMatrix[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)