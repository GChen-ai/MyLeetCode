# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        def preorder(A,B):
            result=False
            if A==None or B==None:
                return result
            if A.val==B.val:
                result=isSub(A,B)
                if result:
                    return result
            return preorder(A.left,B) or preorder(A.right,B)
        def isSub(A,B):
            result=False
            if B==None:
                return True
            if A==None or A.val!=B.val:
                return False
            result=isSub(A.left,B.left) and isSub(A.right,B.right)
            return result
        return preorder(A,B)
