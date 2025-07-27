import bisect

nums = [1, 3, 4, 6, 9]
target = 4
index = bisect.bisect_left(nums, target)
if index < len(nums) and nums[index] == target:
    print("找到了，在索引", index)
else:
    print("没找到")