from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        给定字符串 s 和 t，要求在 s 中找到包含 t 所有字符的最短子串，返回该子串。如果没有，返回空字符串
        :type s: str
        :type t: str
        :rtype: str
        分析：
            时间复杂度：O(n)
            空间复杂度为 O(m)
        """
        target = Counter(t)
        missing = len(t)
        i = l = r = 0
        for j, c in enumerate(s, 1):
            missing -= target[c] > 0
            target[c] -= 1
            if not missing:
                while i < j and target[s[i]] < 0:
                    target[s[i]] += 1
                    i += 1
                if not r or j - i < r - l:
                    l, r = i, j
        return s[l:r]
