class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        l=0
        maxc=0
        win=0
        all_cus=0
        result=0
        for r in range(len(customers)):
            if (grumpy[r]==0):
                win+=customers[r]
                result+=customers[r]
            all_cus+=customers[r]
            maxc=max(all_cus-win,maxc)
            if r>=X-1:
                if grumpy[l]==0:
                    win-=customers[l]
                all_cus-=customers[l]
                l+=1
        result+=maxc
        return result