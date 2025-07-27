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
                O(n)
        """
        rs = 0
        tmp_ = [0]
        for i in range(1, n + 1):
            if i == 1:
                rs = 1
                tmp_.append(1)
            elif i == 2:
                rs = 2
                tmp_.append(2)
            else:
                rs = tmp_[i - 1] + tmp_[i - 2]
                tmp_.append(rs)
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(6))
