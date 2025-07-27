def complete_knapsack_2d(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n)]
    # 初始化第 0 个物品可以选多次的情况
    # 枚举背包容量 j，从能放下第一个物品的最小容量 weights[0] 开始（更小的就放不下了)，直到最大容量 capacity
    for j in range(weights[0], capacity + 1):
        # (j // weights[0])：在容量 j 下，最多能放下几个第 0 个物品
        # (j // weights[0]) * values[0]：放下这些第 0 个物品后，总价值是多少
        # dp[0][j] = ...：结果记录在 dp[0][j] 里：只考虑第一个物品时，容量为 j 的最大价值
        dp[0][j] = (j // weights[0]) * values[0]

    for i in range(1, n):
        for j in range(capacity + 1):
            # 不选第 i 个物品
            dp[i][j] = dp[i - 1][j]
            # 如果可以选第 i 个物品（可以重复），尝试更新
            if j >= weights[i]:
                dp[i][j] = max(dp[i][j], dp[i][j - weights[i]] + values[i])

    for i in dp:
        print(i)

    return dp[n - 1][capacity]


if __name__ == '__main__':
    weights = [1, 3, 4]
    values = [15, 20, 30]
    capacity = 4
    print(complete_knapsack_2d(weights, values, capacity))
    # 输出：60
