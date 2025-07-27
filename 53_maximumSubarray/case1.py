class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = [0]
        for i in nums:
            prefix_sum.append(prefix_sum[-1] + i)
        rs = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                rs = max(rs, prefix_sum[j + 1] - prefix_sum[i])
        return rs


if __name__ == '__main__':
    s = Solution()
    nums_ = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(nums_))
