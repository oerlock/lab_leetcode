# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def maxDepth(self, root):
        """
        给定一棵二叉树，求它的最大深度。

        最大深度定义为从根节点到最远叶子节点的最长路径上的节点数。
        :type root: Optional[TreeNode]
        :rtype: int
        分析：
            每层返回“当前节点 + 左右子树最大深度”

            简洁清晰，但对于极深树可能会导致栈溢出（Python 默认递归深度约 1000）
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
