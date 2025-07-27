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
        """
        map_idx = {}
        for i in range(len(nums)):
            tmp_ = target - nums[i]
            if tmp_ in map_idx:
                return [map_idx[tmp_], i]
            map_idx[nums[i]] = i
        return []
