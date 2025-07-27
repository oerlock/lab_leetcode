class Solution(object):
    def moveZeroes(self, nums):
        """
        给定一个整数数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        分析：
            ✅ 正确性
                所有非零元素按原顺序排列；

                所有零都被移动到末尾；

                操作 原地进行，空间复杂度为 O(1)；

                时间复杂度为 O(n)，一次遍历。
            小优化建议（可读性）
                * 交换语句可以写得更 Pythonic：nums[i], nums[k] = nums[k], nums[i]
                * 如果 i == k，就不需要交换，避免不必要的赋值
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[k]
                nums[k] = temp
                k += 1
        return nums