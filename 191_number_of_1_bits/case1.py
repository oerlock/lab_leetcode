class Solution(object):
    def hammingWeight(self, n):
        """
        给定一个正整数 n，返回其二进制表示中 1 的个数
        :type n: int
        :rtype: int
        分析：
            复杂度是 O(log n), 整数 n 的二进制长度是 log₂(n) 级别
            空间复杂度：O(log n)（由于字符串的创建）

            没有利用位运算
        """
        count_1 = 0
        for i in bin(n)[2:]:
            if i == '1':
                count_1 += 1
        return count_1
