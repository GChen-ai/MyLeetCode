class CQueue(object):
    
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack1.append(value)



    def deleteHead(self):
        """
        :rtype: int
        """
        if len(self.stack1)==0 and len(self.stack2)==0:
            return -1
        while(self.stack2):
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()