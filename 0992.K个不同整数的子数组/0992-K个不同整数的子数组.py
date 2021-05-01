class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        def fun(A,K):
            l=0
            dic={}
            result=0
            for r in range(len(A)):
                if dic.get(A[r],0)==0:
                    K-=1
                dic[A[r]]=dic.get(A[r],0)+1
                while K<0:
                    dic[A[l]]-=1
                    if dic[A[l]]==0:
                        K+=1
                    l+=1
                result+=r-l+1
            return result
        return fun(A,K)-fun(A,K-1)
            
            