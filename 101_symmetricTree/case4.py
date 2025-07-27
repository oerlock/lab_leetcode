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
        给定一个二叉树，判断它是否是镜像对称的
        镜像对称的意思是：左子树是右子树的镜像，即：

        left.val == right.val

        left.left == right.right

        left.right == right.left

        一直到所有节点都满足这个镜像关系
        :type root: Optional[TreeNode]
        :rtype: bool
        分析：
            🧱 栈（DFS）方式解法
                我们将一对对节点（应当是对称的）压入栈中，每次从栈中取出一对，进行对比。
        """

        if not root:
            return True

        stack = [(root.left, root.right)]

        while stack:
            left, right = stack.pop()

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            # 成对压入左右子节点，保持对称结构
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True