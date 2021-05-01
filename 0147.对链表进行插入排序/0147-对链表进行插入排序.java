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
    public ListNode insertionSortList(ListNode head) {
        if (head==null) return head;
        ListNode dummy=new ListNode();
        dummy.next=head;
        ListNode pre=head;
        ListNode cur=head.next;
        while(cur!=null){
            if (cur.val<pre.val){
                pre.next=cur.next;
                ListNode tempPre=dummy;
                while (tempPre.next!=null){
                    if (tempPre.next.val<cur.val){
                        tempPre=tempPre.next;
                    }else{
                        cur.next=tempPre.next;
                        tempPre.next=cur;
                        break;
                    }
                }
                cur=pre.next;
            }else{
                pre=pre.next;
                if (pre!=null) cur=pre.next;
            }
        }
        return dummy.next;
    }
}