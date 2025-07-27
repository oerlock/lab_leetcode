from collections import deque


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        给定一个二维整数矩阵 image，代表一张图片。矩阵中的每个元素表示像素点的颜色值（整数形式）。再给定一个起始像素点的坐标 (sr, sc)，以及一个目标颜色值 color。

        你的任务是从这个起始像素开始，将与其“颜色相同且相邻的所有像素”全部改成目标颜色。
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        row = len(image)
        col = len(image[0])
        color_old = image[sr][sc]

        if color_old == color:
            return image

        queue = deque([(sr, sc)])
        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and image[nr][nc] == color_old:
                    queue.append((r + dr, c + dc))

        return image
