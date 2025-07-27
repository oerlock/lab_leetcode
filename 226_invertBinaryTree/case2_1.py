# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def invertTree(self, root):
        """
        你要做的是将一棵二叉树“镜像翻转”——即：

        所有的左子树和右子树互换位置。
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        分析：
            🧮 时间与空间复杂度
                时间复杂度：O(n)
                每个节点访问一次。

            空间复杂度：O(h) ~ O(n)

                h 是树的高度。

                最坏情况是链式树，栈深 O(n)。
        """
        if root is None:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
