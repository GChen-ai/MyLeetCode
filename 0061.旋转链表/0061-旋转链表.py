# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count=0
        temp=head
        if head==None:
            return head
        while temp:
            temp=temp.next
            count+=1
        k=k%count
        slow=head
        fast=head
        for i in range(k):
            fast=fast.next
        while fast!=None and fast.next!=None:
            fast=fast.next
            slow=slow.next
        fast.next=head
        head=slow.next
        slow.next=None
        return head