class Solution(object):
    def subsets(self, nums):
        """
        给定一个包含不同整数的数组 nums，返回所有可能的子集（幂集）。幂集包含数组的所有子集，包括空集
        :type nums: List[int]
        :rtype: List[List[int]]
        分析：
            时间复杂度：
                O(n * 2^n)
            空间复杂度：
                O(n * 2^n)
        """
        rs = []
        len_ = len(nums)

        def backtrack(start, path, num):
            if len(path) == num:
                rs.append(path[:])
                return

            for j in range(start, len_):
                path.append(nums[j])
                backtrack(j + 1, path, num)
                path.pop()

        for num2choose in range(0, len_ + 1):
            backtrack(0, [], num2choose)

        return rs
