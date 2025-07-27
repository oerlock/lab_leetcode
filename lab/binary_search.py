def binary_search(nums, target):
    left, right = 0, len(nums) - 1  # 左闭右闭 [left, right]
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid  # 找到了
        elif nums[mid] < target:
            left = mid + 1  # 去右边找
        else:
            right = mid - 1  # 去左边找
    return -1  # 没找到
