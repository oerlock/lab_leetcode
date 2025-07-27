class Solution(object):
    def maxProduct(self, nums):
        """
        给定一个整数数组 nums，找出一个乘积最大的连续子数组（子数组长度至少为 1），返回该子数组的乘积。
        :type nums: List[int]
        :rtype: int
        分析：
            复杂度：
                时间复杂度：O(n) —— 遍历一次数组
                空间复杂度：O(1) —— 常数空间（只用了几个变量）
        """
        product_current_max = nums[0]
        product_current_min = nums[0]
        product_max = nums[0]
        product_min = nums[0]
        for i in nums[1:]:
            product_current_max_ = max(i, product_current_max * i, product_current_min * i)
            product_current_min_ = min(i, product_current_max * i, product_current_min * i)
            product_max = max(product_current_max_, product_max)
            product_min = min(product_current_min_, product_min)
            product_current_max = product_current_max_
            product_current_min = product_current_min_
        return product_max


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([-4, -3, -2]))  # 12
