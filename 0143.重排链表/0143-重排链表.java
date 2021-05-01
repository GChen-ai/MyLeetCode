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
    public void reorderList(ListNode head) {
        List<ListNode> node=new ArrayList();
        ListNode first=new ListNode();
        ListNode second=new ListNode();
        int right=-1;
        int left=0;
        while (head!=null){
            node.add(head);
            head=head.next;
            right+=1;            
        }
        while (left<=right){
            first=node.get(left);
            second.next=first;
            second=node.get(right);
            if (first==second){
                first.next=null;
                break;
            }else{
                first.next=second;
                second.next=null;
            }
            left++;
            right--;
        }
    }
}