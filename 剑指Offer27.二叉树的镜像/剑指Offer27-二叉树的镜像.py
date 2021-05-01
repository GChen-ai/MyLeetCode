# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return None
        def preOrder(root):
            if root==None:
                return
            root.left,root.right=root.right,root.left
            preOrder(root.left)
            preOrder(root.right)
            return
        preOrder(root)
        return root