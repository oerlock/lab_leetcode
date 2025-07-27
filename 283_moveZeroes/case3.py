class Solution(object):
    def moveZeroes(self, nums):
        """
        给定一个整数数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        分析：
            先把所有非零元素往前放；

            再把后面剩下的部分全部补 0。
        """
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        for i in range(insert_pos, len(nums)):
            nums[i] = 0