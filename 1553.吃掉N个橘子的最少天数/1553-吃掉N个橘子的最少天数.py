class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic={}
        def dfs(n,dic):
            if n==1:
                return 1
            if n==2:
                return 2
            if n==3:
                return 2
            if n in dic.keys():
                return dic[n]
            result=min(dfs(n//2,dic)+n%2,dfs(n//3,dic)+n%3)+1
            dic[n]=result
            return result
        return dfs(n,dic)