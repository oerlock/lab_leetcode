class Solution(object):
    def isPalindrome(self, s):
        """
        判断输入字符串 s 是否是回文（即正读和反读相同）。但这个判断有一些细节要求：

        只考虑字母和数字，忽略非字母数字字符。

        字母不区分大小写。
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            # Move left pointer to a valid character
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer to a valid character
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
