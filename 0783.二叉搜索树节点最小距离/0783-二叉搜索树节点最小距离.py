# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack=[root]
        pre=None
        result=float('inf')
        while stack:
            cur=stack.pop()
            if type(cur)==int:
                if pre!=None:
                    result=min(abs(cur-pre),result)
                pre=cur
            else:
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur.val)
                if cur.left:
                    stack.append(cur.left)
        return result
        