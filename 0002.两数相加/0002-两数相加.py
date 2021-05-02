# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result=ListNode(0)
        head=result
        mark=0
        while l1 and l2:
            nums=l1.val+l2.val+mark
            if nums>=10:
                nums-=10
                mark=1
            else:
                mark=0
            result.next=ListNode(nums)
            result=result.next
            l1=l1.next
            l2=l2.next
        while l1:
            nums=l1.val+mark
            if nums>=10:
                nums-=10
                mark=1
            else:
                mark=0
            l1=l1.next
            result.next=ListNode(nums)
            result=result.next
        while l2:
            nums=l2.val+mark
            if nums>=10:
                nums-=10
                mark=1
            else:
                mark=0
            l2=l2.next
            result.next=ListNode(nums)
            result=result.next
        if mark==1:
            result.next=ListNode(1)
        return head.next