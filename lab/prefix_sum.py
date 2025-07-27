# 原数组
nums = [2, 4, 5, 7, 1, 3]
# 构造前缀和数组：prefix_sum[i] 表示前 i 个数的总和（不含 nums[i] 本身）
prefix_sum = [0]  # 初始为0，方便计算
for num in nums:
    prefix_sum.append(prefix_sum[-1] + num)
# 查询闭区间 [1, 3] 的和：nums[1] + nums[2] + nums[3]
l, r = 1, 3
result = prefix_sum[r + 1] - prefix_sum[l]
print(result)  # 输出 16（4 + 5 + 7）