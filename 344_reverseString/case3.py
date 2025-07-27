class Solution(object):
    def reverseString(self, s):
        """
        给你一个字符数组 s，请你原地反转这个数组，不能使用额外的数组空间。
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        分析：
            双指针更直观地写法
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
