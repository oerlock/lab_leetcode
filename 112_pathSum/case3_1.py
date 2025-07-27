# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        给定一棵二叉树的根节点 root 和一个整数 targetSum，判断是否存在一条从 根节点到叶子节点 的路径，满足路径上的节点值之和等于 targetSum。
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        分析：
            伪装成中序结构的前序遍历
        """
        stack = []
        cur = (root, root.val if root else 0)

        while stack or cur[0]:
            while cur[0]:
                node, sum_ = cur
                stack.append(cur)
                if node.left is None and node.right is None:
                    if sum_ == targetSum:
                        return True
                cur = (node.left, sum_ + (node.left.val if node.left else 0))

            node, sum_ = stack.pop()
            if node.left is None and node.right is None:
                if sum_ == targetSum:
                    return True
            cur = (node.right, sum_ + (node.right.val if node.right else 0))
        return False
