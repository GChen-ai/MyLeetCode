/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head==null) return null;
        ListNode slow=head;
        ListNode fast=head.next;
        while (slow!=null && fast!=null && fast.next!=null){
            if (slow==fast) break;
            slow=slow.next;
            fast=fast.next.next;
        }
        if (slow!=fast) return null;
        ListNode p=new ListNode(0);
        p.next=head;
        while(p!=slow){
            p=p.next;
            slow=slow.next;
        }
        return p;
    }
}