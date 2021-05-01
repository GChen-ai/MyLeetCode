class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l=0
        r=0
        char=[0]*26
        winMax=0
        for i in s:
            char[ord(i)-65]+=1
            winMax=max(winMax,char[ord(i)-65])
            if (winMax+k<r-l+1):
                char[ord(s[l])-65]-=1
                l+=1
            r+=1
        return r-l