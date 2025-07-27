map_digit = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


class Solution(object):
    def letterCombinations(self, digits):
        """
        给定一个数字字符串 digits（例如 "23"），每个数字对应一些字母（如电话键盘），要求输出所有可能的字母组合。
        :type digits: str
        :rtype: List[str]
        分析：
            时间复杂度：
                O(3^N * N) ～ O(4^N * N)
            空间复杂度：
                O(N * k^N)
        """
        if not digits:
            return []

        rs = []

        def backtrack(path, start):
            if len(path) == len(digits):
                rs.append(path)
                return

            for letter in map_digit[digits[start]]:
                backtrack(path + letter, start + 1)

        backtrack('', 0)
        return rs
