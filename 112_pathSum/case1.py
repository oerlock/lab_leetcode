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
            ❗️问题点：
                代码虽然能跑通，但逻辑上有 重复检查 和 不必要的复杂性：

                你在左右子树分别递归后又手动检查是否为叶子节点并判断 targetSum == 0，这是冗余的。

                实际上这个判断应该只在当前节点是叶子节点时做，而不是在递归之后重复判断。

            时间和空间复杂度分析：
                时间复杂度：O(N)，其中 N 是树中的节点数。最坏情况下要遍历每一个节点。

                空间复杂度：O(H)，其中 H 是树的高度。递归调用栈的深度最深为树高。
        """
        if root is None:
            return False
        targetSum -= root.val

        rs = self.hasPathSum(root.left, targetSum)
        if rs or (root.left is None and root.right is None and targetSum == 0):
            return True

        rs = self.hasPathSum(root.right, targetSum)
        if rs or (root.left is None and root.right is None and targetSum == 0):
            return True

        return False