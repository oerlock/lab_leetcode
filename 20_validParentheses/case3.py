class Solution(object):
    def isValid(self, s):
        """
        判断给定字符串 s 是否包含有效的括号。有效的括号是指每个左括号都能找到对应的右括号，且括号对的顺序正确。
        :type s: str
        :rtype: bool
        """
        stack = []
        map_ = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in map_:
                if stack and stack[-1] == map_[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack  # Stack should be empty at the end
