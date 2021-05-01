class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def dfs(x,y,mem,k):
            if x<0 or x>len(mem)-1 or y<0 or y>len(mem[0])-1 or mem[x][y]==1:
                return
            num_sum=0
            temp=x
            while temp>0:
                num_sum+=temp%10
                temp=temp//10
            temp=y
            while temp>0:
                num_sum+=temp%10
                temp=temp//10
            if num_sum>k:
                return
            mem[x][y]=1
            dfs(x+1,y,mem,k)
            #dfs(x-1,y,mem,k)
            dfs(x,y+1,mem,k)
            #dfs(x,y-1,mem,k)
            return
        mem=[[0]*n for i in range(m)]
        dfs(0,0,mem,k)
        count=0
        for i in range(m):
            for j in range(n):
                if mem[i][j]!=0:
                    count+=1
        return count