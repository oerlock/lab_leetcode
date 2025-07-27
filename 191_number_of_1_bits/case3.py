class Solution(object):
    def hammingWeight(self, n):
        """
        给定一个正整数 n，返回其二进制表示中 1 的个数
        :type n: int
        :rtype: int
        分析：
            n & (n - 1) 的位运算技巧可以高效地清除最低位的 1

            时间复杂度是 O(k)，其中 k 是 1 的数量，通常远远小于 32
            空间复杂度：O(1)
        """
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
    