class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def backtrack(n,r,path,result):
            if r==n:
                temp=[]
                for i in range(n):
                    temp.append(''.join(path[i]))
                result.append(temp)
                return
            for i in range(n):
                if (valid(n,r,i,path)):
                    path[r][i]='Q'
                    backtrack(n,r+1,path,result)
                    path[r][i]='.'
            return
        def valid(n,r,c,path):
            for i in range(r):
                if path[i][c]=='Q':
                    return False
            for i in range(c):
                if path[r][i]=='Q':
                    return False
            i=r-1
            j=c-1
            while i>=0 and j>=0:
                if path[i][j]=='Q':
                    return False
                i-=1
                j-=1
            i=r-1
            j=c+1
            while i>=0 and j<n:
                if path[i][j]=='Q':
                    return False
                i-=1
                j+=1
            return True
        result=[]
        if n<=0:
            return result
        path=[['.']*n for j in range(n)]
        backtrack(n,0,path,result)
        return result