class Solution(object):
    def isAnagram(self, s, t):
        """
        给定两个字符串 s 和 t，编写一个函数判断它们是否是字母异位词（Anagram）。

        字母异位词 是指由相同字母组成，但排列顺序不同的字符串。
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False
        return True
