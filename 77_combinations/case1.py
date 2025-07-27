class Solution(object):
    def combine(self, n, k):
        """
        给定两个整数 n 和 k，返回从 1 到 n 中选取 k 个数的所有组合，结果不要求顺序，但不能重复
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        分析：
             🧨 问题点
                path 用的是 set()，不是 list！

                    set 是无序的，不能控制顺序，导致可能重复。

                    比如 {1, 2} 和 {2, 1} 是同一个集合，但遍历时仍然会产生多次。

                用 used[] + set() 是为了解决重复，但这不是组合问题的正解方式。

                不应该用 used[] 来控制选项，组合问题的关键是「递增地选数字」。
            效率较低，会超时间
                时间复杂度：
                    O(P(n,k) * k) = O(n! / (n-k)! * k)
        """
        choices = [i for i in range(1, n + 1)]
        if n == k:
            return [choices]
        rs = set()
        used = [False] * len(choices)

        def backtrack(path):
            if len(path) == k:
                rs.add(tuple(path))
                return

            for i in range(n):
                if used[i]:
                    continue
                path.add(choices[i])
                used[i] = True
                backtrack(path)
                path.remove(choices[i])
                used[i] = False

        backtrack(set())
        return [list(i) for i in rs]
