class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        rs = [1, 1, 2]
        for i in range(3, n + 1):
            rs.append(rs[i - 1] + rs[i - 2])
        return rs[n]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(6))
