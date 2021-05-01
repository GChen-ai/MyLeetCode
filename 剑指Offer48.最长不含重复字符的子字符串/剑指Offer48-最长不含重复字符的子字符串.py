class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s==None or len(s)<=1:
            return len(s)
        c=set()
        l=0
        result=0
        for r in range(len(s)):
            if s[r] in c:
                while s[r] in c:
                    c.remove(s[l])
                    l+=1
            c.add(s[r])
                
            result=max(result,r-l+1)
        return result