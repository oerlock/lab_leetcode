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
            ✅ 简洁点总结：
                直接用 level == level[::-1] 判断是否对称；

                用 for _ in range(len(queue)) 来处理每层；

                节点展开只对非空节点，避免重复判断；

                保留 None 作为空位，用于结构判断。
        """
        if not root:
            return True

        queue = deque([root])

        while queue:
            level = [node.val if node else None for node in queue]

            if level != level[::-1]:
                return False

            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)

        return True
