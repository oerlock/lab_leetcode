import copy


class Solution(object):
    def permute(self, nums):
        """
        给定一个不含重复数字的数组 nums，返回其所有可能的全排列
        :type nums: List[int]
        :rtype: List[List[int]]
        分析：
            时间复杂度：O(n × n!)
            空间复杂度：O(n × n!)
        """
        rs = []

        def backtrack(nums_, rs_):
            if not nums_:
                rs.append(copy.deepcopy(rs_))
                return

            for i in range(len(nums_)):
                rs_.append(nums_[i])
                backtrack(nums_[:i] + nums_[i + 1:], rs_)
                rs_.pop()

        backtrack(nums, [])
        return rs
