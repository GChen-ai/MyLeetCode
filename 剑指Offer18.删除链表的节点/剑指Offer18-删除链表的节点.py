# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre=ListNode(0)
        newhead=pre
        pre.next=head
        cur=head
        while cur and cur.val!=val:
            cur=cur.next
            pre=pre.next
        pre.next=cur.next
        return newhead.next