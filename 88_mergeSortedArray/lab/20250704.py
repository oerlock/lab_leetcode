import time


def merge_1(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] <= nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


def merge_2(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] <= nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    while p1 >= 0:
        nums1[p] = nums1[p1]
        p1 -= 1
        p -= 1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


# 测试运行时间差异
import random

nums1_base = sorted(random.choices(range(10 ** 5), k=5000))
nums2 = sorted(random.choices(range(10 ** 5), k=5000))
nums1_1 = nums1_base + [0] * len(nums2)
nums1_2 = nums1_base + [0] * len(nums2)

start = time.time()
merge_1(nums1_1, len(nums1_base), nums2, len(nums2))
print("merge_1 took:", time.time() - start)

start = time.time()
merge_2(nums1_2, len(nums1_base), nums2, len(nums2))
print("merge_2 took:", time.time() - start)
