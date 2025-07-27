class Solution(object):
    def combine(self, n, k):
        """
        给定两个整数 n 和 k，返回从 1 到 n 中选取 k 个数的所有组合，结果不要求顺序，但不能重复
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        分析：
            时间复杂度：
                O(C(n,k) * k)
        """
        choices = [i for i in range(1, n + 1)]
        if n == k:
            return [choices]
        rs = []

        def backtrack(start, path):
            if len(path) == k:
                rs.append(path[:])
                return

            for i in range(start, n):
                path.append(choices[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return rs
