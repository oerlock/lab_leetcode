# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        给定一棵二叉树的根节点 root 和一个整数 targetSum，判断是否存在一条从 根节点到叶子节点 的路径，满足路径上的节点值之和等于 targetSum。
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        分析：
        """
        if root is None:
            return False

        queue = deque([(root, root.val)])

        while queue:
            node, curr_sum = queue.popleft()

            # 如果是叶子节点
            if node.left is None and node.right is None:
                if curr_sum == targetSum:
                    return True

            if node.left:
                queue.append((node.left, curr_sum + node.left.val))
            if node.right:
                queue.append((node.right, curr_sum + node.right.val))

        return False