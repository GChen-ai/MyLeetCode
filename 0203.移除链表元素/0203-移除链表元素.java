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
    public ListNode removeElements(ListNode head, int val) {
        ListNode pre=new ListNode();
        ListNode cur=head;
        pre.next=head;
        ListNode newhead=pre;
        while(cur!=null){
            if (cur.val==val){
                pre.next=cur.next;
            }else{
                pre.next=cur;
                pre=pre.next;
            }
            cur=cur.next;
        }
        return newhead.next;
    }
}