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
        """
        if root is None:
            return False

        stack = [(root, root.val)]  # 栈中保存 (节点, 当前路径和)

        while stack:
            node, curr_sum = stack.pop()

            # 如果是叶子节点，判断当前路径和是否等于 targetSum
            if node.left is None and node.right is None:
                if curr_sum == targetSum:
                    return True

            # 把子节点压入栈，并更新路径和
            if node.right:
                stack.append((node.right, curr_sum + node.right.val))
            if node.left:
                stack.append((node.left, curr_sum + node.left.val))

        return False