class Solution(object):
    def isValid(self, s):
        """
        判断给定字符串 s 是否包含有效的括号。有效的括号是指每个左括号都能找到对应的右括号，且括号对的顺序正确。
        :type s: str
        :rtype: bool
        分析：
            存在的问题：
                该解法没有考虑到只包含右括号的情况。

                此解法假设输入字符串的左括号总是出现在右括号之前（两边对称的方式），这可能不是完全正确。比如 "({[})]" 会被错误判断为有效。
        """
        len_ = len(s)
        if len_ % 2 != 0:
            return False
        map_ = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        p1 = 0
        p2 = len_ - 1
        while p1 < p2:
            if s[p1] not in map_ or map_[s[p1]] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
