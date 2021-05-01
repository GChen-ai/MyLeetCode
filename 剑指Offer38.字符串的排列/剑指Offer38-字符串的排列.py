class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        N=len(s1)
        count=N
        dic={}
        for s in s1:
            dic[s]=dic.get(s,0)+1
        l=0
        for r in range(len(s2)):
            if dic.get(s2[r],-999)==-999:
                count=N
                while (l<r):
                    dic[s2[l]]=dic.get(s2[l],0)+1
                    l+=1
                l=r+1
                    
            else:
                dic[s2[r]]-=1
                count-=1
                while dic[s2[r]]<0:
                    dic[s2[l]]+=1
                    l+=1
                    count+=1
                if count==0:
                    return True
        return False
            

            
            
