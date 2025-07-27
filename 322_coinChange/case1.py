class Solution(object):
    def coinChange(self, coins: list, amount):
        """
        给定一组 硬币面额 coins 和一个目标金额 amount，我们要找出组成该金额所需的 最少硬币数量。如果无法组合成目标金额，返回 -1。
        :type coins: List[int]
        :type amount: int
        :rtype: int
        分析：
            物品重量：每个硬币的面额。

            物品价值：每投放一个硬币价值为1（代表数量）。

            背包容量：amount。

            求解：背包容量恰好装满的情况下，使价值（硬币数）最小。

            状态定义: dp[i] = 组成金额 i 所需的最少硬币数

            复杂度
                时间复杂度：O(amount × n)，其中 n 是硬币种类数

                空间复杂度：O(n × amount)
        """
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 0

        for i in range(n):
            for j in range(1, amount + 1):
                if i > 0:
                    dp[i][j] = dp[i - 1][j]
                if j >= coins[i]:
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i]] + 1)

        # for i in dp:
        #     print(i)

        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1


if __name__ == '__main__':
    s = Solution()
    # rs = s.coinChange([186,419,83,408], 6249)
    # rs = s.coinChange([1, 2, 5], 11)  # 3
    rs = s.coinChange([2,5,10,1], 27)  # 4
    # rs = s.coinChange([2], 1)  # -1
    # rs = s.coinChange([2], 3)  # -1
    # rs = s.coinChange([1], 0)  # 0
    # rs = s.coinChange([1, 2], 2)  # 1
    print(rs)
