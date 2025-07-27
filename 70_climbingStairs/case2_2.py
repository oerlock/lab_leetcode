class Solution(object):
    def climbStairs(self, n):
        """
        假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

        每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶？
        :type n: int
        :rtype: int
        分析：
            时间复杂度
                O(n)
            空间复杂度
                O(1)
        """
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(6))
