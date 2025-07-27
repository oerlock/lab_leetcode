# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        你要做的是将一棵二叉树“镜像翻转”——即：

        所有的左子树和右子树互换位置。
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        分析：
            时间复杂度：O(n)
                每个节点都访问一次。

            空间复杂度：

                最好情况下（完全平衡）：O(log n)（递归栈高度 = 树的高度）

                最坏情况下（退化为链表）：O(n)
        """
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
