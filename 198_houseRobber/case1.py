class Solution(object):
    def rob(self, nums):
        """
        你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都有一定的现金。但是 相邻的两间房不能同时被偷，否则会报警。

        给定一个非负整数数组 nums，代表每个房屋中存放的金额，返回你在不触动警报的情况下，能够偷窃到的最大金额。
        :type nums: List[int]
        :rtype:
        分析：
            时间复杂度 O(n)，空间复杂度 O(n)
        """
        if len(nums) < 3:
            return max(nums)
        rs = [nums[0], max(nums[:2]), max(nums[1], nums[0] + nums[2])]
        for i in range(3, len(nums)):
            tmp_1 = max(rs[i - 2] + nums[i], rs[i - 1])
            rs.append(tmp_1)
        return rs[-1]