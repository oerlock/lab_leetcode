class Solution(object):
    def maxSubArray(self, nums):
        """
        给定一个整数数组 nums，找到一个具有最大和的连续子数组（至少包含一个元素），返回其最大和。
        :type nums: List[int]
        :rtype: int
        分析：
            在每一步都思考当前这个数是否应该加入之前的“连续子数组”，还是重新开始一个新的子数组。
            时间复杂度：O(n)，只遍历了一遍数组。

            空间复杂度：O(1)，只用了两个变量。
        """
        sum_current = nums[0]
        sum_max = nums[0]
        for i in nums[1:]:
            sum_current = max(i, sum_current + i)
            sum_max = max(sum_max, sum_current)
        return sum_max


if __name__ == '__main__':
    s = Solution()
    nums_ = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(nums_))
