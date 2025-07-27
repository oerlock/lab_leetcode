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
            不记录每一层的节点值
        """
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            depth += 1

        return depth
