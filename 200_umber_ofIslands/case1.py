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
            ✅ 时间复杂度：
                O(m * n)：每个格子最多访问一次

            ✅ 空间复杂度：
                O(m * n) 最坏情况是整个网格是陆地（递归栈深度），可以优化为 BFS 减少递归风险。
        """
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        count = 0

        def dfs(r_, c_):
            if r_ < 0 or r_ >= row or c_ < 0 or c_ >= col or grid[r_][c_] != '1':
                return
            grid[r_][c_] = '0'
            # left
            dfs(r_, c_ - 1)
            # up
            dfs(r_ - 1, c_)
            # right
            dfs(r_, c_ + 1)
            # down
            dfs(r_ + 1, c_)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count
