# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        count=0
        p=head
        while p:
            p=p.next
            count+=1
        p=head
        for i in range(count//2):
            p=p.next
        pre=None
        while p:
            temp=p.next
            p.next=pre
            pre=p
            p=temp
        while pre:
            if head.val!=pre.val:
                return False
            head=head.next
            pre=pre.next
        return True