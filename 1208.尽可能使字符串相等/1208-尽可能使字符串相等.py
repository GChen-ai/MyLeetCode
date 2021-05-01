class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        l=0
        cost=0
        result=0
        for r in range(len(s)):
            cost+=abs(ord(s[r])-ord(t[r]))
            while cost>maxCost:
                cost-=abs(ord(s[l])-ord(t[l]))
                l+=1
            result=max(result,r-l+1)
        return result