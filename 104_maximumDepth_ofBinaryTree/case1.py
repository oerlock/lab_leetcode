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
            时间复杂度：O(N)，其中 N 是节点数量，每个节点只访问一次。

            空间复杂度：O(W)，其中 W 是树的最大宽度，最坏是满二叉树，W ≈ N/2。
        """
        if root is None:
            return 0

        queue = deque([root])
        rs = []
        while queue:
            level_s = len(queue)
            level = []
            for _ in range(level_s):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            rs.append(level)
        return len(rs)
