class UnionFind:
    def __init__(self, grid: list[list[str]]):
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.count = 0
        self.parent: list[int] = [-1] * (self.rows * self.cols)

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == '1':
                    idx = r * self.cols + c
                    self.parent[idx] = idx
                    self.count += 1  # 初始认为每个陆地是一个岛

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])  # 路径压缩
        return self.parent[i]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.count -= 1  # 合并两个不同集合，岛屿数 -1


class Solution(object):
    def numIslands(self, grid):
        """
        给定一个由 '1'（陆地）和 '0'（水）组成的二维网格，统计岛屿的数量。岛被水包围，且同一块岛屿只能由上下左右相邻的陆地连接而成。
        :type grid: List[List[str]]
        :rtype: int
        解题提示：
            ✅ 1. 把二维矩阵看作一个图
                每个 '1' 代表一个节点

                节点与上下左右四个方向的 '1' 相邻则视为连通

            ✅ 3. 思路二：并查集（Union-Find）
                把每个 '1' 看成一个节点

                把相邻的 '1' 合并为一个集合

                最后统计集合个数（去除 '0' 对应的部分）
        分析：
            总时间复杂度： O(m * n * α(m * n)) ≈ O(m * n)
                和 BFS/DFS 解法一样，接近线性时间
            空间复杂度：O(m * n)
                空间比 DFS 更稳定
        """
        if not grid:
            return 0

        uf = UnionFind(grid)
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    grid[r][c] = '0'  # 标记已访问
                    for dr, dc in [(1, 0), (0, 1)]:  # 只需要合并右边和下边
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            id1 = r * cols + c
                            id2 = nr * cols + nc
                            uf.union(id1, id2)

        return uf.count
