/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA==null || headB==null) return null;
        ListNode p1=headA;
        ListNode p2=headB;
        int mark1=0;
        int mark2=0;
        while (p1!=p2){
            p1=p1.next;
            p2=p2.next;
            if (p1==null) {
                if (mark1==1) return null;
                p1=headB;
                mark1=1;
            }
            if (p2==null) {
                if (mark2==1) return null;
                p2=headA;
                mark2=1;
            }
        }
        return p1;
    }
}