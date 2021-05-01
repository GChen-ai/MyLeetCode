class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dic1={}
        dic2={}
        s=list(s.split())
        if len(pattern)!=len(s):
            return False
        for i in range(len(s)):
            if pattern[i] not in dic1.keys():
                dic1[pattern[i]]=s[i]
            else:
                if dic1[pattern[i]]!=s[i]:
                    return False
            if s[i] not in dic2.keys():
                dic2[s[i]]=pattern[i]
            else:
                if dic2[s[i]]!=pattern[i]:
                    return False
        return True