class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if wall==None or len(wall)==0 or wall[0]==None or len(wall[0])==0:
            return 0
        r=len(wall)
        dic={}
        result=0
        for i in range(r):
            cur=0
            for j in range(len(wall[i])-1):
                cur+=wall[i][j]
                if cur not in dic.keys():
                    dic[cur]=1
                else:
                    dic[cur]+=1
                result=max(result,dic[cur])
        return r-result