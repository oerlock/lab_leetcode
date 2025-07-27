class Solution(object):
    def removeDuplicates(self, nums):
        """
        给你一个升序排列的整数数组 nums，请你原地删除重复出现的元素，使每个元素只出现一次，返回删除后数组的新长度。

        不允许使用额外的数组空间，必须在原地修改输入数组并使用 O(1) 额外空间。
        :type nums: List[int], 非递减列表
        :rtype: int
        分析：
        💡 思路：
            用 i 指向已处理数组的最后一个不重复元素。

            用 j 向后扫描，遇到与 nums[i] 不同的元素，就 i += 1，然后 nums[i] = nums[j]。

            最终 i + 1 就是去重后数组长度。

        ⏱️ 复杂度：
            时间复杂度：O(n)

            空间复杂度：O(1)（题目要求）
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


def test_solution():
    s = Solution()
    test_input_output = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
    ]
    for i in test_input_output:
        rs = s.removeDuplicates(i[0])
        assert rs == i[1]
        assert i[0][:rs] == i[2]
