# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root,max_depth,cur,path):
            cur+=1
            if root==None:
                return max_depth
            if (cur>max_depth):
                max_depth=cur
                path.append(root.val)
            max_depth=max(max_depth,dfs(root.right,max_depth,cur,path))
            max_depth=max(max_depth,dfs(root.left,max_depth,cur,path))
            return max_depth
        if root==None:return []
        path=[]
        dfs(root,0,0,path)
        return path
