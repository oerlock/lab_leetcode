def knapsack_01(weights, values, capacity):
    # n: 物品的数量
    n = len(weights)
    # dp: Dynamic Programming table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):  # 遍历物品
        for j in range(capacity + 1):  # 遍历容量
            if j < weights[i - 1]:
                # 当前背包容量 j 不足以容纳第 i 个物品（注意 Python 中下标从 0 开始，所以物品对应的是 weights[i - 1]），因此不能选择这个物品
                dp[i][j] = dp[i - 1][j]  # 不能选
            else:
                dp[i][j] = max(
                    dp[i - 1][j],  # 不选
                    dp[i - 1][j - weights[i - 1]] + values[i - 1]  # 选
                )

    for i in dp:
        print(i)

    return dp[n][capacity]


if __name__ == '__main__':
    weights = [2, 1, 3]
    values = [4, 2, 3]
    capacity = 4
    print(knapsack_01(weights, values, capacity))  # 输出 6
