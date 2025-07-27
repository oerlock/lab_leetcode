class Solution(object):
    def isValid(self, s):
        """
        判断给定字符串 s 是否包含有效的括号。有效的括号是指每个左括号都能找到对应的右括号，且括号对的顺序正确。
        :type s: str
        :rtype: bool
        分析：
        时间复杂度：O(n)，其中 n 是字符串 s 的长度。每个字符最多被推入和弹出栈一次。

        空间复杂度：O(n)，最坏情况下栈的大小可能是 n（所有字符都是左括号）

        代码最后的判断部分可以简化为：not stack
        """
        if len(s) % 2 != 0:
            return False
        map_ = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        stack = []
        for i in s:
            if i in map_:
                stack.append(i)
            else:
                if not stack or map_[stack.pop()] != i:
                    return False
        return False if stack else True
