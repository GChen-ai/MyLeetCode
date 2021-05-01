class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def backtrack(k,n,cur,result,path):
            if (k==0 and n==0):
                result.append(path[:])
                return
            if n<0 or k<0:
                return
            for i in range(cur,10):
                path.append(i)
                backtrack(k-1,n-i,i+1,result,path)
                path.pop()
            return
        result=[]
        backtrack(k,n,1,result,[])
        return result