# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def rec(preorder,pl,pr,inorder,il,ir):
            if pl>pr or il>ir:
                return None
            root=TreeNode(preorder[pl])
            index=il
            while index<=ir:
                if inorder[index]==root.val:
                    break
                index+=1
            length=index-il
            root.left=rec(preorder,pl+1,pl+length,inorder,il,index-1)
            root.right=rec(preorder,pl+length+1,pr,inorder,index+1,ir)
            return root
        if preorder==None or inorder==None:
            return None
        return rec(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
            