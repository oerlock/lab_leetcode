class Solution(object):
    def rob(self, nums):
        """
        你是一个专业的小偷，计划偷窃一条街上的房屋。每间房内都有一定金额的现金。然而，这条街上的所有房屋都 围成一个环，也就是说，第一个房屋和最后一个房屋是相邻的。相邻的房屋不能被同时打劫。

        给你一个整数数组 nums，每个元素表示每个房屋的钱数，返回你能够偷窃到的最大金额。
        :type nums: List[int]
        :rtype: int

        分析：
            🧠 解题思路：动态规划 + 环形结构处理
                由于首尾相连，我们不能同时偷第一个和最后一个房子。

                所以将问题拆成两个线性问题：

                不偷最后一个房子，即偷 nums[0] 到 nums[n-2]。

                不偷第一个房子，即偷 nums[1] 到 nums[n-1]。
            时间复杂度：O(n)
            空间复杂度：O(1)
        """
        if len(nums) == 1:
            return nums[0]

        def rob_line(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            a, b = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                a, b = b, max(b, a + nums[i])
            return b

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
