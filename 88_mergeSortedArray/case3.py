class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        给你两个有序整数数组 nums1 和 nums2，以及两个整数 m 和 n，分别表示 nums1 和 nums2 中的有效元素数量。
        nums1 的长度是 m + n，后 n 个元素是占位的 0。

        你需要将 nums2 中的元素合并到 nums1 中，使得结果有序，并且原地修改 nums1。

        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        分析：
            利用两个数组有序的性质，使用双指针逆序归并
                时间复杂度：O(m + n)
                空间复杂度：O(1)（原地操作）
        """
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
