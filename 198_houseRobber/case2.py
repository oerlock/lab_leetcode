class Solution(object):
    def rob(self, nums):
        """
        你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都有一定的现金。但是 相邻的两间房不能同时被偷，否则会报警。

        给定一个非负整数数组 nums，代表每个房屋中存放的金额，返回你在不触动警报的情况下，能够偷窃到的最大金额。
        :type nums: List[int]
        :rtype: int
        分析：
            时间复杂度 O(n)，空间复杂度 O(1)
        """
        if len(nums) == 1:
            return nums[0]
        a, b = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            a, b = b, max(b, a + nums[i])
        return b
