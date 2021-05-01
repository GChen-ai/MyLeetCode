/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        Deque node=new LinkedList();
        List<Integer> result=new ArrayList();
        if (root==null) return result;
        node.push(root);
        while (!node.isEmpty()){
            Object cur=node.pop();
            if (cur instanceof Integer){
                Integer temp=(Integer) cur;
                result.add(temp);
            }else{
                TreeNode temp=(TreeNode) cur;
                node.push(temp.val);
                if (temp.right!=null) node.push(temp.right);
                if (temp.left!=null) node.push(temp.left);
            }
        }
        return result;
    }
}