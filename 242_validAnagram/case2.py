from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        给定两个字符串 s 和 t，编写一个函数判断它们是否是字母异位词（Anagram）。

        字母异位词 是指由相同字母组成，但排列顺序不同的字符串。
        :type s: str
        :type t: str
        :rtype: bool
        分析：
            非常清晰：两个字符串出现的字符频率一模一样就是异位词。

            但面试时建议你手写逻辑，除非允许用库函数。
        """
        return Counter(s) == Counter(t)
