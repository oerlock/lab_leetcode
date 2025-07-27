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
            ✅ 正确性：10/10
            代码逻辑正确，对于符合条件的两个数，能返回其索引。

            🐢 性能效率：3/10
            使用了两层 for 循环，时间复杂度为 O(n²)，对于大输入会变慢，Leetcode 上可能会超时。

            🎯 可读性：6/10
            结构尚清晰，但变量命名可以更准确，嵌套 if + continue 可简化为 if 条件就 return。

            🧼 代码简洁性：5/10
            多余比较 if idx == idx2 是为了避免同一元素重复使用，但可以通过更优解方式（使用一个哈希表（dict）记录已经看过的数值及其索引）避免。return None 在 Leetcode 上可以省略（题目假设一定有解）。
        """
        for idx, val in enumerate(nums):
            for idx2, val2 in enumerate(nums):
                if idx == idx2 or val + val2 != target:
                    continue
                return [idx, idx2]
        return None


def test_solution():
    import time

    s = Solution()
    test_input_output = [
        ([2, 7, 11, 15], 9, {0, 1}),
        ([3, 2, 4], 6, {1, 2}),
        ([3, 3], 6, {0, 1}),
        # (list(range(100000)) + [99999], 199998, {99998, 100000})  # 大输入测试
    ]
    print()
    for idx, (input_list, target, expected) in enumerate(test_input_output):
        start = time.perf_counter()
        result = set(s.twoSum(input_list, target))
        end = time.perf_counter()
        duration = (end - start) * 1000  # 转换为毫秒
        assert result == expected, f"Test {idx + 1} failed: got {result}, expected {expected}"
        print(f"Test {idx + 1}: Passed in {duration:.3f} ms")
