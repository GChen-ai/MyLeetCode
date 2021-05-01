# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(cur):
            pre=None
            while cur:
                temp=cur.next
                cur.next=pre
                pre=cur
                cur=temp
            return pre
        dummy=ListNode(0)
        dummy.next=head
        tail=dummy
        pre=dummy
        while tail and tail.next:
            for i in range(k):
                if tail:
                    tail=tail.next
            if tail==None:
                break
            cur=pre.next
            tailnext=tail.next
            tail.next=None
            pre.next=reverse(cur)
            cur.next=tailnext
            pre=cur
            tail=pre

        return dummy.next