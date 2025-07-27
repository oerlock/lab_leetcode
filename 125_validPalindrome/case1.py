class Solution(object):
    def isPalindrome(self, s):
        """
        判断输入字符串 s 是否是回文（即正读和反读相同）。但这个判断有一些细节要求：

        只考虑字母和数字，忽略非字母数字字符。

        字母不区分大小写。
        :type s: str
        :rtype: bool
        分析：
            原代码逻辑清晰，功能上没有问题，但在空间复杂度（O(n)）上存在优化空间
        """
        s_alphanumeric = []
        for i in s:
            # 可以使用 isalnum 代替
            if i.isalpha():
                s_alphanumeric.append(i.lower())
            if i.isdigit():
                s_alphanumeric.append(i)
        for i in range(len(s_alphanumeric) // 2):
            if s_alphanumeric[i] != s_alphanumeric[-(i + 1)]:
                return False
        return True
