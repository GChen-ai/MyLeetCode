class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix==None or len(matrix)==0 or matrix[0]==None or len(matrix[0])==0:
            return []
        left=0
        right=len(matrix[0])-1
        top=0
        down=len(matrix)-1
        result=[]
        while left<=right and top<=down:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            for i in range(top+1,down+1):
                result.append(matrix[i][right])
            if left<right and top<down:
                for i in range(right-1,left,-1):
                    result.append(matrix[down][i])
                for i in range(down,top,-1):
                    result.append(matrix[i][left])
            left+=1
            right-=1
            top+=1
            down-=1
        return result
                