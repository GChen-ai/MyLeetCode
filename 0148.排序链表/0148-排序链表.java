/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        return brokeList(head);
    }
    private ListNode brokeList(ListNode head){
        if (head==null || head.next==null) return head;
        ListNode slow=head;
        ListNode fast=head;
        
        while(fast!=null && fast.next!=null && fast.next.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        ListNode temp=slow.next;
        slow.next=null;
        ListNode left=brokeList(head);
        ListNode right=brokeList(temp);
        ListNode newhead=merge(left,right);
        return newhead;
        
    }
    private ListNode merge(ListNode p1,ListNode p2){
        ListNode dummy=new ListNode();
        ListNode head=dummy;
        while(p1!=null && p2!=null){
            if (p1.val<p2.val){
                dummy.next=p1;
                p1=p1.next;
            }else{
                dummy.next=p2;
                p2=p2.next;
            }
            dummy=dummy.next;
        }
        while (p1!=null){
            dummy.next=p1;
            p1=p1.next;
            dummy=dummy.next;
        }
        while (p2!=null){
            dummy.next=p2;
            p2=p2.next;
            dummy=dummy.next;
        }
        dummy.next=null;
        return head.next;
    }
}