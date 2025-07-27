class Solution(object):
    def searchInsert(self, nums, target):
        """
        给定一个 升序排列 的整数数组 nums 和一个目标值 target，请返回该目标值应该插入的位置，使得数组仍保持有序。
            如果目标值存在于数组中，返回其索引。

            如果不存在，返回它应该被插入的位置索引。
        :type nums: List[int]
        :type target: int
        :rtype: int
        分析：
            时间复杂度是 O(log n)
            空间复杂度是 O(1)
        """
        p_l, p_r = 0, len(nums) - 1
        while p_l <= p_r:
            mid = (p_l + p_r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                p_l = mid + 1
            else:
                p_r = mid - 1
        return p_l
