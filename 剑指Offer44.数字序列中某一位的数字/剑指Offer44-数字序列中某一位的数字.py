class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<10:
            return n
        n-=1
        count=1
        while n>10**(count-1)*9*count:
            n=n-10**(count-1)*9*count
            count+=1
        res=n%(count)
        result=str(n//(count)+10**(count-1))
        return int(result[res])