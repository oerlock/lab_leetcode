from itertools import combinations


class Solution(object):
    def combine(self, n, k):
        """
        给定两个整数 n 和 k，返回从 1 到 n 中选取 k 个数的所有组合，结果不要求顺序，但不能重复
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(combinations(range(1, n + 1), k))
