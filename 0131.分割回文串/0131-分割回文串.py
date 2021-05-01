class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def fun(s):
            l=0
            r=len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def backtrack(path,result,s,cur):
            if cur>=len(s):
                result.append(path[:])
                return
            for i in range(cur,len(s)):
                if fun(s[cur:i+1]):
                    path.append(s[cur:i+1])
                    backtrack(path,result,s,i+1)
                    path.pop()
            return
        result=[]
        path=[]
        backtrack(path,result,s,0)
        return result
                