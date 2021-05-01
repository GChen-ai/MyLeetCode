class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        count=0
        queue=[]
        for i in range(0,len(A)):
            if (queue!=[] and i>=queue[0]+K):
                queue.pop(0)
            if (len(queue)%2==A[i]):
                if i+K>len(A): return -1
                queue.append(i)
                count+=1
        return count