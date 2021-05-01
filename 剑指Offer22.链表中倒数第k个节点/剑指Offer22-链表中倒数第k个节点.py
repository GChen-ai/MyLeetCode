# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        slow=head
        fast=head
        for i in range(k):
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        return slow