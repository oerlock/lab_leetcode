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
            部分	功能	正确性	问题
            拷贝部分	把 nums2 复制到 nums1 后半	有问题 索引应是 i - m，不是 i - n
            排序部分	尝试排序 nums1	❌ 错误	只做了一轮冒泡，排序不完整，无法保证有序性
        """
        for i in range(m, m + n):
            nums1[i] = nums2[i - n]
        i = 0
        while i < m + n - 1:
            if nums1[i] > nums1[i + 1]:
                tmp_ = nums1[i]
                nums1[i] = nums1[i + 1]
                nums1[i + 1] = tmp_
            i += 1
