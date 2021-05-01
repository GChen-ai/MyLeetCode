class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        dic={')':'(','}':'{',']':'['}
        for i in range(len(s)):
            if s[i] in dic.keys():
                if (stack!=[]):
                    if dic[s[i]]!=stack.pop():
                        return False;
                else:
                    return False;
            else:
                stack.append(s[i])
        return stack==[];