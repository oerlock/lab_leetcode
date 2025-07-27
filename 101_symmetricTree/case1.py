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
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        queue = deque([root])
        rs = []

        while queue:
            level_s = len(queue)
            level = []
            for _ in range(level_s):
                node = queue.popleft()
                level.append(node.val if node else None)
                if node is None:
                    continue
                queue.append(node.left)
                queue.append(node.right)

            rs.append(level)

        for i in rs:
            if not i:
                continue
            left, right = 0, len(i) - 1
            while left < right:
                if i[left] != i[right]:
                    return False
                left += 1
                right -= 1
        return True
