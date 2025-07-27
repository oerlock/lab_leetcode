map_digit = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


class Solution(object):
    def letterCombinations(self, digits):
        """
        给定一个数字字符串 digits（例如 "23"），每个数字对应一些字母（如电话键盘），要求输出所有可能的字母组合。
        :type digits: str
        :rtype: List[str]
        分析：
            时间复杂度：

                最多为：3^N 到 4^N，其中 N 是 digits 的长度（每个数字对应 3 或 4 个字母）；

            空间复杂度：

                递归调用栈最多为 O(N)，以及结果列表。
        """
        if not digits:
            return []

        rs = []

        def backtrack(path, start):
            if len(path) == len(digits):
                rs.append(''.join(path))
                return

            for i in range(len(map_digit[digits[start]])):
                path.append(map_digit[digits[start]][i])
                backtrack(path, start + 1)
                path.pop()

        backtrack([], 0)
        return rs
