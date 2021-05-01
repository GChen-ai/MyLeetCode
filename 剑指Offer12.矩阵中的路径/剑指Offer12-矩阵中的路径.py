class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        mem=[[0 for i in range(len(board[0]))]for i in range(len(board))]
        def dfs(board,word,mem,x,y):
            result=False
            if word==None or len(word)==0:
                return True
            if (x<0 or x>len(board)-1 or y<0 or y>len(board[0])-1 or mem[x][y]==1 or board[x][y]!=word[0]):
                return result
            mem[x][y]=1
            result=dfs(board,word[1:],mem,x+1,y) or dfs(board,word[1:],mem,x,y+1) or dfs(board,word[1:],mem,x-1,y) or dfs(board,word[1:],mem,x,y-1)
            mem[x][y]=0
            return result
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board,word,mem,i,j):
                    return True
        return False
            