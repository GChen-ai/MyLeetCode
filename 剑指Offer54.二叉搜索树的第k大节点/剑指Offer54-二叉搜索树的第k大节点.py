# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack=[root]
        num=0
        result=0
        while stack:
            temp=stack.pop()
            if type(temp)==int:
                num+=1
                if num==k:
                    result=temp
                    return result
            else:
                if temp.left:
                    stack.append(temp.left)
                stack.append(temp.val)
                if temp.right:
                    stack.append(temp.right)
        return result

            