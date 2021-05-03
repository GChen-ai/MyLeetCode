/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        Map<Node,Node> dic=new HashMap();
        return dfs(node,dic);
    }
    private Node dfs(Node node,Map<Node,Node> dic){
        if (node==null) return null;
        if (dic.containsKey(node)) return dic.get(node);
        Node clone=new Node(node.val,new ArrayList<Node>());
        dic.put(node,clone);
        for (Node n:node.neighbors){
            clone.neighbors.add(dfs(n,dic));
        }
        return clone;
    }
}