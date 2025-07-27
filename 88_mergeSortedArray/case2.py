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
            使用了 O(n²) 的选择排序，对大数组效率极差
        """
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]

        for idx in range(len(nums1)):
            for idx1 in range(idx + 1, len(nums1)):
                if nums1[idx] > nums1[idx1]:
                    nums1[idx1], nums1[idx] = nums1[idx], nums1[idx1]