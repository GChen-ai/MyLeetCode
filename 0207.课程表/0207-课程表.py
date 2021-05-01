class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if prerequisites==None or len(prerequisites)==0: return True
        maps=[[] for j in range(numCourses)]
        for pre in prerequisites:
            maps[pre[0]].append(pre[1])
        V=[0 for i in range(numCourses)]
        for i in range(len(maps)):
            result=self.dfs(maps,i,V)
            if result==False:
                return False
        return True
        
    def dfs(self,maps,u,V):
        if V[u]==1: return False
        if V[u]==-1: return True
        V[u]=1
        for i in maps[u]:
            if not self.dfs(maps,i,V):return False
        V[u]=-1
        return True
                    
