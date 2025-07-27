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

        def dfs(sr_, sc_):
            if sr_ < 0 or sr_ >= row or sc_ < 0 or sc_ >= col or image[sr_][sc_] != color_old:
                return
            image[sr_][sc_] = color
            for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(sr_ + i[0], sc_ + i[1])

        dfs(sr, sc)
        return image
