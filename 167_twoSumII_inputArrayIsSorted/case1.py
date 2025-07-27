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
            ✅ 优点：
                简单直观，容易理解。

                在数组很小的情况下能正常工作。

            ❌ 缺点：
                时间复杂度是 O(n²)，对于大数组效率低。

                没有利用“数组是有序的”这个条件。
        """
        tmp_ = len(numbers)
        for i in range(tmp_):
            for j in range(i + 1, tmp_):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []
