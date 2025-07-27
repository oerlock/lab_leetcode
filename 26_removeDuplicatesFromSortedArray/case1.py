class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        分析：
        ✅ 优点：
            能正确返回不重复元素的个数 k。

            前 k 个位置填上了不重复的元素。

        ❌ 缺点：
            使用了额外的数组 data_，空间复杂度 O(n) —— 违反了题目的空间限制。

            效率低下：i not in data_ 是 O(n) 操作，整个外层循环是 O(n)，所以整体时间复杂度为 O(n²)。

            修改了原数组后面的内容为 '_'，这不是题目要求。题目明确说只要前 k 个元素对即可，后面内容无要求，甚至可以不管。
        """
        data_ = []
        for i in nums:
            if i not in data_:
                data_.append(i)
        k = len(data_)
        for i in range(len(nums)):
            if i < k:
                nums[i] = data_[i]
            else:
                nums[i] = '_'
        return k


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
