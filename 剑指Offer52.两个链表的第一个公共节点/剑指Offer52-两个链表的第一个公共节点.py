# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA==None or headB==None:
            return None
        p1=headA
        p2=headB
        mark1=1
        mark2=1
        while p1 and p2 and p1!=p2:
            p1=p1.next
            p2=p2.next
            if p1==None and mark1:
                p1=headB
                mark1=0
            if p2==None and mark2:
                mark2=0
                p2=headA
        return p1