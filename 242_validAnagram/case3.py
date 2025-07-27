class Solution(object):
    def isAnagram(self, s, t):
        """
        给定两个字符串 s 和 t，编写一个函数判断它们是否是字母异位词（Anagram）。

        字母异位词 是指由相同字母组成，但排列顺序不同的字符串。
        :type s: str
        :type t: str
        :rtype: bool
        分析：
            如果你事先判断 len(s) != len(t)，可以提早返回
        """
        # if len(s) != len(t):
        #     return False
        data_1 = {}
        data_2 = {}
        for i in s:
            data_1[i] = data_1.get(i, 0) + 1
        for i in t:
            data_2[i] = data_2.get(i, 0) + 1
        return data_1 == data_2