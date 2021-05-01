class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack=[]
        index=0
        if pushed==None or popped==None:
            return True
        for i in pushed:
            stack.append(i)
            while stack and stack[-1]==popped[index]:
                stack.pop()
                index+=1
        return not stack