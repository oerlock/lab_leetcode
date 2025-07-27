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
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                rs.append(path[:])  # 浅拷贝：只拷贝最外层对象，内部的对象（如子列表）仍然共享引用
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return rs
