# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def preorder(root,depth):
            if root==None:
                return depth
            return max(preorder(root.left,depth+1),preorder(root.right,depth+1))
        return preorder(root,0)