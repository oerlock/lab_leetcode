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
        """
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        count = 0

        def bfs(r_, c_):
            queue = deque([(r_, c_)])
            while queue:
                coordinate = queue.popleft()
                if coordinate[0] < 0 or coordinate[1] < 0 or coordinate[0] >= row or coordinate[1] >= col or \
                        grid[coordinate[0]][coordinate[1]] != '1':
                    continue
                grid[coordinate[0]][coordinate[1]] = '0'
                # left
                queue.append((coordinate[0], coordinate[1] - 1))
                # up
                queue.append((coordinate[0] - 1, coordinate[1]))
                # right
                queue.append((coordinate[0], coordinate[1] + 1))
                # down
                queue.append((coordinate[0] + 1, coordinate[1]))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    count += 1
                    bfs(r, c)
        return count
