class Solution(object):
    def singleNumber(self, nums):
        """
        给定一个 非空 整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
        :type nums: List[int]
        :rtype: int
        """
        rs = nums[0]
        for i in nums[1:]:
            rs ^= i
        return rs
