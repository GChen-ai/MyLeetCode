/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head==null) return null;
        Node newhead=new Node(0);
        HashMap<Node,Node> map=new HashMap();
        Node temp=newhead;
        Node headt=head;
        while(headt!=null){
            Node cur=new Node(headt.val);
            temp.next=cur;
            temp=temp.next;
            map.put(headt,cur);
            headt=headt.next;
        }
        headt=head;
        temp=newhead.next;
        while(headt!=null){
            if (headt.random!=null){
                temp.random=map.get(headt.random);
            }
            temp=temp.next;
            headt=headt.next;
        }
        return newhead.next;

    }
}