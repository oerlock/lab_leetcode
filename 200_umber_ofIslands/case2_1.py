from collections import deque


class Solution(object):
    def numIslands(self, grid):
        """
        给定一个由 '1'（陆地）和 '0'（水）组成的二维网格，统计岛屿的数量。岛被水包围，且同一块岛屿只能由上下左右相邻的陆地连接而成。
        :type grid: List[List[str]]
        :rtype: int
        解题提示： 沉没岛屿法
            ✅ 1. 把二维矩阵看作一个图
                每个 '1' 代表一个节点

                节点与上下左右四个方向的 '1' 相邻则视为连通

            ✅ 2. 思路一：DFS / BFS
                遍历整个网格

                每遇到一个 '1'，就触发一次 DFS/BFS，并把这一块的所有 '1' 标记为 '0'（避免重复）

                每次触发遍历，岛屿数量 +1
        分析：
            🔍 时间与空间复杂度
                时间复杂度： O(m * n)

                空间复杂度： O(min(m, n))（最坏 O(m * n)，队列存储边界）
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r_: int, c_: int):
            queue = deque()
            queue.append((r_, c_))
            grid[r_][c_] = '0'  # 标记为已访问

            while queue:
                x, y = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                        queue.append((nx, ny))
                        grid[nx][ny] = '0'  # 同时标记为已访问

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    bfs(r, c)  # 从当前陆地广度遍历淹没整座岛

        return count
