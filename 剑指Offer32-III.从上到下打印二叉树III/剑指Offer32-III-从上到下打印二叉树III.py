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
        :rtype: List[List[int]]
        """
        queue=[root]
        pre=1
        cur=0
        result=[]
        mark=1
        while queue and root:
            temp=[]
            while pre>0:
                curNode=queue.pop(0)
                temp.append(curNode.val)
                if curNode.left:
                    queue.append(curNode.left)
                    cur+=1
                if curNode.right:
                    queue.append(curNode.right)
                    cur+=1
                pre-=1
            pre=cur
            cur=0
            if mark>0:
                result.append(temp)
            else:
                result.append(temp[::-1])
            mark=-mark
        return result