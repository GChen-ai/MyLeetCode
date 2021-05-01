class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        l=0
        for r in range(len(s)):
            while r>l and s[r] in s[l:r]:
                l+=1
            result=max(result,r-l+1)
        return result