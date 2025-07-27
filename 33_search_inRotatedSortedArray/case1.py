class Solution(object):
    def search(self, nums, target):
        """
        给定一个升序排列的整数数组 nums，数组在某个未知的下标处进行了旋转（即变成了一个旋转数组），例如：

            原数组是 [0, 1, 2, 4, 5, 6, 7]
            可能被旋转成 [4, 5, 6, 7, 0, 1, 2]

        现在，给定一个目标值 target，如果数组中存在这个目标值，返回它的索引，否则返回 -1。

        你必须在 O(log n) 时间复杂度内完成搜索。
        :type nums: List[int]
        :type target: int
        :rtype: int
        分析：
            思路：
                这个题的关键是理解 旋转数组的结构 仍然部分有序，我们可以在这个结构上做 二分查找（O(log n)）。
            时间复杂度：O(log n)
            空间复杂度：O(1)
        """
        p_l, p_r = 0, len(nums) - 1
        while p_l <= p_r:
            mid = (p_l + p_r) // 2
            if nums[mid] == target:
                return mid
            if nums[p_r] <= nums[mid]:
                # 左半边有序
                if nums[p_l] <= target < nums[mid]:
                    # target 在左半边
                    p_r = mid - 1
                else:
                    p_l = mid + 1
            else:
                # 右半边有序
                if nums[mid] < target <= nums[p_r]:
                    # target 在右半边
                    p_l = mid + 1
                else:
                    p_r = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([4, 5, 6, 7, 8, 1, 2, 3], 8))
