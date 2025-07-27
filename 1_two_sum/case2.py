class Solution(object):
    def twoSum(self, nums, target):
        """
        给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回它们的数组下标。

        你可以假设每种输入只会对应一个答案，但是，同一个元素不能使用两遍。

        你可以按任意顺序返回答案。
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        分析：
            ✅ 功能分析
                🎯 正确性：完全正确
            📈 性能分析
                ⏱ 时间复杂度：O(n)
                每个元素最多处理一次，哈希表查找/插入是 O(1)

                🧠 空间复杂度：O(n)
                哈希表 data_ 可能需要存储最多 n 个元素（每个数字及其索引）
        """
        data_ = {}  # val: idx
        for idx, var in enumerate(nums):
            tmp_ = target - var
            if tmp_ in data_:
                return [data_[tmp_], idx]
            data_[var] = idx
        return None


def test_solution():
    import time

    s = Solution()
    test_input_output = [
        ([2, 7, 11, 15], 9, {0, 1}),
        ([3, 2, 4], 6, {1, 2}),
        ([3, 3], 6, {0, 1}),
        (list(range(100000)) + [99999], 199998, {99999, 100000})  # 大输入测试
    ]
    print()
    for idx, (input_list, target, expected) in enumerate(test_input_output):
        start = time.perf_counter()
        result = set(s.twoSum(input_list, target))
        end = time.perf_counter()
        duration = (end - start) * 1000  # 转换为毫秒
        assert result == expected, f"Test {idx + 1} failed: got {result}, expected {expected}"
        print(f"Test {idx + 1}: Passed in {duration:.3f} ms")
