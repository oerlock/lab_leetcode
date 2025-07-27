import re


class Solution(object):
    def isPalindrome(self, s):
        """
        判断输入字符串 s 是否是回文（即正读和反读相同）。但这个判断有一些细节要求：

        只考虑字母和数字，忽略非字母数字字符。

        字母不区分大小写。
        :type s: str
        :rtype: bool
        """
        words = re.sub(r'[^a-z0-9]', '', s.lower())
        for i in range(len(words) // 2):
            if words[i] != words[-(i + 1)]:
                return False
        return True
