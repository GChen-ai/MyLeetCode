# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(left,right):
            result=False
            if left==None and right==None:
                return True
            if left==None or right==None:
                return False
            if left.val!=right.val:
                return False
            result=dfs(left.left,right.right) and dfs(left.right,right.left)
            return result
        if root==None:
            return True
        return dfs(root.left,root.right)