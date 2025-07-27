def sliding_window_fixed(nums, k):
    rs = []
    sum_window = sum(nums[:k])
    rs.append(sum_window)
    for i in range(k, len(nums)):
        sum_window += nums[i] - nums[i - k]
        rs.append(sum_window)
    return rs


nums_ = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k_ = 3
print(sliding_window_fixed(nums_, k_))
# 输出: [6, 11, 7, 9, 4, 13, 11]
