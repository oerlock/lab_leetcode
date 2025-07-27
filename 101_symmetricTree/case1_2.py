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
            ✅ 优点
                思路直观，通过每层的对称性间接判断整棵树的对称；

                不需要额外定义递归函数，只用队列完成遍历。

            ⚠️ 需要注意的点
                必须保留空节点（None）的信息，否则无法判断结构对称（比如左右子树一个空一个非空）；

                该方法是 层序+结构判断，但如果某些更复杂的镜像关系，结构相同但位置错乱，可能需要更底层的判断；

                空树视为对称（root=None 时返回 True）。
        """
        queue = deque([root])

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

            if not level:
                continue
            left, right = 0, len(level) - 1
            while left < right:
                if level[left] != level[right]:
                    return False
                left += 1
                right -= 1

        return True
