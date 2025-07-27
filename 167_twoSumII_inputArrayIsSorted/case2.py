class Solution(object):
    def twoSum(self, numbers, target):
        """
        给定一个 升序排序的整数数组 numbers，以及一个目标值 target。

        找出两个数的下标（从1开始），使它们相加之和等于 target。

        你可以假设恰好存在一个解，并且每个输入只使用一次。

        要求：使用 O(1) 的额外空间。
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        分析：
            虽然 代码本身是正确的，但是 不符合本题的空间要求：

            本题的数组是 升序排序的，我们应该利用这一点。

            本题期望的是：使用 O(1) 的额外空间。

            你使用了一个哈希表 data_，这会额外消耗 O(n) 的空间。
        """
        data_ = {}
        for index, num in enumerate(numbers):
            tmp_ = target - num
            if tmp_ in data_:
                return [data_[tmp_] + 1, index + 1]
            data_[num] = index
        return []
