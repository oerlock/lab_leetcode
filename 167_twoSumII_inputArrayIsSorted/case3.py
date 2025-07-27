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
            🔥 时间 & 空间复杂度：
                时间复杂度：O(n)

                空间复杂度：O(1)（只用了两个指针）

            ✨ 逻辑解释：
                如果两数之和 s < target，说明需要更大的数，移动 left。

                如果 s > target，说明需要更小的数，移动 right。

                找到后返回（根据题目假设，一定存在解）。
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            sum_num = numbers[left] + numbers[right]
            if sum_num > target:
                right = right - 1
            elif sum_num < target:
                left = left + 1
            else:
                return [left + 1, right + 1]
        return []
