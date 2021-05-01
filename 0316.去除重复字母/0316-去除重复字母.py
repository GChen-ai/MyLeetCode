class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic={}
        stack=[]
        for i in s:
            if i not in dic.keys():
                dic[i]=1
            else:
                dic[i]+=1
        for i in s:
            if i not in stack:
                while stack and dic[stack[-1]]>=1 and stack[-1]>i:
                    stack.pop()
                stack.append(i)
            dic[i]-=1
        return ''.join(stack)