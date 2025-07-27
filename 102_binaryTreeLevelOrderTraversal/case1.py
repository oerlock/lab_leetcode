# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        给你一棵二叉树，请你返回其按层序遍历的节点值（即从左到右，一层一层地遍历）。
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        分析：
            ✅ 复杂度：
                O(N)：每个节点进队出队各一次，N 是节点数量。

                O(N)：空间用于 queue 和 rs。
        """
        if root is None:
            return []
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
        return rs
