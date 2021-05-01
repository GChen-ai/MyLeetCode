# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[root]
        result=[]
        while stack and root:
            cur=stack.pop(0)
            result.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return result