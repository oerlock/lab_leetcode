class Solution(object):
    def moveZeroes(self, nums):
        """
        给定一个整数数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        分析：
        ✅ 优点
            原地修改，符合题目要求。

            算法复杂度为 O(n)，空间复杂度为 O(1)。

        ⚠️ 注意点
            p2 一定要走在 p1 前面，否则会漏掉元素或陷入死循环。

            每次交换后两个指针都前进，可以保证非零元素的顺序不变。
        """
        p1 = 0
        p2 = 1
        while p2 < len(nums):
            if nums[p1] == 0 and nums[p2] == 0:
                p2 += 1
                continue
            if nums[p1] == 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 += 1
