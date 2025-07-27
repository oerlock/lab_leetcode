class Solution(object):
    def climbStairs(self, n):
        """
        假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

        每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶？
        :type n: int
        :rtype: int
        分析：
            时间复杂度：
                O(2ⁿ)
            空间复杂度：
                O(n)
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))
