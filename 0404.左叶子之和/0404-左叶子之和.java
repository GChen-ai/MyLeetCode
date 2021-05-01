/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        if (root==null || (root.left==null && root.right==null)) return 0;
        return sum(root,0);
    }
    private int sum(TreeNode root,int flag){
        if (root==null) return 0;
        if (root.left==null && root.right==null && flag==0) return root.val;
        return sum(root.left,0)+sum(root.right,1);
    }
}