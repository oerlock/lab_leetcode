class Solution(object):
    def hammingWeight(self, n):
        """
        给定一个正整数 n，返回其二进制表示中 1 的个数
        :type n: int
        :rtype: int
        分析：
            空间复杂度 O(1)
            时间复杂度 O(log n)
        """
        count_1 = 0
        while n > 0:
            count_1 += n & 1
            n >>= 1
        return count_1
