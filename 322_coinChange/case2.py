class Solution(object):
    def coinChange(self, coins: list, amount):
        """
        给定一组 硬币面额 coins 和一个目标金额 amount，我们要找出组成该金额所需的 最少硬币数量。如果无法组合成目标金额，返回 -1。
        :type coins: List[int]
        :type amount: int
        :rtype: int
        思路：
            1、状态定义：dp[i] = 凑出金额 i 所需的最小硬币数
            2、初始化：dp = [amount + 1] * (amount + 1) dp[0] = 0
                我们的目标是从 dp[0] 一直推到 dp[amount]

                dp[0] = 0：因为凑出 0 元，不需要任何硬币

                其他的初始值应该设置为一个「足够大」的值，通常用 amount + 1（比最大可能的硬币数还大）
            3、状态转移方程（核心）：dp[i] = min(dp[i], dp[i - coin] + 1)
                如果我使用了 coin 这个硬币，剩下的就是 i - coin 元

                那么 dp[i - coin] + 1 就是当前这一选择所需要的总硬币数（+1 是因为我们用了一个 coin）

                在所有可选的 coin 中，我们取最小的
        分析：
            时间复杂度：O(amount × n)，其中 n 是硬币种类数

            空间复杂度：O(amount)
        """
        dp = [amount + 1] * (amount + 1)  # 初始设置为无穷大
        dp[0] = 0  # base case：凑出0元需要0个硬币

        for i in range(1, amount + 1):  # 从金额1开始
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1

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
