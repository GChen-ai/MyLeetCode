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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result=new ArrayList();
        if (root==null) return result;
        rightOrder(root,0,result,0);
        return result;
    }
    private int rightOrder(TreeNode root,int depth,List result,int max){
        if (root==null) return max;
        depth++;
        if (depth>max){
            max=depth;
            result.add(root.val);
        }
        max=Math.max(rightOrder(root.right,depth,result,max),max);
        max=Math.max(rightOrder(root.left,depth,result,max),max);
        return max;
    }
}