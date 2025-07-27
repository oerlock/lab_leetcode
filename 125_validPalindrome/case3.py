import re


class Solution(object):
    def isPalindrome(self, s):
        """
        判断输入字符串 s 是否是回文（即正读和反读相同）。但这个判断有一些细节要求：

        只考虑字母和数字，忽略非字母数字字符。

        字母不区分大小写。
        :type s: str
        :rtype: bool
        分析：
            原代码通过将字符串拆分、拼接并处理每个字符来检查回文。虽然这在功能上没有问题，但在空间和效率上可以进一步优化。使用双指针法可以更加高效地完成任务，并避免了中间创建多个临时字符串的操作。
        """
        words = s.split()
        words = ''.join(words)
        words = words.lower()
        words = re.sub(r'[^a-z0-9]', '', words)
        return words == words[::-1]
