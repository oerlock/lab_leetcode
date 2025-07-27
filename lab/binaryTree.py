from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_preorder_traversal(root):
    rs = []

    def dfs(node):
        if node is None:
            return
        rs.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return rs


def dfs_preorder_traversal2(root):
    if root is None:
        return []
    stack = [root]
    rs = []
    while stack:
        node = stack.pop()
        rs.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return rs


def dfs_inorder_traversal(root):
    rs = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        rs.append(node.val)
        dfs(node.right)

    dfs(root)
    return rs


def dfs_inorder_traversal2(root):
    stack = []
    cur = root
    rs = []

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        rs.append(cur.val)
        cur = cur.right
    return rs


def dfs_postorder_traversal(root):
    rs = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        dfs(node.right)
        rs.append(node.val)

    dfs(root)
    return rs


def dfs_postorder_traversal2(root):
    if root is None:
        return []
    stack = [root]
    rs = []
    while stack:
        node = stack.pop()
        rs.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    rs.reverse()
    return rs


def dfs_postorder_traversal3(root):
    if root is None:
        return []
    stack = [root]
    stack1 = []

    while stack:
        node = stack.pop()
        stack1.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return stack1[::-1]


def bfs_traversal(root):
    if root is None:
        return []
    queue = deque([root])
    rs = []

    while queue:
        node = queue.popleft()
        rs.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return rs


def bfs_traversal2(root):
    if root is None:
        return []

    queue = deque([root])
    rs = []
    while queue:
        level_s = len(queue)
        level = []

        for _ in range(level_s):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        rs.append(level)
    return rs
