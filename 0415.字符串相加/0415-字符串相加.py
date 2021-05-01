class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1=len(num1)
        l2=len(num2)
        if l1==None and l2==None:
            return ''
        result=''
        mark=0
        for i in range(max(l1,l2)):
            n=0
            if i<l1:
                n+=int(num1[l1-i-1])
            if i<l2:
                n+=int(num2[l2-i-1])
            n+=mark
            if n>=10:
                n-=10
                mark=1
            else:
                mark=0
            result+=str(n)
        if mark==1:
            result+='1'
        return result[::-1]

