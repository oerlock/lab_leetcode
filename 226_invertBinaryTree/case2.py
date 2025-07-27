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
            时间复杂度：O(n)

                每个节点只访问一次。

            空间复杂度：

                最多同时有一层的节点在队列中，最坏情况下 O(n)。
        """
        if root is None:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
