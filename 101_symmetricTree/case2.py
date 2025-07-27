# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def isSymmetric(self, root):
        """
        给定一个二叉树，判断它是否是镜像对称的
        镜像对称的意思是：左子树是右子树的镜像，即：

        left.val == right.val

        left.left == right.right

        left.right == right.left

        一直到所有节点都满足这个镜像关系
        :type root: Optional[TreeNode]
        :rtype: bool
        分析：
        """

        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return (isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left))

        return isMirror(root.left, root.right)