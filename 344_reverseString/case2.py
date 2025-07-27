class Solution(object):
    def reverseString(self, s):
        """
        给你一个字符数组 s，请你原地反转这个数组，不能使用额外的数组空间。
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        分析：
            case1 的进阶版本
        """
        t = len(s)
        for i in range(t // 2):
            s[i], s[t - i - 1] = s[t - i - 1], s[i]
